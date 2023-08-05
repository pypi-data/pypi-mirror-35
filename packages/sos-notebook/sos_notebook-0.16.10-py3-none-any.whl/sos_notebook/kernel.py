#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import argparse
import contextlib
import fnmatch
import logging
import os
import pydoc
import re
import shlex
import subprocess
import sys
import time
from collections import OrderedDict, Sized, defaultdict
from io import StringIO
from textwrap import dedent
from types import ModuleType

import pandas as pd
import pkg_resources
from ipykernel.ipkernel import IPythonKernel
from IPython.core.display import HTML
from IPython.core.error import UsageError
from IPython.lib.clipboard import (ClipboardEmpty, osx_clipboard_get,
                                   tkinter_clipboard_get)
from IPython.utils.tokenutil import line_at_cursor, token_at_cursor
from jupyter_client import find_connection_file, manager
from sos._version import __sos_version__, __version__
from sos.eval import SoS_eval, SoS_exec, interpolate
from sos.syntax import SOS_GLOBAL_SECTION_HEADER, SOS_SECTION_HEADER
from sos.utils import (format_duration, WorkflowDict, env, log_to_file,
                       pretty_size, short_repr)

from ._version import __version__ as __notebook_version__
from .completer import SoS_Completer
from .inspector import SoS_Inspector
from .step_executor import PendingTasks
from .workflow_executor import runfile, NotebookLoggingHandler


class FlushableStringIO:
    '''This is a string buffer for output, but it will only
    keep the first 200 lines and the last 10 lines.
    '''

    def __init__(self, kernel, name, *args, **kwargs):
        self.kernel = kernel
        self.name = name

    def write(self, content):
        if content.startswith('HINT: '):
            content = content.splitlines()
            hint_line = content[0][6:].strip()
            content = '\n'.join(content[1:])
            self.kernel.send_response(self.kernel.iopub_socket, 'display_data',
                                      {
                                          'metadata': {},
                                          'data': {'text/html': HTML(
                                              f'<div class="sos_hint">{hint_line}</div>').data}
                                      })
        if content:
            if self.kernel._meta['capture_result'] is not None:
                self.kernel._meta['capture_result'].append(
                    ('stream', {'name': self.name, 'text': content}))
            self.kernel.send_response(self.kernel.iopub_socket, 'stream',
                                      {'name': self.name, 'text': content})

    def flush(self):
        pass


__all__ = ['SoS_Kernel']


def clipboard_get():
    """ Get text from the clipboard.
    """
    if sys.platform == 'darwin':
        try:
            return osx_clipboard_get()
        except Exception:
            return tkinter_clipboard_get()
    else:
        return tkinter_clipboard_get()


class subkernel(object):
    # a class to information on subkernel
    def __init__(self, name=None, kernel=None, language='', color='', options={}):
        self.name = name
        self.kernel = kernel
        self.language = language
        self.color = color
        self.options = options

    def __repr__(self):
        return f'subkernel {self.name} with kernel {self.kernel} for language {self.language} with color {self.color}'


def header_to_toc(text, id):
    '''Convert a bunch of ## header to TOC'''
    toc = [f'<div class="toc" id="{id}">' if id else '<div class="toc">']
    lines = [x for x in text.splitlines() if x.strip()]
    if not lines:
        return ''
    top_level = min(x.split(' ')[0].count('#') for x in lines)
    level = top_level - 1
    for line in lines:
        header, text = line.split(' ', 1)
        # the header might have anchor link like <a id="videos"></a>
        matched = re.match('.*(<a\s+id="(.*)">.*</a>).*', text)
        anchor = ''
        if matched:
            text = text.replace(matched.group(1), '')
            anchor = matched.group(2)
        # remove image
        matched = re.match('.*(<img .*>).*', text)
        if matched:
            text = text.replace(matched.group(1), '')
        if not anchor:
            anchor = re.sub('[^ a-zA-Z0-9]', '',
                            text).strip().replace(' ', '-')
        # handle ` ` in header
        text = re.sub('`(.*?)`', '<code>\\1</code>', text)
        line_level = header.count('#')
        if line_level > level:
            # level          2
            # line_leval     4
            # add level 3, 4
            for l in range(level + 1, line_level + 1):
                # increase level, new ui
                toc.append(f'<ul class="toc-item lev{l - top_level}">')
        elif line_level < level:
            # level          4
            # line_level     2
            # end level 4 and 3.
            for level in range(level - line_level):
                # end last one
                toc.append('</ul>')
        level = line_level
        toc.append(f'''<li><a href="#{anchor}">{text}</a></li>''')
    # if last level is 4, toplevel is 2 ...
    if level:
        for level in range(level - top_level):
            toc.append('</div>')
    return HTML('\n'.join(toc)).data

# translate a message to transient_display_data message


def make_transient_msg(msg_type, content, title, append=False, page='Info'):
    if msg_type == 'display_data':
        return {
            'title': title,
            'data': content.get('data', {}),
            'metadata': {'append': append, 'page': page}
        }
    elif msg_type == 'stream':
        if content['name'] == 'stdout':
            return {
                'title': title,
                'data': {
                    'text/plain': content['text'],
                    'application/vnd.jupyter.stdout': content['text']
                },
                'metadata': {'append': append, 'page': page}
            }
        else:
            return {
                'title': title,
                'data': {
                    'text/plain': content['text'],
                    'application/vnd.jupyter.stderr': content['text']
                },
                'metadata': {'append': append, 'page': page}
            }
    else:
        raise ValueError(
            f"failed to translate message {msg_type} to transient_display_data message")


class Subkernels(object):
    # a collection of subkernels
    def __init__(self, kernel):
        self.sos_kernel = kernel
        self.language_info = kernel.supported_languages

        from jupyter_client.kernelspec import KernelSpecManager
        km = KernelSpecManager()
        specs = km.find_kernel_specs()
        # get supported languages
        self._kernel_list = []
        lan_map = {}
        for x in self.language_info.keys():
            for lname, knames in kernel.supported_languages[x].supported_kernels.items():
                for kname in knames:
                    if x != kname:
                        lan_map[kname] = (lname, self.get_background_color(self.language_info[x], lname),
                                          getattr(self.language_info[x], 'options', {}))
        # kernel_list has the following items
        #
        # 1. displayed name
        # 2. kernel name
        # 3. language name
        # 4. color
        for spec in specs.keys():
            if spec == 'sos':
                # the SoS kernel will be default theme color.
                self._kernel_list.append(
                    subkernel(name='SoS', kernel='sos', options={
                        'variable_pattern': r'^\s*[_A-Za-z0-9\.]+\s*$',
                        'assignment_pattern': r'^\s*([_A-Za-z0-9\.]+)\s*=.*$'}))
            elif spec in lan_map:
                # e.g. ir ==> R
                self._kernel_list.append(
                    subkernel(name=lan_map[spec][0], kernel=spec, language=lan_map[spec][0],
                              color=lan_map[spec][1], options=lan_map[spec][2]))
            else:
                # undefined language also use default theme color
                self._kernel_list.append(subkernel(name=spec, kernel=spec))

    def kernel_list(self):
        return self._kernel_list

    # now, no kernel is found, name has to be a new name and we need some definition
    # if kernel is defined
    def add_or_replace(self, kdef):
        for idx, x in enumerate(self._kernel_list):
            if x.name == kdef.name:
                self._kernel_list[idx] = kdef
                return self._kernel_list[idx]
            else:
                self._kernel_list.append(kdef)
                return self._kernel_list[-1]

    def get_background_color(self, plugin, lan):
        # if a single color is defined, it is used for all supported
        # languages
        if isinstance(plugin.background_color, str):
            # return the same background color for all inquiry
            return plugin.background_color
        else:
            # return color for specified, or any color if unknown inquiry is made
            return plugin.background_color.get(lan, next(iter(plugin.background_color.values())))

    def find(self, name, kernel=None, language=None, color=None, notify_frontend=True):
        # find from subkernel name
        def update_existing(idx):
            x = self._kernel_list[idx]
            if (kernel is not None and kernel != x.kernel) or (language not in (None, '', 'None') and language != x.language):
                raise ValueError(
                    f'Cannot change kernel or language of predefined subkernel {name} {x}')
            if color is not None:
                if color == 'default':
                    if self._kernel_list[idx].language:
                        self._kernel_list[idx].color = self.get_background_color(
                            self.language_info[self._kernel_list[idx].language], self._kernel_list[idx].language)
                    else:
                        self._kernel_list[idx].color = ''
                else:
                    self._kernel_list[idx].color = color
                if notify_frontend:
                    self.notify_frontend()

        # if the language module cannot be loaded for some reason
        if name in self.sos_kernel._failed_languages:
            raise self.sos_kernel._failed_languages[name]
        # find from language name (subkernel name, which is usually language name)
        for idx, x in enumerate(self._kernel_list):
            if x.name == name:
                if x.name == 'SoS' or x.language or language is None:
                    update_existing(idx)
                    return x
                else:
                    if not kernel:
                        kernel = name
                    break
        # find from kernel name
        for idx, x in enumerate(self._kernel_list):
            if x.kernel == name:
                # if exist language or no new language defined.
                if x.language or language is None:
                    update_existing(idx)
                    return x
                else:
                    # otherwise, try to use the new language
                    kernel = name
                    break

        if kernel is not None:
            # in this case kernel should have been defined in kernel list
            if kernel not in [x.kernel for x in self._kernel_list]:
                raise ValueError(
                    f'Unrecognized Jupyter kernel name {kernel}. Please make sure it is properly installed and appear in the output of command "jupyter kenelspec list"')
            # now this a new instance for an existing kernel
            kdef = [x for x in self._kernel_list if x.kernel == kernel][0]
            if not language:
                if color == 'default':
                    if kdef.language:
                        color = self.get_background_color(
                            self.language_info[kdef.language], kdef.language)
                    else:
                        color = kdef.color
                new_def = self.add_or_replace(subkernel(name, kdef.kernel, kdef.language, kdef.color if color is None else color,
                                                        getattr(self.language_info[kdef.language], 'options', {}) if kdef.language else {}))
                if notify_frontend:
                    self.notify_frontend()
                return new_def
            else:
                # if language is defined,
                if ':' in language:
                    # if this is a new module, let us create an entry point and load
                    from pkg_resources import EntryPoint
                    mn, attr = language.split(':', 1)
                    ep = EntryPoint(name=kernel, module_name=mn,
                                    attrs=tuple(attr.split('.')))
                    try:
                        plugin = ep.resolve()
                        self.language_info[name] = plugin
                        # for convenience, we create two entries for, e.g. R and ir
                        # but only if there is no existing definition
                        for supported_lan, supported_kernels in plugin.supported_kernels.items():
                            for supported_kernel in supported_kernels:
                                if name != supported_kernel and supported_kernel not in self.language_info:
                                    self.language_info[supported_kernel] = plugin
                            if supported_lan not in self.language_info:
                                self.language_info[supported_lan] = plugin
                    except Exception as e:
                        raise RuntimeError(
                            f'Failed to load language {language}: {e}')
                    #
                    if color == 'default':
                        color = self.get_background_color(plugin, kernel)
                    new_def = self.add_or_replace(subkernel(name, kdef.kernel, kernel, kdef.color if color is None else color,
                                                            getattr(plugin, 'options', {})))
                else:
                    # if should be defined ...
                    if language not in self.language_info:
                        raise RuntimeError(
                            f'Unrecognized language definition {language}, which should be a known language name or a class in the format of package.module:class')
                    #
                    self.language_info[name] = self.language_info[language]
                    if color == 'default':
                        color = self.get_background_color(
                            self.language_info[name], language)
                    new_def = self.add_or_replace(subkernel(name, kdef.kernel, language, kdef.color if color is None else color,
                                                            getattr(self.language_info[name], 'options', {})))
                if notify_frontend:
                    self.notify_frontend()
                return new_def
        elif language is not None:
            # kernel is not defined and we only have language
            if ':' in language:
                # if this is a new module, let us create an entry point and load
                from pkg_resources import EntryPoint
                mn, attr = language.split(':', 1)
                ep = EntryPoint(name='__unknown__', module_name=mn,
                                attrs=tuple(attr.split('.')))
                try:
                    plugin = ep.resolve()
                    self.language_info[name] = plugin
                except Exception as e:
                    raise RuntimeError(
                        f'Failed to load language {language}: {e}')
                if name in plugin.supported_kernels:
                    # if name is defined in the module, only search kernels for this language
                    avail_kernels = [x for x in plugin.supported_kernels[name] if
                                     x in [y.kernel for y in self._kernel_list]]
                else:
                    # otherwise we search all supported kernels
                    avail_kernels = [x for x in sum(plugin.supported_kernels.values(), []) if
                                     x in [y.kernel for y in self._kernel_list]]

                if not avail_kernels:
                    raise ValueError(
                        'Failed to find any of the kernels {} supported by language {}. Please make sure it is properly installed and appear in the output of command "jupyter kenelspec list"'.format(
                            ', '.join(sum(plugin.supported_kernels.values(), [])), language))
                # use the first available kernel
                # find the language that has the kernel
                lan_name = list({x: y for x, y in plugin.supported_kernels.items(
                ) if avail_kernels[0] in y}.keys())[0]
                if color == 'default':
                    color = self.get_background_color(plugin, lan_name)
                new_def = self.add_or_replace(subkernel(name, avail_kernels[0], lan_name, self.get_background_color(plugin, lan_name) if color is None else color,
                                                        getattr(plugin, 'options', {})))
            else:
                # if a language name is specified (not a path to module), if should be defined in setup.py
                if language not in self.language_info:
                    raise RuntimeError(
                        f'Unrecognized language definition {language}')
                #
                plugin = self.language_info[language]
                if language in plugin.supported_kernels:
                    avail_kernels = [x for x in plugin.supported_kernels[language] if
                                     x in [y.kernel for y in self._kernel_list]]
                else:
                    avail_kernels = [x for x in sum(plugin.supported_kernels.values(), []) if
                                     x in [y.kernel for y in self._kernel_list]]
                if not avail_kernels:
                    raise ValueError(
                        'Failed to find any of the kernels {} supported by language {}. Please make sure it is properly installed and appear in the output of command "jupyter kenelspec list"'.format(
                            ', '.join(
                                sum(self.language_info[language].supported_kernels.values(), [])),
                            language))

                new_def = self.add_or_replace(subkernel(
                    name, avail_kernels[0], language,
                    self.get_background_color(
                        self.language_info[language], language) if color is None or color == 'default' else color,
                    getattr(self.language_info[language], 'options', {})))

            self.notify_frontend()
            return new_def
        else:
            # let us check if there is something wrong with the pre-defined language
            for entrypoint in pkg_resources.iter_entry_points(group='sos_languages'):
                if entrypoint.name == name:
                    # there must be something wrong, let us trigger the exception here
                    entrypoint.load()
            # if nothing is triggerred, kernel is not defined, return a general message
            raise ValueError(
                f'No subkernel named {name} is found. Please make sure that you have the kernel installed (listed in the output of "jupyter kernelspec list" and usable in jupyter by itself), install appropriate language module (e.g. "pip install sos-r"), restart jupyter notebook and try again.')

    def update(self, notebook_kernel_list):
        for kinfo in notebook_kernel_list:
            try:
                # if we can find the kernel, fine...
                self.find(kinfo[0], kinfo[1], kinfo[2],
                          kinfo[3], notify_frontend=False)
            except Exception as e:
                # otherwise do not worry about it.
                env.logger.warning(
                    f'Failed to locate subkernel {kinfo[0]} with kernerl "{kinfo[1]}" and language "{kinfo[2]}": {e}')

    def notify_frontend(self):
        self._kernel_list.sort(key=lambda x: x.name)
        self.sos_kernel.send_frontend_msg('kernel-list',
                                          [[x.name, x.kernel, x.language, x.color, x.options] for x in self._kernel_list])


class SoS_Kernel(IPythonKernel):
    implementation = 'SOS'
    implementation_version = __version__
    language = 'sos'
    language_version = __sos_version__
    language_info = {
        'mimetype': 'text/x-sos',
        'name': 'sos',
        'file_extension': '.sos',
        'pygments_lexer': 'sos',
        'codemirror_mode': 'sos',
        'nbconvert_exporter': 'sos_notebook.converter.SoS_Exporter',
    }
    banner = "SoS kernel - script of scripts"

    ALL_MAGICS = {
        'cd',
        'capture',
        'clear',
        'debug',
        'dict',
        'expand',
        'get',
        'matplotlib',
        'paste',
        'preview',
        'pull',
        'push',
        'put',
        'render',
        'rerun',
        'revisions',
        'run',
        'save',
        'sandbox',
        'set',
        'sessioninfo',
        'sosrun',
        'sossave',
        'shutdown',
        'taskinfo',
        'tasks',
        'toc',
        'use',
        'with',
    }
    MAGIC_CD = re.compile('^%cd(\s|$)')
    MAGIC_CAPTURE = re.compile('^%capture(\s|$)')
    MAGIC_CLEAR = re.compile('^%clear(\s|$)')
    MAGIC_CONNECT_INFO = re.compile('^%connect_info(\s|$)')
    MAGIC_DEBUG = re.compile('^%debug(\s|$)')
    MAGIC_DICT = re.compile('^%dict(\s|$)')
    MAGIC_EXPAND = re.compile('^%expand(\s|$)')
    MAGIC_GET = re.compile('^%get(\s|$)')
    MAGIC_FRONTEND = re.compile('^%frontend(\s|$)')
    MAGIC_MATPLOTLIB = re.compile('^%matplotlib(\s|$)')
    MAGIC_PASTE = re.compile('^%paste(\s|$)')
    MAGIC_PREVIEW = re.compile('^%preview(\s|$)')
    MAGIC_PULL = re.compile('^%pull(\s|$)')
    MAGIC_PUSH = re.compile('^%push(\s|$)')
    MAGIC_PUT = re.compile('^%put(\s|$)')
    MAGIC_RENDER = re.compile('^%render(\s|$)')
    MAGIC_RERUN = re.compile('^%rerun(\s|$)')
    MAGIC_REVISIONS = re.compile('^%revisions(\s|$)')
    MAGIC_RUN = re.compile('^%run(\s|$)')
    MAGIC_SAVE = re.compile('^%save(\s|$)')
    MAGIC_SANDBOX = re.compile('^%sandbox(\s|$)')
    MAGIC_SKIP = re.compile('^%skip(\s|$)')
    MAGIC_SET = re.compile('^%set(\s|$)')
    MAGIC_SESSIONINFO = re.compile('^%sessioninfo(\s|$)')
    MAGIC_SOSRUN = re.compile('^%sosrun(\s|$)')
    MAGIC_SOSSAVE = re.compile('^%sossave(\s|$)')
    MAGIC_SHUTDOWN = re.compile('^%shutdown(\s|$)')
    MAGIC_TASKINFO = re.compile('^%taskinfo(\s|$)')
    MAGIC_TASKS = re.compile('^%tasks(\s|$)')
    MAGIC_TOC = re.compile('^%toc(\s|$)')
    MAGIC_USE = re.compile('^%use(\s|$)')
    MAGIC_WITH = re.compile('^%with(\s|$)')

    def get_capture_parser(self):
        parser = argparse.ArgumentParser(prog='%capture',
                                         description='''Capture output (stdout) or output file from a subkernel
                                         as variable in SoS''')
        parser.add_argument('msg_type', nargs='?', default='stdout', choices=['stdout', 'stderr', 'text', 'markdown',
                'html', 'raw'],
                        help='''Message type to capture, default to standard output. In terms of Jupyter message
                        types, "stdout" refers to "stream" message with "stdout" type, "stderr" refers to "stream"
                        message with "stderr" type, "text", "markdown" and "html" refers to "display_data" message
                        with "text/plain", "text/markdown" and "text/html" type respectively. If "raw" is specified,
                        all returned messages will be returned in a list format.''')
        parser.add_argument('--as', dest='as_type', default='text', nargs='?', choices=('text', 'json', 'csv', 'tsv'),
                            help='''How to interpret the captured text. This only applicable to stdout, stderr and
                            text message type where the text from cell output will be collected. If this
                            option is given, SoS will try to parse the text as json, csv (comma separated text),
                             tsv (tab separated text), and store text (from text), Pandas DataFrame
                            (from csv or tsv), dict or other types (from json) to the variable.''')
        grp = parser.add_mutually_exclusive_group(required=False)
        grp.add_argument('-t', '--to', dest='__to__', metavar='VAR',
                         help='''Name of variable to which the captured content will be saved. If no varialbe is
                         specified, the return value will be saved to variable "__captured" and be displayed
                         at the side panel. ''')
        grp.add_argument('-a', '--append', dest='__append__', metavar='VAR',
                         help='''Name of variable to which the captured content will be appended.
                            This option is equivalent to --to if VAR does not exist. If VAR exists
                            and is of the same type of new content (str or dict or DataFrame), the
                            new content will be appended to VAR if VAR is of str (str concatenation),
                            dict (dict update), or DataFrame (DataFrame.append) types. If VAR is of
                            list type, the new content will be appended to the end of the list.''')
        parser.error = self._parse_error
        return parser

    def get_clear_parser(self):
        parser = argparse.ArgumentParser(prog='%clear',
                                         description='''Clear the output of the current cell, or the current
            active cell if executed in the sidepanel.''')
        parser.add_argument('-a', '--all', action='store_true',
                            help='''Clear all output or selected status or class of the current notebook.''')
        grp = parser.add_mutually_exclusive_group()
        grp.add_argument('-s', '--status', nargs='+',
                         help='''Clear tasks that match specifie status (e.g. completed).''')
        grp.add_argument('-c', '--class', nargs='+', dest='elem_class',
                         help='''Clear all HTML elements with specified classes (e.g. sos_hint)''')
        parser.error = self._parse_error
        return parser

    def get_debug_parser(self):
        parser = argparse.ArgumentParser(prog='%debug',
                                         description='''Turn on or off debug information''')
        parser.add_argument('status', choices=['on', 'off'],
                            help='''Turn on or off debugging''')
        parser.error = self._parse_error
        return parser

    def get_expand_parser(self):
        parser = argparse.ArgumentParser(prog='%expand',
                                         description='''Expand the script in the current cell with default ({}) or
                specified sigil.''')
        parser.add_argument('sigil', nargs='?', help='''Sigil to be used to interpolated the
            texts. It can be quoted, or be specified as two options.''')
        parser.add_argument('right_sigil', nargs='?', help='''Right sigil if the sigil is
            specified as two pieces.''')
        parser.error = self._parse_error
        return parser

    def get_get_parser(self):
        parser = argparse.ArgumentParser(prog='%get',
                                         description='''Get specified variables from another kernel, which is
                by default the SoS kernel.''')
        parser.add_argument('--from', dest='__from__',
                            help='''Name of kernel from which the variables will be obtained.
                Default to the SoS kernel.''')
        parser.add_argument('vars', nargs='*',
                            help='''Names of SoS variables''')
        parser.error = self._parse_error
        return parser

    def get_matplotlib_parser(self):
        parser = argparse.ArgumentParser(prog='%matplotlib',
                                         description='''Set matplotlib parser type''')
        parser.add_argument('gui', choices=['agg', 'gtk', 'gtk3', 'inline', 'ipympl', 'nbagg',
                                            'notebook', 'osx', 'pdf', 'ps', 'qt', 'qt4', 'qt5', 'svg', 'tk', 'widget', 'wx'],
                            nargs='?',
                            help='''Name of the matplotlib backend to use (‘agg’, ‘gtk’, ‘gtk3’,''')
        parser.add_argument('-l', '--list', action='store_true',
                            help='''Show available matplotlib backends''')
        parser.error = self._parse_error
        return parser

    def get_preview_parser(self):
        parser = argparse.ArgumentParser(prog='%preview',
                                         description='''Preview files, sos variables, or expressions in the
                side panel, or notebook if side panel is not opened, unless
                options --panel or --notebook is specified.''')
        parser.add_argument('items', nargs='*',
                            help='''Filename, variable name, or expression. Wildcard characters
                such as '*' and '?' are allowed for filenames.''')
        parser.add_argument('-k', '--kernel',
                            help='''kernel in which variables will be previewed. By default
            the variable will be previewed in the current kernel of the cell.''')
        parser.add_argument('-w', '--workflow', action='store_true',
                            help='''Preview notebook workflow''')
        parser.add_argument('-o', '--keep-output', action='store_true',
                            help='''Do not clear the output of the side panel.''')
        # this option is currently hidden
        parser.add_argument('-s', '--style', choices=['table', 'scatterplot', 'png'],
                            help='''Option for preview file or variable, which by default is "table"
            for Pandas DataFrame. The %%preview magic also accepts arbitrary additional
            keyword arguments, which would be interpreted by individual style. Passing
            '-h' with '--style' would display the usage information of particular
            style.''')
        parser.add_argument('-r', '--host', dest='host', metavar='HOST',
                            help='''Preview files on specified remote host, which should
            be one of the hosts defined in sos configuration files.''')
        parser.add_argument('--off', action='store_true',
                            help='''Turn off file preview''')
        loc = parser.add_mutually_exclusive_group()
        loc.add_argument('-p', '--panel', action='store_true',
                         help='''Preview in side panel even if the panel is currently closed''')
        loc.add_argument('-n', '--notebook', action='store_true',
                         help='''Preview in the main notebook.''')
        parser.add_argument('-c', '--config', help='''A configuration file with host
            definitions, in case the definitions are not defined in global or local
            sos config.yml files.''')
        parser.error = self._parse_error
        return parser

    def get_pull_parser(self):
        parser = argparse.ArgumentParser('pull',
                                         description='''Pull files or directories from remote host to local host''')
        parser.add_argument('items', nargs='+', help='''Files or directories to be
            retrieved from remote host. The files should be relative to local file
            system. The files to retrieve are determined by "path_map"
            determined by "paths" definitions of local and remote hosts.''')
        parser.add_argument('-f', '--from', dest='host',
                            help='''Remote host to which the files will be sent, which should
            be one of the hosts defined in sos configuration files.''')
        parser.add_argument('-c', '--config', help='''A configuration file with host
            definitions, in case the definitions are not defined in global or local
            sos config.yml files.''')
        parser.add_argument('-v', '--verbosity', type=int, choices=range(5), default=2,
                            help='''Output error (0), warning (1), info (2), debug (3) and trace (4)
                information to standard output (default to 2).''')
        parser.error = self._parse_error
        return parser

    def get_push_parser(self):
        parser = argparse.ArgumentParser('push',
                                         description='''Push local files or directory to a remote host''')
        parser.add_argument('items', nargs='+', help='''Files or directories to be sent
            to remote host. The location of remote files are determined by "path_map"
            determined by "paths" definitions of local and remote hosts.''')
        parser.add_argument('-t', '--to', dest='host',
                            help='''Remote host to which the files will be sent. SoS will list all
            configured queues if no such key is defined''')
        parser.add_argument('-c', '--config', help='''A configuration file with host
            definitions, in case the definitions are not defined in global or local
            sos config.yml files.''')
        parser.add_argument('-v', '--verbosity', type=int, choices=range(5), default=2,
                            help='''Output error (0), warning (1), info (2), debug (3) and trace (4)
                information to standard output (default to 2).''')
        parser.error = self._parse_error
        return parser

    def get_put_parser(self):
        parser = argparse.ArgumentParser(prog='%put',
                                         description='''Put specified variables in the subkernel to another
            kernel, which is by default the SoS kernel.''')
        parser.add_argument('--to', dest='__to__',
                            help='''Name of kernel from which the variables will be obtained.
                Default to the SoS kernel.''')
        parser.add_argument('vars', nargs='*',
                            help='''Names of SoS variables''')
        parser.error = self._parse_error
        return parser

    def get_render_parser(self):
        parser = argparse.ArgumentParser(prog='%render',
                                         description='''Treat the output of a SoS cell as another format, default to markdown.''')
        parser.add_argument('msg_type', default='stdout', choices=['stdout', 'text'], nargs='?',
                        help='''Message type to capture, default to standard output. In terms of Jupyter message
                        types, "stdout" refers to "stream" message with "stdout" type, and "text" refers to
                        "display_data" message with "text/plain" type.''')
        parser.add_argument('--as', dest='as_type', default='Markdown', nargs='?',
                            help='''Format to render output of cell, default to Markdown, but can be any
            format that is supported by the IPython.display module such as HTML, Math, JSON,
            JavaScript and SVG.''')
        parser.error = self._parse_error
        return parser

    def get_rerun_parser(self):
        parser = argparse.ArgumentParser(prog='%rerun',
                                         description='''Re-execute the last executed code, most likely with
            different command line options''')
        parser.error = self._parse_error
        return parser

    def get_run_parser(self):
        parser = argparse.ArgumentParser(prog='%run',
                                         description='''Execute the current cell with specified command line
            arguments. Arguments set by magic %set will be appended at the
            end of command line''')
        parser.error = self._parse_error
        return parser

    def get_revisions_parser(self):
        parser = argparse.ArgumentParser(prog='%revision',
                                         description='''Revision history of the document, parsed from the log
            message of the notebook if it is kept in a git repository. Additional parameters to "git log" command
            (e.g. -n 5 --since --after) could be specified to limit the revisions to display.''')
        parser.add_argument('-s', '--source', nargs='?', default='',
                            help='''Source URL to to create links for revisions.
            SoS automatically parse source URL of the origin and provides variables "repo" for complete origin
            URL without trailing ".git" (e.g. https://github.com/vatlab/sos-notebook), "path" for complete
            path name (e.g. src/document/doc.ipynb), "filename" for only the name of the "path", and "revision"
            for revisions. Because sos interpolates command line by default, variables in URL template should be
            included with double braceses (e.g. --source {{repo}}/blob/{{revision}}/{{path}})). If this option is
            provided without value and the document is hosted on github, a default template will be provided.''')
        parser.add_argument('-l', '--links', nargs='+', help='''Name and URL or additional links for related
            files (e.g. --links report URL_to_repo ) with URL interpolated as option --source.''')
        parser.error = self._parse_error
        return parser

    def get_save_parser(self):
        parser = argparse.ArgumentParser(prog='%save',
                                         description='''Save the content of the cell (after the magic itself) to specified file''')
        parser.add_argument('filename',
                            help='''Filename of saved report or script.''')
        parser.add_argument('-f', '--force', action='store_true',
                            help='''If destination file already exists, overwrite it.''')
        parser.add_argument('-a', '--append', action='store_true',
                            help='''If destination file already exists, append to it.''')
        parser.add_argument('-x', '--set-executable', dest="setx", action='store_true',
                            help='''Set `executable` permission to saved script.''')
        parser.error = self._parse_error
        return parser

    def get_set_parser(self):
        parser = argparse.ArgumentParser(prog='%set',
                                         description='''Set persistent command line options for SoS runs.''')
        parser.error = self._parse_error
        return parser

    def get_sessioninfo_parser(self):
        parser = argparse.ArgumentParser(prog='%sessioninfo',
                                         description='''List the session info of all subkernels, and information
            stored in variable sessioninfo''')
        parser.error = self._parse_error
        return parser

    def get_shutdown_parser(self):
        parser = argparse.ArgumentParser(prog='%shutdown',
                                         description='''Shutdown or restart specified subkernel''')
        parser.add_argument('kernel', nargs='?',
                            help='''Name of the kernel to be restarted, default to the
            current running kernel.''')
        parser.add_argument('-r', '--restart', action='store_true',
                            help='''Restart the kernel''')
        parser.error = self._parse_error
        return parser

    def get_sosrun_parser(self):
        parser = argparse.ArgumentParser(prog='%sosrun',
                                         description='''Execute the entire notebook with steps consisting of SoS
            cells (cells with SoS kernel) with section header, with specified command
            line arguments. Arguments set by magic %set will be appended at the
            end of command line''')
        parser.error = self._parse_error
        return parser

    def get_sossave_parser(self):
        parser = argparse.ArgumentParser(prog='%sossave',
                                         description='''Save the jupyter notebook as workflow (consisting of all sos
            steps defined in cells starting with section header) or a HTML report to
            specified file.''')
        parser.add_argument('filename', nargs='?',
                            help='''Filename of saved report or script. Default to notebookname with file
            extension determined by option --to.''')
        parser.add_argument('-t', '--to', dest='__to__', choices=['sos', 'html'],
                            help='''Destination format, default to sos.''')
        parser.add_argument('-c', '--commit', action='store_true',
                            help='''Commit the saved file to git directory using command
            git commit FILE''')
        parser.add_argument('-a', '--all', action='store_true',
                            help='''The --all option for sos convert script.ipynb script.sos, which
            saves all cells and their metadata to a .sos file, that contains all input
            information of the notebook but might not be executable in batch mode.''')
        parser.add_argument('-m', '--message',
                            help='''Message for git commit. Default to "save FILENAME"''')
        parser.add_argument('-p', '--push', action='store_true',
                            help='''Push the commit with command "git push"''')
        parser.add_argument('-f', '--force', action='store_true',
                            help='''If destination file already exists, overwrite it.''')
        parser.add_argument('-x', '--set-executable', dest="setx", action='store_true',
                            help='''Set `executable` permission to saved script.''')
        parser.add_argument('--template', default='default-sos-template',
                            help='''Template to generate HTML output. The default template is a
            template defined by configuration key default-sos-template, or
            sos-report if such a key does not exist.''')
        parser.error = self._parse_error
        return parser

    def get_taskinfo_parser(self):
        parser = argparse.ArgumentParser(prog='%taskinfo',
                                         description='''Get information on specified task. By default
            sos would query against all running task queues but it would
            start a task queue and query status if option -q is specified.
            ''')
        parser.add_argument('task', help='ID of task')
        parser.add_argument('-q', '--queue',
                            help='''Task queue on which the task is executed.''')
        parser.add_argument('-c', '--config', help='''A configuration file with host
            definitions, in case the definitions are not defined in global or local
            sos config.yml files.''')
        parser.error = self._parse_error
        return parser

    def get_tasks_parser(self):
        parser = argparse.ArgumentParser(prog='%tasks',
                                         description='''Show a list of tasks from specified queue''')
        parser.add_argument('tasks', nargs='*', help='ID of tasks')
        parser.add_argument('-s', '--status', nargs='*',
                            help='''Display tasks of specified status. Default to all.''')
        parser.add_argument('-q', '--queue',
                            help='''Task queue on which the tasks are retrived.''')
        parser.add_argument('--age', help='''Limit to tasks that is created more than
            (default) or within specified age. Value of this parameter can be in units
            s (second), m (minute), h (hour), or d (day, default), with optional
            prefix + for older (default) and - for younder than specified age.''')
        parser.add_argument('-c', '--config', help='''A configuration file with host
            definitions, in case the definitions are not defined in global or local
            sos config.yml files.''')
        parser.error = self._parse_error
        return parser

    def get_toc_parser(self):
        parser = argparse.ArgumentParser(prog='%toc',
                                         description='''Generate a table of content from the current notebook.''')
        loc = parser.add_mutually_exclusive_group()
        loc.add_argument('-p', '--panel', action='store_true',
                         help='''Show the TOC in side panel even if the panel is currently closed''')
        loc.add_argument('-n', '--notebook', action='store_true',
                         help='''Show the TOC in the main notebook.''')
        parser.add_argument(
            '--id', help='''Optional ID of the generated TOC.''')
        parser.error = self._parse_error
        return parser

    def get_use_parser(self):
        parser = argparse.ArgumentParser(prog='%use',
                                         description='''Switch to an existing subkernel
            or start a new subkernel.''')
        parser.add_argument('name', nargs='?', default='',
                            help='''Displayed name of kernel to start (if no kernel with name is
            specified) or switch to (if a kernel with this name is already started).
            The name is usually a kernel name (e.g. %%use ir) or a language name
            (e.g. %%use R) in which case the language name will be used. One or
            more parameters --language or --kernel will need to be specified
            if a new name is used to start a separate instance of a kernel.''')
        parser.add_argument('-k', '--kernel',
                            help='''kernel name as displayed in the output of jupyter kernelspec
            list. Default to the default kernel of selected language (e.g. ir for
            language R.''')
        parser.add_argument('-l', '--language',
                            help='''Language extension that enables magics such as %%get and %%put
            for the kernel, which should be in the name of a registered language
            (e.g. R), or a specific language module in the format of
            package.module:class. SoS maitains a list of languages and kernels
            so this option is only needed for starting a new instance of a kernel.
            ''')
        parser.add_argument('-c', '--color',
                            help='''Background color of new or existing kernel, which overrides
            the default color of the language. A special value "default" can be
            used to reset color to default.''')
        parser.add_argument('-r', '--restart', action='store_true',
                            help='''Restart the kernel if it is running.''')
        parser.error = self._parse_error
        return parser

    def get_with_parser(self):
        parser = argparse.ArgumentParser(prog='%with',
                                         description='''Use specified subkernel to evaluate current
            cell, with optional input and output variables''')
        parser.add_argument('name', nargs='?', default='',
                            help='''Name of an existing kernel.''')
        parser.add_argument('-i', '--in', nargs='*', dest='in_vars',
                            help='Input variables (variables to get from SoS kernel)')
        parser.add_argument('-o', '--out', nargs='*', dest='out_vars',
                            help='''Output variables (variables to put back to SoS kernel
            before switching back to the SoS kernel''')
        parser.error = self._parse_error
        return parser

    def get_supported_languages(self):
        if self._supported_languages is not None:
            return self._supported_languages
        group = 'sos_languages'
        self._supported_languages = {}

        for entrypoint in pkg_resources.iter_entry_points(group=group):
            # Grab the function that is the actual plugin.
            name = entrypoint.name
            try:
                plugin = entrypoint.load()
                self._supported_languages[name] = plugin
            except Exception as e:
                self._failed_languages[name] = e
        return self._supported_languages

    supported_languages = property(lambda self: self.get_supported_languages())

    def get_kernel_list(self):
        if not hasattr(self, '_subkernels'):
            self._subkernels = Subkernels(self)

        # sort kernel list by name to avoid unnecessary change of .ipynb files
        return self._subkernels

    subkernels = property(lambda self: self.get_kernel_list())

    def get_completer(self):
        if self._completer is None:
            self._completer = SoS_Completer(self)
        return self._completer

    completer = property(lambda self: self.get_completer())

    def get_inspector(self):
        if self._inspector is None:
            self._inspector = SoS_Inspector(self)
        return self._inspector

    inspector = property(lambda self: self.get_inspector())

    def __init__(self, **kwargs):
        super(SoS_Kernel, self).__init__(**kwargs)
        self.options = ''
        self.kernel = 'SoS'
        # a dictionary of started kernels, with the format of
        #
        # 'R': ['ir', 'sos.R.sos_R', '#FFEEAABB']
        #
        # Note that:
        #
        # 'R' is the displayed name of the kernel.
        # 'ir' is the kernel name.
        # 'sos.R.sos_R' is the language module.
        # '#FFEEAABB' is the background color
        #
        self.kernels = {}
        # self.shell = InteractiveShell.instance()
        self.format_obj = self.shell.display_formatter.format

        self.previewers = None
        self.original_keys = None
        self._meta = {'use_panel': True}
        self._supported_languages = None
        self._completer = None
        self._inspector = None
        self._real_execution_count = 1
        self._execution_count = 1
        self._debug_mode = False
        self.frontend_comm = None
        self.comm_manager.register_target('sos_comm', self.sos_comm)
        self.my_tasks = {}
        self.last_executed_code = ''
        self._kernel_return_vars = []
        self._failed_languages = {}
        env.__task_notifier__ = self.notify_task_status
        # enable matplotlib by default #77
        self.shell.enable_gui = lambda gui: None
        # sos does not yet support MaxOSX backend to start a new window
        # so a default inline mode is used.
        self.shell.enable_matplotlib('inline')
        #
        self.editor_kernel = 'sos'
        # remove all other ahdnlers
        env.logger.handlers = []
        env.logger.addHandler(
            NotebookLoggingHandler(logging.DEBUG, kernel=self))

    cell_id = property(lambda self: self._meta['cell_id'])
    _workflow_mode = property(lambda self: self._meta['workflow_mode'])
    _resume_execution = property(lambda self: self._meta['resume_execution'])

    def handle_magic_revisions(self, args, unknown_args):
        filename = self._meta['notebook_name'] + '.ipynb'
        path = self._meta['notebook_path']
        revisions = subprocess.check_output(['git', 'log'] + unknown_args + ['--date=short', '--pretty=%H!%cN!%cd!%s',
                                                                             '--', filename]).decode().splitlines()
        if not revisions:
            return
        # args.source is None for --source without option
        if args.source != '' or args.links:
            # need to determine origin etc for interpolation
            try:
                origin = subprocess.check_output(
                    ['git', 'ls-remote', '--get-url', 'origin']).decode().strip()
                repo = origin[:-4] if origin.endswith('.git') else origin
            except Exception as e:
                repo = ''
                if self._debug_mode:
                    self.warn(f'Failed to get repo URL: {e}')
            if args.source is None:
                if 'github.com' in repo:
                    args.source = '{repo}/blob/{revision}/{path}'
                    if self._debug_mode:
                        self.warn(
                            f"source is set to {args.source} with repo={repo}")
                else:
                    args.source = ''
                    self.warn(
                        f'A default source URL is unavailable for repository {repo}')
        text = '''
        <table class="revision_table">
        <tr>
        <th>Revision</th>
        <th>Author</th>
        <th>Date</th>
        <th>Message</th>
        <tr>
        '''
        for line in revisions:
            fields = line.split('!', 3)
            revision = fields[0]
            fields[0] = f'<span class="revision_id">{fields[0][:7]}<span>'
            if args.source != '':
                # source URL
                URL = interpolate(args.source, {'revision': revision, 'repo': repo,
                                                'filename': filename, 'path': path})
                fields[0] = f'<a target="_blank" href="{URL}">{fields[0]}</a>'
            links = []
            if args.links:
                for i in range(len(args.links) // 2):
                    name = args.links[2 * i]
                    if len(args.links) == 2 * i + 1:
                        continue
                    URL = interpolate(args.links[2 * i + 1],
                                      {'revision': revision, 'repo': repo, 'filename': filename, 'path': path})
                    links.append(f'<a target="_blank" href="{URL}">{name}</a>')
            if links:
                fields[0] += ' (' + ', '.join(links) + ')'
            text += '<tr>' + \
                '\n'.join(f'<td>{x}</td>' for x in fields) + '</tr>'
        text += '</table>'
        self.send_response(self.iopub_socket, 'display_data',
                           {
                               'metadata': {},
                               'data': {'text/html': HTML(text).data}
                           })

    def handle_taskinfo(self, task_id, task_queue):
        # requesting information on task
        from sos.hosts import Host
        host = Host(task_queue)
        result = host._task_engine.query_tasks(
            [task_id], verbosity=2, html=True)
        # log_to_file(result)
        self.send_frontend_msg('display_data', {
            'metadata': {},
            'data': {'text/plain': result,
                     'text/html': HTML(result).data
                     }}, title=f'%taskinfo {task_id} -q {task_queue}', page='Tasks')

        # now, there is a possibility that the status of the task is different from what
        # task engine knows (e.g. a task is rerun outside of jupyter). In this case, since we
        # already get the status, we should update the task engine...
        #
        # <tr><th align="right"  width="30%">Status</th><td align="left"><div class="one_liner">completed</div></td></tr>
        status = result.split(
            '>Status<', 1)[-1].split('</div', 1)[0].split('>')[-1]
        host._task_engine.update_task_status(task_id, status)

    def handle_tasks(self, tasks, queue='localhost', status=None, age=None):
        from sos.hosts import Host
        try:
            host = Host(queue)
        except Exception as e:
            self.warn('Invalid task queu {}: {}'.format(queue, e))
            return
        # get all tasks
        for tid, tst, tdt in host._task_engine.monitor_tasks(tasks, status=status, age=age):
            self.notify_task_status(['new-status', queue, tid, tst, tdt])
        self.send_frontend_msg('update-duration', {})

    def handle_sessioninfo(self):
        #
        from sos.utils import loaded_modules
        result = OrderedDict()
        #
        result['SoS'] = [('SoS Version', __version__)]
        result['SoS'].extend(loaded_modules(env.sos_dict))
        #
        cur_kernel = self.kernel
        try:
            for kernel in self.kernels.keys():
                kinfo = self.subkernels.find(kernel)
                self.switch_kernel(kernel)
                result[kernel] = [
                    ('Kernel', kinfo.kernel),
                    ('Language', kinfo.language)
                ]
                if kernel not in self.supported_languages:
                    continue
                lan = self.supported_languages[kernel]
                if hasattr(lan, 'sessioninfo'):
                    try:
                        sinfo = lan(self, kinfo.kernel).sessioninfo()
                        if isinstance(sinfo, str):
                            result[kernel].append([sinfo])
                        elif isinstance(sinfo, dict):
                            result[kernel].extend(list(sinfo.items()))
                        elif isinstance(sinfo, list):
                            result[kernel].extend(sinfo)
                        else:
                            self.warn(f'Unrecognized session info: {sinfo}')
                    except Exception as e:
                        self.warn(
                            f'Failed to obtain sessioninfo of kernel {kernel}: {e}')
        finally:
            self.switch_kernel(cur_kernel)
        #
        if 'sessioninfo' in env.sos_dict:
            result.update(env.sos_dict['sessioninfo'])
        #
        res = ''
        for key, items in result.items():
            res += f'<p class="session_section">{key}</p>\n'
            res += '<table class="session_info">\n'
            for item in items:
                res += '<tr>\n'
                if isinstance(item, str):
                    res += f'<td colspan="2"><pre>{item}</pre></td>\n'
                elif len(item) == 1:
                    res += f'<td colspan="2"><pre>{item[0]}</pre></td>\n'
                elif len(item) == 2:
                    res += f'<th>{item[0]}</th><td><pre>{item[1]}</pre></td>\n'
                else:
                    self.warn(
                        f'Invalid session info item of type {item.__class__.__name__}: {short_repr(item)}')
                res += '</tr>\n'
            res += '</table>\n'
        self.send_response(self.iopub_socket, 'display_data',
                           {'metadata': {},
                            'data': {'text/html': HTML(res).data}})

    def sos_comm(self, comm, msg):
        # record frontend_comm to send messages
        self.frontend_comm = comm

        @comm.on_msg
        def handle_frontend_msg(msg):
            content = msg['content']['data']
            # log_to_file(msg)
            for k, v in content.items():
                if k == 'list-kernel':
                    if v:
                        self.subkernels.update(v)
                    self.subkernels.notify_frontend()
                elif k == 'set-editor-kernel':
                    self.editor_kernel = v
                elif k == 'kill-task':
                    # kill specified task
                    from sos.hosts import Host
                    Host(v[1])._task_engine.kill_tasks([v[0]])
                    self.notify_task_status(
                        ['change-status', v[1], v[0], 'aborted', (None, None, None)])
                elif k == 'resume-task':
                    # kill specified task
                    from sos.hosts import Host
                    Host(v[1])._task_engine.resume_task(v[0])
                    self.notify_task_status(
                        ['change-status', v[1], v[0], 'pending', (None, None, None)])
                elif k == 'task-info':
                    self._meta['use_panel'] = True
                    self.handle_taskinfo(v[0], v[1])
                elif k == 'update-task-status':
                    if not isinstance(v, list):
                        continue
                    # split by host ...
                    host_status = defaultdict(list)
                    for name in v:
                        if not name.startswith('status_'):
                            continue
                        try:
                            tqu, tid = name[7:].rsplit('_', 1)
                        except Exception:
                            # incorrect ID...
                            continue
                        host_status[tqu].append(tid)
                    # log_to_file(host_status)
                    #
                    from sos.hosts import Host
                    for tqu, tids in host_status.items():
                        try:
                            h = Host(tqu)
                        except Exception:
                            continue
                        for _, tst, tdt in h._task_engine.monitor_tasks(tids):
                            self.notify_task_status(
                                ['change-status', tqu, tid, tst, tdt])
                    self.send_frontend_msg('update-duration', {})
                elif k == 'paste-table':
                    try:
                        from tabulate import tabulate
                        df = pd.read_clipboard()
                        tbl = tabulate(df, headers='keys', tablefmt='pipe')
                        self.send_frontend_msg('paste-table', tbl)
                        if self._debug_mode:
                            log_to_file(tbl)
                    except Exception as e:
                        self.send_frontend_msg(
                            'alert', f'Failed to paste clipboard as table: {e}')
                elif k == 'notebook-version':
                    # send the version of notebook, right now we will not do anything to it, but
                    # we will send the version of sos-notebook there
                    self.send_frontend_msg(
                        'notebook-version', __notebook_version__)
                else:
                    # this somehow does not work
                    self.warn(f'Unknown message {k}: {v}')

    status_class = {
        'pending': 'fa-square-o',
        'submitted': 'fa-spinner',
        'running': 'fa-spinner fa-pulse fa-spin',
        'completed': 'fa-check-square-o',
        'failed': 'fa-times-circle-o',
        'aborted': 'fa-frown-o',
        'missing': 'fa-question',
        'unknown': 'fa-question',
    }

    def notify_task_status(self, task_status):
        action_class = {
            'pending': 'fa-stop',
            'submitted': 'fa-stop',
            'running': 'fa-stop',
            'completed': 'fa-play',
            'failed': 'fa-play',
            'aborted': 'fa-play',
            'missing': 'fa-question',
            'unknown': 'fa-question',
        }

        action_func = {
            'pending': 'kill_task',
            'submitted': 'kill_task',
            'running': 'kill_task',
            'completed': 'resume_task',
            'failed': 'resume_task',
            'aborted': 'resume_task',
            'missing': 'function(){}',
            'unknown': 'function(){}',
        }
        if task_status[0] == 'new-status':
            tqu, tid, tst, tdt = task_status[1:]
            # tdt contains cretion time, start running time, and duration time.
            if tdt[2]:
                timer = f'Ran for {format_duration(tdt[2])}</time>'
            elif tdt[1]:
                # start running
                timer = f'<time id="duration_{tqu}_{tid}" class="{tst}" datetime="{tdt[1]*1000}">Ran for {format_duration(time.time() - tdt[1])}</time>'
            else:
                timer = f'<time id="duration_{tqu}_{tid}" class="{tst}" datetime="{tdt[0]*1000}">Pending for {format_duration(time.time() - tdt[0])}</time>'
            self.send_response(self.iopub_socket, 'display_data',
                               {
                                   'metadata': {},
                                   'data': {'text/html':
                                            HTML(f'''<table id="table_{tqu}_{tid}" class="task_table"><tr style="border: 0px">
                        <td style="border: 0px">
                        <i id="status_{tqu}_{tid}"
                            class="fa fa-2x fa-fw {self.status_class[tst]}"
                            onmouseover="'{self.status_class[tst]}'.split(' ').map(x => document.getElementById('status_{tqu}_{tid}').classList.remove(x));'{action_class[tst]} task_hover'.split(' ').map(x => document.getElementById('status_{tqu}_{tid}').classList.add(x));"
                            onmouseleave="'{action_class[tst]} task_hover'.split(' ').map(x => document.getElementById('status_{tqu}_{tid}').classList.remove(x));'{self.status_class[tst]}'.split(' ').map(x => document.getElementById('status_{tqu}_{tid}').classList.add(x));"
                            onclick="{action_func[tst]}('{tid}', '{tqu}')"
                        ></i> </td>
                        <td style="border:0px"><a href='#' onclick="task_info('{tid}', '{tqu}')"><pre>{tid}</pre></a></td>
                        <td style="border:0px">&nbsp;</td>
                        <td style="border:0px;text-align=right;">
                        <pre><span id="tagline_{tqu}_{tid}">{timer}</span></pre></td>
                        </tr>
                        </table>''').data}})
            # keep tracks of my tasks to avoid updating status of
            # tasks that does not belong to the notebook
            self.my_tasks[(tqu, tid)] = time.time()
        elif task_status[0] == 'remove-task':
            tqu, tid = task_status[1:]
            if (tqu, tid) in self.my_tasks:
                self.send_frontend_msg('remove-task', [tqu, tid])
        elif task_status[0] == 'change-status':
            tqu, tid, tst, tdt = task_status[1:]
            if tst not in ('pending', 'submitted', 'running', 'completed',
                           'failed', 'aborted'):
                tst = 'unknown'
            self.send_frontend_msg('task-status',
                                   [tqu, tid, tst, tdt, self.status_class[tst], action_class[tst], action_func[tst]])
            self.my_tasks[(tqu, tid)] = time.time()
        elif task_status[0] == 'pulse-status':
            tqu, tid, tst, tdt = task_status[1:]
            if tst not in ('pending', 'submitted', 'running', 'completed',
                           'failed', 'aborted'):
                tst = 'unknown'
            if (tqu, tid) in self.my_tasks:
                if time.time() - self.my_tasks[(tqu, tid)] < 20:
                    # if it has been within the first 20 seconds of new or updated message
                    # can confirm to verify it has been successfully delivered. Otherwise
                    # ignore such message
                    self.send_frontend_msg('task-status',
                                           [tqu, tid, tst, tdt, self.status_class[tst], action_class[tst], action_func[tst]])
            else:
                # perhaps the pulse one does not have an initial value yet
                self.send_frontend_msg('task-status',
                                       [tqu, tid, tst, tdt, self.status_class[tst], action_class[tst], action_func[tst]])
                self.my_tasks[(tqu, tid)] = time.time()
        else:
            raise RuntimeError(
                f'Unrecognized status change message {task_status}')

    def send_frontend_msg(self, msg_type, msg=None, title='', append=False, page='Info'):
        # if comm is never created by frontend, the kernel is in test mode without frontend
        if msg_type in ('display_data', 'stream'):
            if self._meta['use_panel'] is False:
                if msg_type in ('display_data', 'stream'):
                    self.send_response(self.iopub_socket, msg_type,
                                       {} if msg is None else msg)
            else:
                self.frontend_comm.send(
                    make_transient_msg(
                        msg_type, msg, append=append, title=title, page=page),
                    {'msg_type': 'transient_display_data'})
        elif self.frontend_comm:
            self.frontend_comm.send({} if msg is None else msg, {
                                    'msg_type': msg_type})
        elif self._debug_mode:
            # we should not always do this because the kernel could be triggered by
            # tests, which will not have a frontend sos comm
            self.warn(
                'Frontend communicator is broken. Please restart jupyter server')

    def _reset_dict(self):
        env.sos_dict = WorkflowDict()
        SoS_exec('import os, sys, glob', None)
        SoS_exec('from sos.runtime import *', None)
        SoS_exec("run_mode = 'interactive'", None)
        self.original_keys = set(env.sos_dict._dict.keys()) | {'SOS_VERSION', 'CONFIG',
                                                               'step_name', '__builtins__', 'input', 'output',
                                                               'depends'}

    @contextlib.contextmanager
    def redirect_sos_io(self):
        save_stdout = sys.stdout
        save_stderr = sys.stderr
        sys.stdout = FlushableStringIO(self, 'stdout')
        sys.stderr = FlushableStringIO(self, 'stderr')
        yield
        sys.stdout = save_stdout
        sys.stderr = save_stderr

    def do_is_complete(self, code):
        '''check if new line is in order'''
        code = code.strip()
        if not code:
            return {'status': 'complete', 'indent': ''}
        if any(code.startswith(x) for x in ['%dict', '%paste', '%edit', '%cd', '!']):
            return {'status': 'complete', 'indent': ''}
        if code.endswith(':') or code.endswith(','):
            return {'status': 'incomplete', 'indent': '  '}
        lines = code.split('\n')
        if lines[-1].startswith(' ') or lines[-1].startswith('\t'):
            # if it is a new line, complte
            empty = [idx for idx, x in enumerate(
                lines[-1]) if x not in (' ', '\t')][0]
            return {'status': 'incomplete', 'indent': lines[-1][:empty]}
        #
        if SOS_SECTION_HEADER.match(lines[-1]):
            return {'status': 'incomplete', 'indent': ''}
        #
        return {'status': 'incomplete', 'indent': ''}

    def do_inspect(self, code, cursor_pos, detail_level=0):
        if self.editor_kernel.lower() == 'sos':
            line, offset = line_at_cursor(code, cursor_pos)
            name = token_at_cursor(code, cursor_pos)
            data = self.inspector.inspect(name, line, cursor_pos - offset)
            return {
                'status': 'ok',
                'metadata': {},
                'found': True if data else False,
                'data': data
            }
        else:
            cell_kernel = self.subkernels.find(self.editor_kernel)
            try:
                _, KC = self.kernels[cell_kernel.name]
            except Exception as e:
                if self._debug_mode:
                    log_to_file(f'Failed to get subkernels {cell_kernel.name}')
                KC = self.KC
            try:
                KC.inspect(code, cursor_pos)
                while KC.shell_channel.msg_ready():
                    msg = KC.shell_channel.get_msg()
                    if msg['header']['msg_type'] == 'inspect_reply':
                        return msg['content']
                    else:
                        # other messages, do not know what is going on but
                        # we should not wait forever and cause a deadloop here
                        if self._debug_mode:
                            log_to_file(
                                f"complete_reply not obtained: {msg['header']['msg_type']} {msg['content']} returned instead")
                        break
            except Exception as e:
                if self._debug_mode:
                    log_to_file(f'Completion fail with exception: {e}')

    def do_complete(self, code, cursor_pos):
        if self.editor_kernel.lower() == 'sos':
            text, matches = self.completer.complete_text(code, cursor_pos)
            return {'matches': matches,
                    'cursor_end': cursor_pos,
                    'cursor_start': cursor_pos - len(text),
                    'metadata': {},
                    'status': 'ok'}
        else:
            cell_kernel = self.subkernels.find(self.editor_kernel)
            try:
                _, KC = self.kernels[cell_kernel.name]
            except Exception as e:
                if self._debug_mode:
                    log_to_file(f'Failed to get subkernels {cell_kernel.name}')
                KC = self.KC
            try:
                KC.complete(code, cursor_pos)
                while KC.shell_channel.msg_ready():
                    msg = KC.shell_channel.get_msg()
                    if msg['header']['msg_type'] == 'complete_reply':
                        return msg['content']
                    else:
                        # other messages, do not know what is going on but
                        # we should not wait forever and cause a deadloop here
                        if self._debug_mode:
                            log_to_file(
                                f"complete_reply not obtained: {msg['header']['msg_type']} {msg['content']} returned instead")
                        break
            except Exception as e:
                if self._debug_mode:
                    log_to_file(f'Completion fail with exception: {e}')

    def warn(self, message):
        message = str(message).rstrip() + '\n'
        if message.strip():
            self.send_response(self.iopub_socket, 'stream',
                               {'name': 'stderr', 'text': message})

    def get_magic_and_code(self, code, warn_remaining=False):
        if code.startswith('%') or code.startswith('!'):
            lines = re.split(r'(?<!\\)\n', code, 1)
            # remove lines joint by \
            lines[0] = lines[0].replace('\\\n', '')
        else:
            lines = code.split('\n', 1)

        pieces = self._interpolate_text(
            lines[0], quiet=False).strip().split(None, 1)
        if len(pieces) == 2:
            command_line = pieces[1]
        else:
            command_line = ''
        remaining_code = lines[1] if len(lines) > 1 else ''
        if warn_remaining and remaining_code.strip():
            self.warn('Statement {} ignored'.format(
                short_repr(remaining_code)))
        return command_line, remaining_code

    def run_cell(self, code, silent, store_history, on_error=None):
        #
        if not self.KM.is_alive():
            self.send_response(self.iopub_socket, 'stream',
                               dict(name='stdout', text='Restarting kernel "{}"\n'.format(self.kernel)))
            self.KM.restart_kernel(now=False)
            self.KC = self.KM.client()
        # flush stale replies, which could have been ignored, due to missed heartbeats
        while self.KC.shell_channel.msg_ready():
            self.KC.shell_channel.get_msg()
        # executing code in another kernel
        self.KC.execute(code, silent=silent, store_history=store_history)

        # first thing is wait for any side effects (output, stdin, etc.)
        _execution_state = "busy"
        while _execution_state != 'idle':
            # display intermediate print statements, etc.
            while self.KC.stdin_channel.msg_ready():
                sub_msg = self.KC.stdin_channel.get_msg()
                if self._debug_mode:
                    log_to_file(f"MSG TYPE {sub_msg['header']['msg_type']}")
                    log_to_file(f'CONTENT  {sub_msg}')
                if sub_msg['header']['msg_type'] != 'input_request':
                    self.send_response(
                        self.stdin_socket, sub_msg['header']['msg_type'], sub_msg["content"])
                else:
                    content = sub_msg["content"]
                    if content['password']:
                        res = self.getpass(prompt=content['prompt'])
                    else:
                        res = self.raw_input(prompt=content['prompt'])
                    self.KC.input(res)
            while self.KC.iopub_channel.msg_ready():
                sub_msg = self.KC.iopub_channel.get_msg()
                msg_type = sub_msg['header']['msg_type']
                if self._debug_mode:
                    log_to_file(f'MSG TYPE {msg_type}')
                    log_to_file(f'CONTENT  {sub_msg["content"]}')
                if msg_type == 'status':
                    _execution_state = sub_msg["content"]["execution_state"]
                else:
                    if msg_type in ('execute_input', 'execute_result'):
                        # override execution count with the master count,
                        # not sure if it is needed
                        sub_msg['content']['execution_count'] = self._execution_count
                    #
                    if msg_type in ['display_data', 'stream', 'execute_result', 'update_display_data']:
                        if self._meta['capture_result'] is not None:
                            self._meta['capture_result'].append((msg_type, sub_msg['content']))
                        if silent:
                            continue
                    self.send_response(
                        self.iopub_socket, msg_type, sub_msg['content'])
        #
        # now get the real result
        reply = self.KC.get_shell_msg(timeout=10)
        reply['content']['execution_count'] = self._execution_count
        return reply['content']

    def switch_kernel(self, kernel, in_vars=None, ret_vars=None, kernel_name=None, language=None, color=None):
        # switching to a non-sos kernel
        if not kernel:
            kinfo = self.subkernels.find(self.kernel)
            self.send_response(self.iopub_socket, 'stream',
                               dict(name='stdout', text='''\
Active subkernels: {}
Available subkernels:\n{}'''.format(', '.join(self.kernels.keys()),
                                    '\n'.join(['    {} ({})'.format(x.name, x.kernel) for x in self.subkernels.kernel_list()]))))
            return
        kinfo = self.subkernels.find(kernel, kernel_name, language, color)
        if kinfo.name == self.kernel:
            # the same kernel, do nothing?
            # but the senario can be
            #
            # kernel in SoS
            # cell R
            # %use R -i n
            #
            # SoS get:
            #
            # %softwidth --default-kernel R --cell-kernel R
            # %use R -i n
            #
            # Now, SoS -> R without variable passing
            # R -> R should honor -i n

            # or, when we randomly jump cells, we should more aggreessively return
            # automatically shared variables to sos (done by the following) (#375)
            if kinfo.name != 'SoS':
                self.switch_kernel('SoS')
                self.switch_kernel(kinfo.name, in_vars, ret_vars)
        elif kinfo.name == 'SoS':
            self.handle_magic_put(self._kernel_return_vars)
            self._kernel_return_vars = []
            self.kernel = 'SoS'
        elif self.kernel != 'SoS':
            # not to 'sos' (kernel != 'sos'), see if they are the same kernel under
            self.switch_kernel('SoS', in_vars, ret_vars)
            self.switch_kernel(kinfo.name, in_vars, ret_vars)
        else:
            if self._debug_mode:
                self.warn(f'Switch from {self.kernel} to {kinfo.name}')
            # case when self.kernel == 'sos', kernel != 'sos'
            # to a subkernel
            new_kernel = False
            if kinfo.name not in self.kernels:
                # start a new kernel
                try:
                    self.kernels[kinfo.name] = manager.start_new_kernel(
                        startup_timeout=60, kernel_name=kinfo.kernel, cwd=os.getcwd())
                    new_kernel = True
                except Exception as e:
                    # try toget error message
                    import tempfile
                    with tempfile.TemporaryFile() as ferr:
                        try:
                            # this should fail
                            manager.start_new_kernel(
                                startup_timeout=60, kernel_name=kinfo.kernel, cwd=os.getcwd(),
                                stdout=subprocess.DEVNULL, stderr=ferr)
                        except:
                            ferr.seek(0)
                            self.warn(
                                f'Failed to start kernel "{kernel}". {e}\nError Message:\n{ferr.read().decode()}')
                    return
            self.KM, self.KC = self.kernels[kinfo.name]
            self._kernel_return_vars = [] if ret_vars is None else ret_vars
            self.kernel = kinfo.name
            if new_kernel and self.kernel in self.supported_languages:
                init_stmts = self.supported_languages[self.kernel](
                    self, kinfo.kernel).init_statements
                if init_stmts:
                    self.run_cell(init_stmts, True, False)
            # passing
            self.handle_magic_get(in_vars)

    def shutdown_kernel(self, kernel, restart=False):
        kernel = self.subkernels.find(kernel).name
        if kernel == 'SoS':
            # cannot restart myself ...
            self.warn('Cannot restart SoS kernel from within SoS.')
        elif kernel:
            if kernel not in self.kernels:
                self.send_response(self.iopub_socket, 'stream',
                                   dict(name='stdout', text=f'{kernel} is not running'))
            elif restart:
                orig_kernel = self.kernel
                try:
                    # shutdown
                    self.shutdown_kernel(kernel)
                    # switch back to kernel (start a new one)
                    self.switch_kernel(kernel)
                finally:
                    # finally switch to starting kernel
                    self.switch_kernel(orig_kernel)
            else:
                # shutdown
                if self.kernel == kernel:
                    self.switch_kernel('SoS')
                try:
                    self.kernels[kernel][0].shutdown_kernel(restart=False)
                except Exception as e:
                    self.warn(f'Failed to shutdown kernel {kernel}: {e}\n')
                finally:
                    self.kernels.pop(kernel)
        else:
            self.send_response(self.iopub_socket, 'stream',
                               dict(name='stdout', text='Specify one of the kernels to shutdown: SoS{}\n'
                                    .format(''.join(f', {x}' for x in self.kernels))))

    def _parse_error(self, msg):
        self.warn(msg)

    def get_dict_parser(self):
        parser = argparse.ArgumentParser(prog='%dict',
                                         description='Inspect or reset SoS dictionary')
        parser.add_argument('vars', nargs='*')
        parser.add_argument('-k', '--keys', action='store_true',
                            help='Return only keys')
        parser.add_argument('-r', '--reset', action='store_true',
                            help='Rest SoS dictionary (clear all user variables)')
        parser.add_argument('-a', '--all', action='store_true',
                            help='Return all variales, including system functions and variables')
        parser.add_argument('-d', '--del', nargs='+', metavar='VAR', dest='__del__',
                            help='Remove specified variables from SoS dictionary')
        parser.error = self._parse_error
        return parser

    def get_sandbox_parser(self):
        parser = argparse.ArgumentParser(prog='%sandbox',
                                         description='''Execute content of a cell in a temporary directory
                with fresh dictionary (by default).''')
        parser.add_argument('-d', '--dir',
                            help='''Execute workflow in specified directory. The directory
                will be created if does not exist, and will not be removed
                after the completion. ''')
        parser.add_argument('-k', '--keep-dict', action='store_true',
                            help='''Keep current sos dictionary.''')
        parser.add_argument('-e', '--expect-error', action='store_true',
                            help='''If set, expect error from the excution and report
                success if an error occurs.''')
        parser.error = self._parse_error
        return parser

    def handle_magic_dict(self, line):
        'Magic that displays content of the dictionary'
        # do not return __builtins__ beacuse it is too long...
        parser = self.get_dict_parser()
        try:
            args = parser.parse_args(shlex.split(line))
        except SystemExit:
            return

        for x in args.vars:
            if not x in env.sos_dict:
                self.warn(
                    'Unrecognized sosdict option or variable name {}'.format(x))
                return

        if args.reset:
            self._reset_dict()
            return

        if args.__del__:
            for x in args.__del__:
                if x in env.sos_dict:
                    env.sos_dict.pop(x)
            return

        if args.keys:
            if args.all:
                self.send_result(env.sos_dict._dict.keys())
            elif args.vars:
                self.send_result(set(args.vars))
            else:
                self.send_result({x for x in env.sos_dict._dict.keys(
                ) if not x.startswith('__')} - self.original_keys)
        else:
            if args.all:
                self.send_result(env.sos_dict._dict)
            elif args.vars:
                self.send_result(
                    {x: y for x, y in env.sos_dict._dict.items() if x in args.vars})
            else:
                self.send_result({x: y for x, y in env.sos_dict._dict.items() if
                                  x not in self.original_keys and not x.startswith('__')})

    def handle_magic_set(self, options):
        if options.strip():
            # self.send_response(self.iopub_socket, 'stream',
            #    {'name': 'stdout', 'text': 'sos options set to "{}"\n'.format(options)})
            if not options.strip().startswith('-'):
                self.warn(
                    f'Magic %set cannot set positional argument, {options} provided.\n')
            else:
                self.options = options.strip()
                self.send_response(self.iopub_socket, 'stream',
                                   dict(name='stdout', text=f'Set sos options to "{self.options}"\n'))
        else:
            if self.options:
                self.send_response(self.iopub_socket, 'stream',
                                   dict(name='stdout', text=f'Reset sos options from "{self.options}" to ""\n'))
                self.options = ''
            else:
                self.send_response(self.iopub_socket, 'stream',
                                   {'name': 'stdout',
                                    'text': 'Usage: set persistent sos command line options such as "-v 3" (debug output)\n'})

    def handle_magic_get(self, items, from_kernel=None, explicit=False):
        if from_kernel is None or from_kernel.lower() == 'sos':
            # autmatically get all variables with names start with 'sos'
            default_items = [x for x in env.sos_dict.keys() if x.startswith(
                'sos') and x not in self.original_keys]
            items = default_items if not items else items + default_items
            for item in items:
                if item not in env.sos_dict:
                    self.warn(f'Variable {item} does not exist')
                    return
            if not items:
                return
            if self.kernel in self.supported_languages:
                lan = self.supported_languages[self.kernel]
                kinfo = self.subkernels.find(self.kernel)
                try:
                    lan(self, kinfo.kernel).get_vars(items)
                except Exception as e:
                    self.warn(f'Failed to get variable: {e}\n')
                    return
            elif self.kernel == 'SoS':
                self.warn(
                    'Magic %get without option --kernel can only be executed by subkernels')
                return
            else:
                if explicit:
                    self.warn(
                        f'Magic %get failed because the language module for {self.kernel} is not properly installed. Please install it according to language specific instructions on the Running SoS section of the SoS homepage and restart Jupyter server.')
                return
        elif self.kernel.lower() == 'sos':
            # if another kernel is specified and the current kernel is sos
            # we get from subkernel
            try:
                self.switch_kernel(from_kernel)
                self.handle_magic_put(items)
            except Exception as e:
                self.warn(
                    f'Failed to get {", ".join(items)} from {from_kernel}: {e}')
            finally:
                self.switch_kernel('SoS')
        else:
            # if another kernel is specified, we should try to let that kernel pass
            # the variables to this one directly
            try:
                my_kernel = self.kernel
                self.switch_kernel(from_kernel)
                # put stuff to sos or my_kernel directly
                self.handle_magic_put(
                    items, to_kernel=my_kernel, explicit=explicit)
            except Exception as e:
                self.warn(
                    f'Failed to get {", ".join(items)} from {from_kernel}: {e}')
            finally:
                # then switch back
                self.switch_kernel(my_kernel)

    def get_response(self, statement, msg_types, name=None):
        # get response of statement of specific msg types.
        responses = []
        self.KC.execute(statement, silent=False, store_history=False)
        # first thing is wait for any side effects (output, stdin, etc.)
        _execution_state = "busy"
        while _execution_state != 'idle':
            # display intermediate print statements, etc.
            while self.KC.iopub_channel.msg_ready():
                sub_msg = self.KC.iopub_channel.get_msg()
                msg_type = sub_msg['header']['msg_type']
                if self._debug_mode:
                    log_to_file(f'Received {msg_type} {sub_msg["content"]}')
                if msg_type == 'status':
                    _execution_state = sub_msg["content"]["execution_state"]
                else:
                    if msg_type in msg_types and (name is None or sub_msg['content'].get('name', None) in name):
                        if self._debug_mode:
                            log_to_file(
                                f'Capture response: {msg_type}: {sub_msg["content"]}')
                        responses.append([msg_type, sub_msg['content']])
                    else:
                        if self._debug_mode:
                            log_to_file(
                                f'Non-response: {msg_type}: {sub_msg["content"]}')
                        self.send_response(
                            self.iopub_socket, msg_type, sub_msg['content'])
        if not responses and self._debug_mode:
            self.warn(
                f'Failed to get a response from message type {msg_types} for the execution of {statement}')
        return responses

    def handle_magic_put(self, items, to_kernel=None, explicit=False):
        if self.kernel.lower() == 'sos':
            if to_kernel is None:
                self.warn(
                    'Magic %put without option --kernel can only be executed by subkernels')
                return
            # if another kernel is specified and the current kernel is sos
            try:
                # switch to kernel and bring in items
                self.switch_kernel(to_kernel, in_vars=items)
            except Exception as e:
                self.warn(
                    f'Failed to put {", ".join(items)} to {to_kernel}: {e}')
            finally:
                # switch back
                self.switch_kernel('SoS')
        else:
            # put to sos kernel or another kernel
            #
            # items can be None if unspecified
            if not items:
                # we do not simply return because we need to return default variables (with name startswith sos
                items = []
            if self.kernel not in self.supported_languages:
                if explicit:
                    self.warn(
                        f'Subkernel {self.kernel} does not support magic %put.')
                return
            #
            lan = self.supported_languages[self.kernel]
            kinfo = self.subkernels.find(self.kernel)
            # pass language name to to_kernel
            try:
                if to_kernel:
                    objects = lan(self, kinfo.kernel).put_vars(
                        items, to_kernel=self.subkernels.find(to_kernel).language)
                else:
                    objects = lan(self, kinfo.kernel).put_vars(
                        items, to_kernel='SoS')
            except Exception as e:
                # if somethign goes wrong in the subkernel does not matter
                if self._debug_mode:
                    self.warn(
                        f'Failed to call put_var({items}) from {kinfo.kernel}')
                objects = {}
            if isinstance(objects, dict):
                # returns a SOS dictionary
                try:
                    env.sos_dict.update(objects)
                except Exception as e:
                    self.warn(
                        f'Failed to put {", ".join(items)} to {to_kernel}: {e}')
                    return

                if to_kernel is None:
                    return
                # if another kernel is specified and the current kernel is not sos
                # we need to first put to sos then to another kernel
                try:
                    my_kernel = self.kernel
                    # switch to the destination kernel and bring in vars
                    self.switch_kernel(to_kernel, in_vars=items)
                except Exception as e:
                    self.warn(
                        f'Failed to put {", ".join(items)} to {to_kernel}: {e}')
                finally:
                    # switch back to the original kernel
                    self.switch_kernel(my_kernel)
            elif isinstance(objects, str):
                # an statement that will be executed in the destination kernel
                if to_kernel is None or to_kernel == 'SoS':
                    # evaluate in SoS, this should not happen or rarely happen
                    # because the subkernel should return a dictionary for SoS kernel
                    try:
                        exec(objects, env.sos_dict._dict)
                    except Exception as e:
                        self.warn(
                            f'Failed to put variables {items} to SoS kernel: {e}')
                        return
                try:
                    my_kernel = self.kernel
                    # switch to the destination kernel
                    self.switch_kernel(to_kernel)
                    # execute the statement to pass variables directly to destination kernel
                    self.run_cell(objects, True, False)
                except Exception as e:
                    self.warn(
                        f'Failed to put {", ".join(items)} to {to_kernel}: {e}')
                finally:
                    # switch back to the original kernel
                    self.switch_kernel(my_kernel)
            else:
                self.warn(
                    f'Unrecognized return value of type {object.__class__.__name__} for action %put')
                return

    def handle_magic_pull(self, args):
        from sos.hosts import Host
        if args.config:
            from sos.utils import load_config_files
            load_config_files(args.config)
        env.sos_dict['CONFIG']
        try:
            host = Host(args.host)
            #
            received = host.receive_from_host(args.items)
            #
            msg = '{} item{} received from {}:<br>{}'.format(len(received),
                                                             ' is' if len(
                                                                 received) <= 1 else 's are', args.host,
                                                             '<br>'.join([f'{x} <= {received[x]}' for x in
                                                                          sorted(received.keys())]))
            self.send_response(self.iopub_socket, 'display_data',
                               {
                                   'metadata': {},
                                   'data': {'text/html': HTML(f'<div class="sos_hint">{msg}</div>').data}
                               })
        except Exception as e:
            self.warn(f'Failed to retrieve {", ".join(args.items)}: {e}')

    def handle_magic_push(self, args):
        from sos.hosts import Host
        if args.config:
            from sos.utils import load_config_files
            load_config_files(args.config)
        env.sos_dict['CONFIG']
        try:
            host = Host(args.host)
            #
            sent = host.send_to_host(args.items)
            #
            msg = '{} item{} sent to {}:<br>{}'.format(len(sent),
                                                       ' is' if len(
                                                           sent) <= 1 else 's are', args.host,
                                                       '<br>'.join([f'{x} => {sent[x]}' for x in sorted(sent.keys())]))
            self.send_response(self.iopub_socket, 'display_data',
                               {
                                   'metadata': {},
                                   'data': {'text/html': HTML(f'<div class="sos_hint">{msg}</div>').data}
                               })
        except Exception as e:
            self.warn(f'Failed to send {", ".join(args.items)}: {e}')

    def _interpolate_text(self, text, quiet=False):
        # interpolate command
        try:
            new_text = interpolate(text, local_dict=env.sos_dict._dict)
            if new_text != text and not quiet:
                self.send_response(self.iopub_socket, 'display_data',
                                   {
                                       'metadata': {},
                                       'data': {
                                           'text/html': HTML(
                                               f'<div class="sos_hint">> {new_text.strip() + "<br>"}</div>').data}
                                   })
            return new_text
        except Exception as e:
            self.warn(f'Failed to interpolate {short_repr(text)}: {e}\n')
            return None

    def handle_magic_preview(self, items, kernel=None, style=None, title=''):
        handled = [False for x in items]
        for idx, item in enumerate(items):
            try:
                # quoted
                if (item.startswith('"') and item.endswith('"')) or \
                        (item.startswith("'") and item.endswith("'")):
                    try:
                        item = eval(item)
                    except Exception:
                        pass
                item = os.path.expanduser(item)
                if os.path.isfile(item):
                    self.preview_file(item, style, title=title)
                    handled[idx] = True
                    continue
                if os.path.isdir(item):
                    handled[idx] = True
                    _, dirs, files = os.walk(item).__next__()
                    self.send_frontend_msg('display_data',
                                           {'metadata': {},
                                            'data': {'text/plain': '>>> ' + item + ':\n',
                                                     'text/html': HTML(
                                                         f'<div class="sos_hint">> {item}: directory<br>{len(files)}  file{"s" if len(files)>1 else ""}<br>{len(dirs)}  subdirector{"y" if len(dirs)<=1 else "ies"}</div>').data
                                                     }
                                            }, title=title, append=False, page='Preview')
                    continue
                else:
                    import glob
                    files = glob.glob(item)
                    if files:
                        for pfile in files:
                            self.preview_file(pfile, style, title=title)
                        handled[idx] = True
                        continue
            except Exception as e:
                self.warn(f'\n> Failed to preview file {item}: {e}')
                continue

        # non-sos kernel
        use_sos = kernel in ('sos', 'SoS') or (
            kernel is None and self.kernel == 'SoS')
        orig_kernel = self.kernel
        if kernel is not None and self.kernel != self.subkernels.find(kernel).name:
            self.switch_kernel(kernel)
        if self._meta['use_panel']:
            self.send_frontend_msg(
                'preview-kernel', self.kernel, page='Preview')
        try:
            for idx, item in enumerate(items):
                try:
                    # quoted
                    if (item.startswith('"') and item.endswith('"')) or \
                            (item.startswith("'") and item.endswith("'")):
                        try:
                            item = eval(item)
                        except Exception:
                            pass
                    if use_sos:
                        obj_desc, preview = self.preview_var(item, style)
                        if preview is None:
                            continue
                        else:
                            format_dict, md_dict = preview
                        self.send_frontend_msg('display_data',
                                               {'metadata': {},
                                                'data': {'text/plain': '>>> ' + item + ':\n',
                                                         'text/html': HTML(
                                                             f'<div class="sos_hint">> {item}: {obj_desc}</div>').data
                                                         }
                                                }, title=title, append=True, page='Preview')
                        self.send_frontend_msg('display_data',
                                               {'execution_count': self._execution_count, 'data': format_dict,
                                                'metadata': md_dict}, title=title, append=True, page='Preview')
                    else:
                        # evaluate
                        responses = self.get_response(
                            item, ['stream', 'display_data', 'execution_result', 'error'])
                        if not self._debug_mode:
                            # if the variable or expression is invalid, do not do anything
                            responses = [
                                x for x in responses if x[0] != 'error']
                        if responses:
                            self.send_frontend_msg('display_data',
                                                   {'metadata': {},
                                                    'data': {'text/plain': '>>> ' + item + ':\n',
                                                             'text/html': HTML(
                                                                 f'<div class="sos_hint">> {item}:</div>').data
                                                             }
                                                    }, title=title, append=True, page='Preview')
                            for response in responses:
                                # self.warn(f'{response[0]} {response[1]}' )
                                self.send_frontend_msg(
                                    response[0], response[1], title=title, append=True, page='Preview')
                        else:
                            raise ValueError(
                                f'Cannot preview expresison {item}')
                except Exception as e:
                    if not handled[idx]:
                        self.send_frontend_msg('stream',
                                               dict(name='stderr',
                                                    text='> Failed to preview file or expression {}{}'.format(
                                                        item, f': {e}' if self._debug_mode else '')),
                                               title=title, append=True, page='Preview')
        finally:
            self.switch_kernel(orig_kernel)

    def handle_magic_cd(self, option):
        if not option:
            return
        to_dir = option.strip()
        try:
            os.chdir(os.path.expanduser(to_dir))
            self.send_response(self.iopub_socket, 'stream',
                               {'name': 'stdout', 'text': os.getcwd()})
        except Exception as e:
            self.warn(
                f'Failed to change dir to {os.path.expanduser(to_dir)}: {e}')
            return
        #
        cur_kernel = self.kernel
        try:
            for kernel in self.kernels.keys():
                if kernel not in self.supported_languages:
                    self.warn(
                        f'Current directory of kernel {kernel} is not changed: unsupported language')
                    continue
                lan = self.supported_languages[kernel]
                if hasattr(lan, 'cd_command'):
                    try:
                        self.switch_kernel(kernel)
                        cmd = interpolate(lan.cd_command, {'dir': to_dir})
                        self.run_cell(
                            cmd, True, False, on_error=f'Failed to execute {cmd} in {kernel}')
                    except Exception as e:
                        self.warn(
                            f'Current directory of kernel {kernel} is not changed: {e}')
                else:
                    self.warn(
                        f'Current directory of kernel {kernel} is not changed: cd_command not defined')
        finally:
            self.switch_kernel(cur_kernel)

    def handle_shell_command(self, cmd):
        # interpolate command
        if not cmd:
            return
        from sos.utils import pexpect_run
        try:
            with self.redirect_sos_io():
                pexpect_run(cmd, shell=True,
                            win_width=40 if self._meta['cell_id'] == "" else 80)
        except Exception as e:
            self.warn(e)

    def run_sos_code(self, code, silent):
        code = dedent(code)
        with self.redirect_sos_io():
            try:
                # record input and output
                fopt = ''
                res = runfile(
                    code=code, raw_args=self.options + fopt, kernel=self)
                self.send_result(res, silent)
            except PendingTasks as e:
                # send cell index and task IDs to frontend
                self.send_frontend_msg(
                    'tasks-pending', [self._meta['cell_id'], e.tasks])
                return
            except Exception as e:
                sys.stderr.flush()
                sys.stdout.flush()
                # self.send_response(self.iopub_socket, 'display_data',
                #    {
                #        'metadata': {},
                #        'data': { 'text/html': HTML('<hr color="black" width="60%">').data}
                #    })
                raise
            except KeyboardInterrupt:
                self.warn('Keyboard Interrupt\n')
                return {'status': 'abort', 'execution_count': self._execution_count}
            finally:
                sys.stderr.flush()
                sys.stdout.flush()
        #
        if not silent and (not hasattr(self, 'preview_output') or self.preview_output):
            # Send standard output
            # if os.path.isfile('.sos/report.md'):
            #    with open('.sos/report.md') as sr:
            #        sos_report = sr.read()
            # with open(self.report_file, 'a') as summary_report:
            #    summary_report.write(sos_report + '\n\n')
            #    if sos_report.strip():
            #        self.send_response(self.iopub_socket, 'display_data',
            #            {
            #                'metadata': {},
            #                'data': {'text/markdown': sos_report}
            #            })
            #
            if 'step_input' in env.sos_dict:
                input_files = env.sos_dict['step_input']
                if input_files is None:
                    input_files = []
                else:
                    input_files = [
                        x for x in input_files if isinstance(x, str)]
            else:
                input_files = []
            if 'step_output' in env.sos_dict:
                output_files = env.sos_dict['step_output']
                if output_files is None:
                    output_files = []
                else:
                    output_files = [
                        x for x in output_files if isinstance(x, str)]
            else:
                output_files = []
            # use a table to list input and/or output file if exist
            if output_files:
                title = f'%preview {" ".join(output_files)}'
                if not self._meta['use_panel']:
                    self.send_response(self.iopub_socket, 'display_data',
                                       {
                                           'metadata': {},
                                           'data': {'text/html': HTML(f'<div class="sos_hint">{title}</div>').data}
                                       })

                if hasattr(self, 'in_sandbox') and self.in_sandbox:
                    # if in sand box, do not link output to their files because these
                    # files will be removed soon.
                    self.send_frontend_msg('display_data',
                                           {
                                               'metadata': {},
                                               'data': {'text/html':
                                                        HTML(
                                                            '''<div class="sos_hint"> input: {}<br>output: {}\n</div>'''.format(
                                                                ', '.join(
                                                                    x for x in input_files),
                                                                ', '.join(x for x in output_files))).data
                                                        }
                                           }, title=title, page='Preview')
                else:
                    self.send_frontend_msg('display_data',
                                           {
                                               'metadata': {},
                                               'data': {'text/html':
                                                        HTML(
                                                            '''<div class="sos_hint"> input: {}<br>output: {}\n</div>'''.format(
                                                                ', '.join(
                                                                    f'<a target="_blank" href="{x}">{x}</a>' for x
                                                                    in input_files),
                                                                ', '.join(
                                                                    f'<a target="_blank" href="{x}">{x}</a>' for x
                                                                    in output_files))).data
                                                        }
                                           }, title=title, page='Preview')
                for filename in output_files:
                    self.preview_file(filename, style=None, title=title)

    def preview_var(self, item, style=None):
        if item in env.sos_dict:
            obj = env.sos_dict[item]
        else:
            obj = SoS_eval(item)
        # get the basic information of object
        txt = type(obj).__name__
        # we could potentially check the shape of data frame and matrix
        # but then we will need to import the numpy and pandas libraries
        if hasattr(obj, 'shape') and getattr(obj, 'shape') is not None:
            txt += f' of shape {getattr(obj, "shape")}'
        elif isinstance(obj, Sized):
            txt += f' of length {obj.__len__()}'
        if isinstance(obj, ModuleType):
            return txt, ({'text/plain': pydoc.render_doc(obj, title='SoS Documentation: %s')}, {})
        elif hasattr(obj, 'to_html') and getattr(obj, 'to_html') is not None:
            try:
                from sos.visualize import Visualizer
                result = Visualizer(self, style).preview(obj)
                if isinstance(result, (list, tuple)) and len(result) == 2:
                    return txt, result
                elif isinstance(result, dict):
                    return txt, (result, {})
                elif result is None:
                    return txt, None
                else:
                    raise ValueError(
                        f'Unrecognized return value from visualizer: {short_repr(result)}.')
            except Exception as e:
                self.warn(f'Failed to preview variable: {e}')
                return txt, self.format_obj(obj)
        else:
            return txt, self.format_obj(obj)

    def preview_file(self, filename, style=None, title=''):
        if not os.path.isfile(filename):
            self.warn('\n> ' + filename + ' does not exist')
            return
        self.send_frontend_msg('display_data',
                               {'metadata': {},
                                'data': {
                                    'text/plain': f'\n> {filename} ({pretty_size(os.path.getsize(filename))}):',
                                    'text/html': HTML(
                                        f'<div class="sos_hint">> {filename} ({pretty_size(os.path.getsize(filename))}):</div>').data,
                               }
                               }, title=title, append=True, page='Preview')
        previewer_func = None
        # lazy import of previewers
        if self.previewers is None:
            from sos.preview import get_previewers
            self.previewers = get_previewers()
        for x, y, _ in self.previewers:
            if isinstance(x, str):
                if fnmatch.fnmatch(os.path.basename(filename), x):
                    # we load entrypoint only before it is used. This is to avoid
                    # loading previewers that require additional external modules
                    # we can cache the loaded function but there does not seem to be
                    # a strong performance need for this.
                    previewer_func = y.load()
                    break
            else:
                # it should be a function
                try:
                    if x(filename):
                        try:
                            previewer_func = y.load()
                        except Exception as e:
                            self.send_frontend_msg('stream',
                                                   dict(name='stderr',
                                                        text=f'Failed to load previewer {y}: {e}'),
                                                   title=title, append=True, page='Preview')
                            continue
                        break
                except Exception as e:
                    self.send_frontend_msg('stream', {
                        'name': 'stderr',
                        'text': str(e)},
                        title=title, append=True, page='Preview')
                    continue
        #
        # if no previewer can be found
        if previewer_func is None:
            return
        try:
            result = previewer_func(filename, self, style)
            if not result:
                return
            if isinstance(result, str):
                if result.startswith('HINT: '):
                    result = result.splitlines()
                    hint_line = result[0][6:].strip()
                    result = '\n'.join(result[1:])
                    self.send_frontend_msg('display_data',
                                           {
                                               'metadata': {},
                                               'data': {'text/html': HTML(
                                                   f'<div class="sos_hint">{hint_line}</div>').data}
                                           }, title=title, append=True, page='Preview')
                if result:
                    self.send_frontend_msg('stream',
                                           {'name': 'stdout', 'text': result},
                                           title=title, append=True, page='Preview')
            elif isinstance(result, dict):
                self.send_frontend_msg('display_data',
                                       {'data': result, 'metadata': {}},
                                       title=title, append=True, page='Preview')
            elif isinstance(result, [list, tuple]) and len(result) == 2:
                self.send_frontend_msg('display_data',
                                       {'data': result[0],
                                           'metadata': result[1]},
                                       title=title, append=True, page='Preview')
            else:
                self.send_frontend_msg('stream',
                                       dict(
                                           name='stderr', text=f'Unrecognized preview content: {result}'),
                                       title=title, append=True, page='Preview')
        except Exception as e:
            if self._debug_mode:
                self.send_frontend_msg('stream',
                                       dict(
                                           name='stderr', text=f'Failed to preview {filename}: {e}'),
                                       title=title, append=True, page='Preview')

    def render_result(self, res):
        if not self._meta['render_result']:
            return res
        if not isinstance(res, str):
            self.warn(
                f'Cannot render result {short_repr(res)} in type {res.__class__.__name__} as {self._meta["render_result"]}.')
        else:
            # import the object from IPython.display
            mod = __import__('IPython.display')
            if not hasattr(mod.display, self._meta['render_result']):
                self.warn(
                    f'Unrecognized render format {self._meta["render_result"]}')
            else:
                func = getattr(mod.display, self._meta['render_result'])
                res = func(res)
        return res

    def send_result(self, res, silent=False):
        # this is Ok, send result back
        if not silent and res is not None:
            format_dict, md_dict = self.format_obj(self.render_result(res))
            self.send_response(self.iopub_socket, 'execute_result',
                               {'execution_count': self._execution_count, 'data': format_dict,
                                'metadata': md_dict})

    def init_metadata(self, metadata):
        super(SoS_Kernel, self).init_metadata(metadata)
        if 'sos' in metadata['content']:
            meta = metadata['content']['sos']
        else:
            # if there is no sos metadata, the execution should be started from a test suite
            # just ignore
            self._meta = {
                'workflow': '',
                'workflow_mode': False,
                'render_result': False,
                'capture_result': None,
                'cell_id': 0,
                'notebook_name': '',
                'notebook_path': '',
                'use_panel': False,
                'default_kernel': self.kernel,
                'cell_kernel': self.kernel,
                'resume_execution': False,
                'toc': '',
            }
            return self._meta

        if self._debug_mode:
            self.warn(f"Meta info: {meta}")
        self._meta = {
            'workflow': meta['workflow'] if 'workflow' in meta else '',
            'workflow_mode': False,
            'render_result': False,
            'capture_result': None,
            'cell_id': meta['cell_id'] if 'cell_id' in meta else "",
            'notebook_path': meta['path'] if 'path' in meta else 'Untitled.ipynb',
            'use_panel': True if 'use_panel' in meta and meta['use_panel'] is True else False,
            'default_kernel': meta['default_kernel'] if 'default_kernel' in meta else 'SoS',
            'cell_kernel': meta['cell_kernel'] if 'cell_kernel' in meta else (meta['default_kernel'] if 'default_kernel' in meta else 'SoS'),
            'resume_execution': True if 'rerun' in meta and meta['rerun'] else False,
            'toc': meta.get('toc', ''),
        }
        # remove path and extension
        self._meta['notebook_name'] = os.path.basename(
            self._meta['notebook_path']).rsplit('.', 1)[0]
        if 'list_kernel' in meta and meta['list_kernel']:
            # https://github.com/jupyter/help/issues/153#issuecomment-289026056
            #
            # when the frontend is refreshed, cached comm would be lost and
            # communication would be discontinued. However, a kernel-list
            # request would be sent by the new-connection so we reset the
            # frontend_comm to re-connect to the frontend.
            self.comm_manager.register_target('sos_comm', self.sos_comm)
        return self._meta

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=True):
        if self._debug_mode:
            self.warn(code)
        self._forward_input(allow_stdin)
        # switch to global default kernel
        try:
            if self.subkernels.find(self._meta['default_kernel']).name != self.subkernels.find(self.kernel).name:
                self.switch_kernel(self._meta['default_kernel'])
                # evaluate user expression
        except Exception as e:
            self.warn(
                f'Failed to switch to language {self._meta["default_kernel"]}: {e}\n')
            return {'status': 'error',
                    'ename': e.__class__.__name__,
                    'evalue': str(e),
                    'traceback': [],
                    'execution_count': self._execution_count,
                    }
        # switch to cell kernel
        try:
            if self.subkernels.find(self._meta['cell_kernel']).name != self.subkernels.find(self.kernel).name:
                self.switch_kernel(self._meta['cell_kernel'])
        except Exception as e:
            self.warn(
                f'Failed to switch to language {self._meta["cell_kernel"]}: {e}\n')
            return {'status': 'error',
                    'ename': e.__class__.__name__,
                    'evalue': str(e),
                    'traceback': [],
                    'execution_count': self._execution_count,
                    }
        # execute with cell kernel
        try:
            ret = self._do_execute(code=code, silent=silent, store_history=store_history,
                                   user_expressions=user_expressions, allow_stdin=allow_stdin)
        except Exception as e:
            self.warn(e)
            return {'status': 'error',
                    'ename': e.__class__.__name__,
                    'evalue': str(e),
                    'traceback': [],
                    'execution_count': self._execution_count,
                    }
        finally:
            self._meta['resume_execution'] = False

        if ret is None:
            ret = {'status': 'ok',
                   'payload': [], 'user_expressions': {},
                   'execution_count': self._execution_count}

        out = {}
        for key, expr in (user_expressions or {}).items():
            try:
                # value = self.shell._format_user_obj(SoS_eval(expr))
                value = SoS_eval(expr)
                value = self.shell._format_user_obj(value)
            except Exception as e:
                self.warn(f'Failed to evaluate user expression {expr}: {e}')
                value = self.shell._user_obj_error()
            out[key] = value
        ret['user_expressions'] = out
        #
        if not silent and store_history:
            self._real_execution_count += 1
        self._execution_count = self._real_execution_count
        # make sure post_executed is triggered after the completion of all cell content
        self.shell.user_ns.update(env.sos_dict._dict)
        # trigger post processing of object and display matplotlib figures
        self.shell.events.trigger('post_execute')
        # tell the frontend the kernel for the "next" cell
        return ret

    def _do_execute(self, code, silent, store_history=True, user_expressions=None,
                    allow_stdin=True):
        # handles windows/unix newline
        code = '\n'.join(code.splitlines())

        if self.original_keys is None:
            self._reset_dict()
        if code == 'import os\n_pid = os.getpid()':
            # this is a special probing command from vim-ipython. Let us handle it specially
            # so that vim-python can get the pid.
            return
        if self.MAGIC_SKIP.match(code):
            self.warn('The %skip magic is deprecated and will be removed later.')
            return {'status': 'ok', 'payload': [], 'user_expressions': {}, 'execution_count': self._execution_count}
        elif self.MAGIC_RENDER.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_render_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            try:
                self._meta['capture_result'] = []
                self._meta['render_result'] = args.as_type
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            finally:
                content = ''
                if args.msg_type == 'stdout':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'stream' and msg[1]['name'] == 'stdout':
                            content += msg[1]['text']
                elif args.msg_type == 'text':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'display_data' and 'data' in msg[1] and 'text/plain' in msg[1]['data']:
                            content += msg[1]['data']['text/plain']
                try:
                    if content:
                        format_dict, md_dict = self.format_obj(
                            self.render_result(content))
                        self.send_response(self.iopub_socket, 'display_data',
                                           {'metadata': md_dict,
                                            'data': format_dict
                                            })
                finally:
                    self._meta['capture_result'] = None
                    self._meta['render_result'] = False
        elif self.MAGIC_CAPTURE.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_capture_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            try:
                self._meta['capture_result'] = []
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            finally:
                # parse capture_result
                content = ''
                if args.msg_type == 'stdout':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'stream' and msg[1]['name'] == 'stdout':
                            content += msg[1]['text']
                elif args.msg_type == 'stderr':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'stream' and msg[1]['name'] == 'stderr':
                            content += msg[1]['text']
                elif args.msg_type == 'text':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'display_data' and 'data' in msg[1] and 'text/plain' in msg[1]['data']:
                            content += msg[1]['data']['text/plain']
                elif args.msg_type == 'markdown':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'display_data' and 'data' in msg[1] and 'text/markdown' in msg[1]['data']:
                            content += msg[1]['data']['text/markdown']
                elif args.msg_type == 'html':
                    for msg in self._meta['capture_result']:
                        if msg[0] == 'display_data' and 'data' in msg[1] and 'text/html' in msg[1]['data']:
                            content += msg[1]['data']['text/html']
                else:
                    args.as_type = 'raw'
                    content = self._meta['capture_result']

                if self._debug_mode:
                    self.warn(f'Captured {self._meta["capture_result"][:40]}')
                if not args.as_type or args.as_type == 'text':
                    if not isinstance(content, str):
                        self.warn('Option --as is only available for message types stdout, stderr, and text.')
                elif args.as_type == 'json':
                    import json
                    try:
                        if isinstance(content, str):
                            content = json.loads(content)
                        else:
                            self.warn('Option --as is only available for message types stdout, stderr, and text.')
                    except Exception as e:
                        self.warn(
                            f'Failed to capture output in JSON format, text returned: {e}')
                elif args.as_type == 'csv':
                    try:
                        if isinstance(content, str):
                            with StringIO(content) as ifile:
                                content = pd.read_csv(ifile)
                        else:
                            self.warn('Option --as is only available for message types stdout, stderr, and text.')
                    except Exception as e:
                        self.warn(
                            f'Failed to capture output in {args.as_type} format, text returned: {e}')
                elif args.as_type == 'tsv':
                    try:
                        if isinstance(content, str):
                            with StringIO(content) as ifile:
                                content = pd.read_csv(ifile, sep='\t')
                        else:
                            self.warn('Option --as is only available for message types stdout, stderr, and text.')
                    except Exception as e:
                        self.warn(
                            f'Failed to capture output in {args.as_type} format, text returned: {e}')
                #
                if args.__to__ and not args.__to__.isidentifier():
                    self.warn(f'Invalid variable name {args.__to__}')
                    self._meta['capture_result'] = None
                    return
                if args.__append__ and not args.__append__.isidentifier():
                    self.warn(f'Invalid variable name {args.__append__}')
                    self._meta['capture_result'] = None
                    return

                if args.__to__:
                    env.sos_dict.set(args.__to__, content)
                elif args.__append__:
                    if args.__append__ not in env.sos_dict:
                        env.sos_dict.set(args.__append__, content)
                    elif isinstance(env.sos_dict[args.__append__], str):
                        if isinstance(content, str):
                            env.sos_dict[args.__append__] += content
                        else:
                            self.warn(
                                f'Cannot append new content of type {type(content).__name__} to {args.__append__} of type {type(env.sos_dict[args.__append__]).__name__}')
                    elif isinstance(env.sos_dict[args.__append__], dict):
                        if isinstance(content, dict):
                            env.sos_dict[args.__append__].update(content)
                        else:
                            self.warn(
                                f'Cannot append new content of type {type(content).__name__} to {args.__append__} of type {type(env.sos_dict[args.__append__]).__name__}')
                    elif isinstance(env.sos_dict[args.__append__], pd.DataFrame):
                        if isinstance(content, pd.DataFrame):
                            env.sos_dict.set(
                                args.__append__, env.sos_dict[args.__append__].append(content))
                        else:
                            self.warn(
                                f'Cannot append new content of type {type(content).__name__} to {args.__append__} of type {type(env.sos_dict[args.__append__]).__name__}')
                    elif isinstance(env.sos_dict[args.__append__], list):
                        env.sos_dict[args.__append__].append(content)
                    else:
                        self.warn(
                            f'Cannot append new content of type {type(content).__name__} to {args.__append__} of type {type(env.sos_dict[args.__append__]).__name__}')
                else:
                    env.sos_dict.set('__captured', content)
                    import pprint
                    self.send_frontend_msg('display_data',
                                           {'metadata': {},
                                            'data': {'text/plain': pprint.pformat(content) }
                                           }, title="__captured", append=False, page='Preview')
            self._meta['capture_result'] = None
        elif self.MAGIC_SESSIONINFO.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_sessioninfo_parser()
            try:
                parser.parse_known_args(shlex.split(options))
            except SystemExit:
                return
            self.handle_sessioninfo()
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_TOC.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_toc_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            if args.panel:
                self._meta['use_panel'] = True
            elif args.notebook:
                self._meta['use_panel'] = False
            if self._meta['use_panel']:
                self.send_frontend_msg('show_toc')
            else:
                self.send_response(self.iopub_socket, 'display_data',
                                   {'metadata': {},
                                    'data': {
                                       'text/html': header_to_toc(self._meta['toc'], args.id)
                                   },
                                   })
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_DICT.match(code):
            # %dict should be the last magic
            options, remaining_code = self.get_magic_and_code(code, False)
            self.handle_magic_dict(options)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_CONNECT_INFO.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            cfile = find_connection_file()
            with open(cfile) as conn:
                conn_info = conn.read()
            self.send_response(self.iopub_socket, 'stream',
                               {'name': 'stdout', 'text': 'Connection file: {}\n{}'.format(cfile, conn_info)})
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_MATPLOTLIB.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_matplotlib_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            if args.list:
                self.send_response(self.iopub_socket, 'stream',
                                   {'name': 'stdout', 'text': 'Available matplotlib backends: {}'.format(
                                       ['agg', 'gtk', 'gtk3', 'inline', 'ipympl', 'nbagg', 'notebook',
                                        'osx', 'pdf', 'ps', 'qt', 'qt4', 'qt5', 'svg', 'tk', 'widget', 'wx'])})
                return
            try:
                _, backend = self.shell.enable_matplotlib(args.gui)
                if not args.gui or args.gui == 'auto':
                    self.send_response(self.iopub_socket, 'stream',
                                       {'name': 'stdout',
                                        'text': f'Using matplotlib backend {backend}'})
            except Exception as e:
                self.warn(
                    'Failed to set matplotlib backnd {}: {}'.format(options, e))
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_SET.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            self.handle_magic_set(options)
            # self.options will be set to inflence the execution of remaing_code
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_EXPAND.match(code):
            lines = code.splitlines()
            options = lines[0]
            parser = self.get_expand_parser()
            try:
                args = parser.parse_args(options.split()[1:])
            except SystemExit:
                return
            if self.kernel.lower() == 'sos':
                self.warn('Use of %expand magic in SoS cells is deprecated.')
            if args.sigil in ('None', None):
                sigil = None
            if args.right_sigil is not None:
                sigil = f'{args.sigil} {args.right_sigil}'
            # now we need to expand the text, but separate the SoS magics first
            lines = lines[1:]
            start_line: int = 0
            for idx, line in enumerate(lines):
                if line.strip() and not any(line.startswith(f'%{x} ') for x in self.ALL_MAGICS) and not line.startswith('!'):
                    start_line = idx
                    break
            text = '\n'.join(lines[start_line:])
            if sigil is not None and sigil != '{ }':
                from sos.parser import replace_sigil
                text = replace_sigil(text, sigil)
            try:
                interpolated = interpolate(text, local_dict=env.sos_dict._dict)
                remaining_code = '\n'.join(
                    lines[:start_line] + [interpolated]) + '\n'
                # self.options will be set to inflence the execution of remaing_code
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            except Exception as e:
                self.warn(e)
                return
        elif self.MAGIC_SHUTDOWN.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_shutdown_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            self.shutdown_kernel(
                args.kernel if args.kernel else self.kernel, args.restart)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_CLEAR.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_clear_parser()
            try:
                args = parser.parse_args(options.split())
            except SystemExit:
                return
            # self._meta['cell_id'] could be reset by _do_execute
            cell_id = self._meta['cell_id']
            try:
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            finally:
                if args.status:
                    status_style = [self.status_class[x] for x in args.status]
                else:
                    status_style = None
                self.send_frontend_msg(
                    'clear-output', [cell_id, args.all, status_style, args.elem_class])
        elif self.MAGIC_WITH.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_with_parser()
                try:
                    args = parser.parse_args(shlex.split(options))
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            original_kernel = self.kernel
            try:
                self.switch_kernel(args.name, args.in_vars, args.out_vars)
            except Exception as e:
                self.warn(
                    f'Failed to switch to subkernel {args.name}): {e}')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            try:
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            finally:
                self.switch_kernel(original_kernel)
        elif self.MAGIC_USE.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_use_parser()
                try:
                    args = parser.parse_args(shlex.split(options))
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'abort',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            if args.restart and args.name in self.kernels:
                self.shutdown_kernel(args.name)
                self.warn(f'{args.name} is shutdown')
            try:
                self.switch_kernel(args.name, None, None, args.kernel,
                                   args.language, args.color)
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            except Exception as e:
                self.warn(
                    f'Failed to switch to subkernel {args.name} (kernel {args.kernel}, language {args.language}): {e}')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
        elif self.MAGIC_GET.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_get_parser()
                try:
                    args = parser.parse_args(options.split())
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            self.handle_magic_get(args.vars, args.__from__, explicit=True)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_PUT.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_put_parser()
                try:
                    args = parser.parse_args(options.split())
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            self.handle_magic_put(args.vars, args.__to__, explicit=True)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_PUSH.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_push_parser()
                try:
                    args = parser.parse_args(options.split())
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            self.handle_magic_push(args)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_PULL.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_pull_parser()
                try:
                    args = parser.parse_args(options.split())
                except SystemExit:
                    return
            except Exception as e:
                self.warn(f'Invalid option "{options}": {e}\n')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            self.handle_magic_pull(args)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_PASTE.match(code):
            options, remaining_code = self.get_magic_and_code(code, True)
            try:
                old_options = self.options
                self.options = options + ' ' + self.options
                try:
                    code = clipboard_get()
                except ClipboardEmpty:
                    raise UsageError("The clipboard appears to be empty")
                except Exception as e:
                    env.logger.warn(
                        f'Failed to get text from the clipboard: {e}')
                    return
                #
                self.send_response(self.iopub_socket, 'stream',
                                   {'name': 'stdout', 'text': code.strip() + '\n## -- End pasted text --\n'})
                return self._do_execute(code, silent, store_history, user_expressions, allow_stdin)
            finally:
                self.options = old_options
        elif self.MAGIC_RUN.match(code):
            # there can be multiple %run magic, but there should not be any other magics
            run_code = code
            run_options = []
            while True:
                if self.MAGIC_RUN.match(run_code):
                    options, run_code = self.get_magic_and_code(
                        run_code, False)
                    run_options.append(options)
                else:
                    break
            # if there are more magics after %run, they will be ignored so a warning
            # is needed.
            if run_code.lstrip().startswith('%') and not any(run_code.lstrip().startswith(x) for x in ('%include', '%from')):
                self.warn(
                    f'Magic {run_code.split()[0]} after magic %run will be ignored.')

            if not any(SOS_SECTION_HEADER.match(line) for line in run_code.splitlines()):
                run_code = '[default]\n' + run_code
            # now we need to run the code multiple times with each option
            for options in run_options:
                old_options = self.options
                self.options = options + ' ' + self.options
                try:
                    # %run is executed in its own namespace
                    old_dict = env.sos_dict
                    self._reset_dict()
                    self._meta['workflow_mode'] = True
                    if self._debug_mode:
                        self.warn(f'Executing\n{global_sections + run_code}')
                    ret = self._do_execute(run_code, silent, store_history, user_expressions,
                                           allow_stdin)
                except Exception as e:
                    self.warn(f'Failed to execute workflow: {e}')
                    raise
                finally:
                    old_dict.quick_update(env.sos_dict._dict)
                    env.sos_dict = old_dict
                    self._meta['workflow_mode'] = False
                    self.options = old_options
            return ret
        elif self.MAGIC_SOSRUN.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            old_options = self.options
            self.options = options + ' ' + self.options
            try:
                # %run is executed in its own namespace
                old_dict = env.sos_dict
                self._reset_dict()
                self._meta['workflow_mode'] = True
                # self.send_frontend_msg('preview-workflow', self._meta['workflow'])
                if not self._meta['workflow']:
                    self.warn(
                        'Nothing to execute (notebook workflow is empty).')
                else:
                    self._do_execute(self._meta['workflow'], silent,
                                     store_history, user_expressions, allow_stdin)
            except Exception as e:
                self.warn(f'Failed to execute workflow: {e}')
                raise
            finally:
                old_dict.quick_update(env.sos_dict._dict)
                env.sos_dict = old_dict
                self._meta['workflow_mode'] = False
                self.options = old_options
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_SAVE.match(code):
            # if sos kernel ...
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_save_parser()
                try:
                    args = parser.parse_args(shlex.split(options))
                except SystemExit:
                    return
                filename = os.path.expanduser(args.filename)
                if os.path.isfile(filename) and not args.force:
                    raise ValueError(
                        f'Cannot overwrite existing output file {filename}')

                with open(filename, 'a' if args.append else 'w') as script:
                    script.write(
                        '\n'.join(remaining_code.splitlines()).rstrip() + '\n')
                if args.setx:
                    import stat
                    os.chmod(filename, os.stat(
                        filename).st_mode | stat.S_IEXEC)

                self.send_response(self.iopub_socket, 'display_data',
                                   {'metadata': {},
                                    'data': {
                                        'text/plain': f'Cell content saved to {filename}\n',
                                        'text/html': HTML(
                                            f'<div class="sos_hint">Cell content saved to <a href="{filename}" target="_blank">{filename}</a></div>').data
                                   }
                                   })
                return
            except Exception as e:
                self.warn(f'Failed to save cell: {e}')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
        elif self.MAGIC_SOSSAVE.match(code):
            # get the saved filename
            options, remaining_code = self.get_magic_and_code(code, False)
            try:
                parser = self.get_sossave_parser()
                try:
                    args = parser.parse_args(shlex.split(options))
                except SystemExit:
                    return
                if args.filename:
                    filename = args.filename
                    if filename.lower().endswith('.html'):
                        if args.__to__ is None:
                            ftype = 'html'
                        elif args.__to__ != 'html':
                            self.warn(
                                f'%sossave to an .html file in {args.__to__} format')
                            ftype = args.__to__
                    else:
                        ftype = 'sos'
                else:
                    ftype = args.__to__ if args.__to__ else 'sos'
                    filename = self._meta['notebook_name'] + '.' + ftype

                filename = os.path.expanduser(filename)

                if os.path.isfile(filename) and not args.force:
                    raise ValueError(
                        f'Cannot overwrite existing output file {filename}')
                # self.send_frontend_msg('preview-workflow', self._meta['workflow'])
                if ftype == 'sos':
                    if not args.all:
                        with open(filename, 'w') as script:
                            script.write(self._meta['workflow'])
                    else:
                        # convert to sos report
                        from .converter import notebook_to_script
                        arg = argparse.Namespace()
                        arg.all = True
                        notebook_to_script(
                            self._meta['notebook_name'] + '.ipynb', filename, args=arg, unknown_args=[])
                    if args.setx:
                        import stat
                        os.chmod(filename, os.stat(
                            filename).st_mode | stat.S_IEXEC)
                else:
                    # convert to sos report
                    from .converter import notebook_to_html
                    arg = argparse.Namespace()
                    if args.template == 'default-sos-template':
                        from sos.utils import load_config_files
                        cfg = load_config_files()
                        if 'default-sos-template' in cfg:
                            arg.template = cfg['default-sos-template']
                        else:
                            arg.template = 'sos-report'
                    else:
                        arg.template = args.template
                    arg.view = False
                    notebook_to_html(self._meta['notebook_name'] + '.ipynb',
                                     filename, sargs=arg, unknown_args=[])

                self.send_response(self.iopub_socket, 'display_data',
                                   {'metadata': {},
                                    'data': {
                                        'text/plain': f'Workflow saved to {filename}\n',
                                        'text/html': HTML(
                                            f'<div class="sos_hint">Workflow saved to <a href="{filename}" target="_blank">{filename}</a></div>').data
                                   }
                                   })
                #
                if args.commit:
                    self.handle_shell_command({'git', 'commit', filename, '-m',
                                               args.message if args.message else f'save {filename}'})
                if args.push:
                    self.handle_shell_command(['git', 'push'])
                return
            except Exception as e:
                self.warn(f'Failed to save workflow: {e}')
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
        elif self.MAGIC_RERUN.match(code):
            options, remaining_code = self.get_magic_and_code(code, True)
            old_options = self.options
            self.options = options + ' ' + self.options
            try:
                self._meta['workflow_mode'] = True
                old_dict = env.sos_dict
                self._reset_dict()
                if not self.last_executed_code:
                    self.warn('No saved script')
                    self.last_executed_code = ''
                return self._do_execute(self.last_executed_code, silent, store_history, user_expressions, allow_stdin)
            except Exception as e:
                self.warn(f'Failed to execute workflow: {e}')
                raise
            finally:
                old_dict.quick_update(env.sos_dict._dict)
                env.sos_dict = old_dict
                self._meta['workflow_mode'] = False
                self.options = old_options
        elif self.MAGIC_REVISIONS.match(code):
            options, remaining_code = self.get_magic_and_code(code, True)
            parser = self.get_revisions_parser()
            try:
                args, unknown_args = parser.parse_known_args(
                    shlex.split(options))
            except SystemExit:
                return
            try:
                self.handle_magic_revisions(args, unknown_args)
            except Exception as e:
                self.warn(f'Failed to retrieve revisions of notebook: {e}')
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_SANDBOX.match(code):
            import tempfile
            import shutil
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_sandbox_parser()
            try:
                args = parser.parse_args(shlex.split(options))
            except SystemExit:
                return
            self.in_sandbox = True
            try:
                old_dir = os.getcwd()
                if args.dir:
                    args.dir = os.path.expanduser(args.dir)
                    if not os.path.isdir(args.dir):
                        os.makedirs(args.dir)
                    env.exec_dir = os.path.abspath(args.dir)
                    os.chdir(args.dir)
                else:
                    new_dir = tempfile.mkdtemp()
                    env.exec_dir = os.path.abspath(new_dir)
                    os.chdir(new_dir)
                if not args.keep_dict:
                    old_dict = env.sos_dict
                    self._reset_dict()
                ret = self._do_execute(
                    remaining_code, silent, store_history, user_expressions, allow_stdin)
                if args.expect_error and ret['status'] == 'error':
                    # self.warn('\nSandbox execution failed.')
                    return {'status': 'ok',
                            'payload': [], 'user_expressions': {},
                            'execution_count': self._execution_count}
                else:
                    return ret
            finally:
                if not args.keep_dict:
                    env.sos_dict = old_dict
                os.chdir(old_dir)
                if not args.dir:
                    shutil.rmtree(new_dir)
                self.in_sandbox = False
                # env.exec_dir = old_dir
        elif self.MAGIC_PREVIEW.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_preview_parser()
            options = shlex.split(options, posix=False)
            help_option = []
            if ('-s' in options or '--style' in options) and '-h' in options:
                # defer -h to subparser
                options.remove('-h')
                help_option = ['-h']
            try:
                args, style_options = parser.parse_known_args(options)
            except SystemExit:
                return
            #
            style_options.extend(help_option)
            style = {'style': args.style, 'options': style_options}
            #
            if args.off:
                self.preview_output = False
            else:
                self.preview_output = True
            #
            if args.panel:
                self._meta['use_panel'] = True
            elif args.notebook:
                self._meta['use_panel'] = False
            # else, use default _use_panel
            try:
                return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
            finally:
                # preview workflow
                if args.workflow:
                    import random
                    ta_id = 'preview_wf_{}'.format(random.randint(1, 1000000))
                    content = {
                        'data': {
                            'text/plain': self._meta['workflow'],
                            'text/html': HTML(
                                f'<textarea id="{ta_id}">{self._meta["workflow"]}</textarea>').data
                        },
                        'metadata': {}
                    }
                    self.send_frontend_msg('display_data', content,
                                           title='%preview --workflow', page='Workflow')
                    self.send_frontend_msg('highlight-workflow', ta_id)
                if not args.off and args.items:
                    if args.host:
                        title = f'%preview {" ".join(args.items)} -r {args.host}'
                    else:
                        title = f'%preview {" ".join(args.items)}'
                    # reset preview panel
                    if not self._meta['use_panel']:
                        self.send_response(self.iopub_socket, 'display_data',
                                           {
                                               'metadata': {},
                                               'data': {'text/html': HTML(f'<div class="sos_hint">{title}</div>').data}
                                           })
                    else:
                        # clear the page
                        self.send_frontend_msg(
                            'display_data', {}, page='Preview')
                    if args.host is None:
                        self.handle_magic_preview(
                            args.items, args.kernel, style,
                            title=title)
                    elif args.workflow:
                        self.warn('Invalid option --kernel with -r (--host)')
                    elif args.kernel:
                        self.warn('Invalid option --kernel with -r (--host)')
                    else:
                        if args.config:
                            from sos.utils import load_config_files
                            load_config_files(args.config)
                        try:
                            rargs = ['sos', 'preview', '--html'] + options
                            rargs = [x for x in rargs if x not in (
                                '-n', '--notebook', '-p', '--panel')]
                            if self._debug_mode:
                                self.warn(f'Running "{" ".join(rargs)}"')
                            for msg in eval(subprocess.check_output(rargs)):
                                self.send_frontend_msg(
                                    msg[0], msg[1], title=title, append=True, page='Preview')
                        except Exception as e:
                            self.warn('Failed to preview {} on remote host {}{}'.format(
                                args.items, args.host, f': {e}' if self._debug_mode else ''))
        elif self.MAGIC_CD.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            self.handle_magic_cd(options)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_DEBUG.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_debug_parser()
            try:
                args = parser.parse_args(options.split())
            except SystemExit:
                return
            self._debug_mode = args.status == 'on'
            if self._debug_mode:
                self.warn(remaining_code)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_TASKINFO.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_taskinfo_parser()
            try:
                args = parser.parse_args(options.split())
            except SystemExit:
                return
            if args.config:
                from sos.utils import load_cfg_files
                load_cfg_files(args.config)
            self.handle_taskinfo(args.task, args.queue)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.MAGIC_TASKS.match(code):
            options, remaining_code = self.get_magic_and_code(code, False)
            parser = self.get_tasks_parser()
            try:
                args = parser.parse_args(options.split())
            except SystemExit:
                return
            if args.config:
                from sos.utils import load_cfg_files
                load_cfg_files(args.config)
            self.handle_tasks(
                args.tasks, args.queue if args.queue else 'localhost', args.status, args.age)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif code.startswith('!'):
            options, remaining_code = self.get_magic_and_code(code, False)
            self.handle_shell_command(code.split(' ')[0][1:] + ' ' + options)
            return self._do_execute(remaining_code, silent, store_history, user_expressions, allow_stdin)
        elif self.kernel != 'SoS':
            # handle string interpolation before sending to the underlying kernel
            if code:
                self.last_executed_code = code
            # code = self._interpolate_text(code, quiet=False)
            if self._meta['cell_id']:
                self.send_frontend_msg(
                    'cell-kernel', [self._meta['cell_id'], self.kernel])
                self._meta['cell_id'] = ""
            if code is None:
                return
            try:
                # We remove leading new line in case that users have a SoS
                # magic and a cell magic, separated by newline.
                # issue #58 and #33
                return self.run_cell(code.lstrip(), silent, store_history)
            except KeyboardInterrupt:
                self.warn('Keyboard Interrupt\n')
                self.KM.interrupt_kernel()
                return {'status': 'abort', 'execution_count': self._execution_count}
        else:
            if code:
                self.last_executed_code = code

            # if the cell starts with comment, and newline, remove it
            lines = code.splitlines()
            empties = [x.startswith('#') or not x.strip() for x in lines]
            self.send_frontend_msg(
                'cell-kernel', [self._meta['cell_id'], 'SoS'])
            if all(empties):
                return {'status': 'ok', 'payload': [], 'user_expressions': {}, 'execution_count': self._execution_count}
            else:
                idx = empties.index(False)
                if idx != 0:
                    # not start from empty, but might have magic etc
                    return self._do_execute('\n'.join(lines[idx:]), silent, store_history, user_expressions, allow_stdin)

            # if there is no more empty, magic etc, enter workflow mode
            # run sos
            try:
                self.run_sos_code(code, silent)
                if self._meta['cell_id']:
                    self._meta['cell_id'] = ""
                return {'status': 'ok', 'payload': [], 'user_expressions': {}, 'execution_count': self._execution_count}
            except Exception as e:
                self.warn(str(e))
                return {'status': 'error',
                        'ename': e.__class__.__name__,
                        'evalue': str(e),
                        'traceback': [],
                        'execution_count': self._execution_count,
                        }
            finally:
                # even if something goes wrong, we clear output so that the "preview"
                # will not be viewed by a later step.
                env.sos_dict.pop('input', None)
                env.sos_dict.pop('output', None)

    def do_shutdown(self, restart):
        #
        for name, (km, _) in self.kernels.items():
            try:
                km.shutdown_kernel(restart=restart)
            except Exception as e:
                self.warn(f'Failed to shutdown kernel {name}: {e}')

    def __del__(self):
        # upon releasing of sos kernel, kill all subkernels. This I thought would be
        # called by the Jupyter cleanup code or the OS (because subkernels are subprocesses)
        # but they are not.
        self.do_shutdown(False)


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp

    IPKernelApp.launch_instance(kernel_class=SoS_Kernel)
