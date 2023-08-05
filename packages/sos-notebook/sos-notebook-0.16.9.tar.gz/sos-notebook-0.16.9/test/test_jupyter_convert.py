#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import os
import shutil
import subprocess
import unittest

from sos.utils import env
from sos_notebook.converter import notebook_to_script, script_to_notebook


class TestConvert(unittest.TestCase):
    def setUp(self):
        env.reset()
        self.olddir = os.getcwd()
        file_dir = os.path.split(__file__)[0]
        if file_dir:
            os.chdir(file_dir)
        if not os.path.isdir('temp'):
            os.mkdir('temp')
        with open('temp/script1.sos', 'w') as script:
            script.write('''
[0]
seq = range(3)
input: for_each='seq'
output: 'test${_seq}.txt'
print(output)
''')
        with open('temp/script2.sos', 'w') as script:
            # with tab after run:
            script.write('''
#! This is supposed to be a markdown
#! cell

[0]
seq = range(3)
input: for_each='seq'
output: 'test${_seq}.txt'
run:			concurrent=True
    echo 'this is test script'
[10]
report('this is action report')
''')
        self.scripts = ['temp/script1.sos', 'temp/script2.sos']

    def tearDown(self):
        shutil.rmtree('temp')
        os.chdir(self.olddir)

    def testScriptToAndFromNotebook(self):
        '''Test sos show script --notebook'''
        for script_file in self.scripts:
            script_to_notebook(script_file, script_file[:-4] + '.ipynb')
            notebook_to_script(script_file[:-4] + '.ipynb', script_file)

    def testConvertAll(self):
        subprocess.call('sos convert test.ipynb test_wf.sos --all', shell=True)
        self.assertTrue(os.path.isfile('test_wf.sos'))
        subprocess.call('sos convert test_wf.sos test2.ipynb', shell=True)
        self.assertTrue(os.path.isfile('test2.ipynb'))
        # --execute does not yet work
        os.remove('test_wf.sos')
        os.remove('test2.ipynb')

    def testConvertHTML(self):
        subprocess.call('sos convert test.ipynb test_wf.html', shell=True)
        self.assertTrue(os.path.isfile('test_wf.html'))
        # test the use of jupyter templates
        subprocess.call('sos convert test.ipynb test_wf1.html --template basic', shell=True)
        self.assertTrue(os.path.isfile('test_wf1.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf2.html --template sos-report', shell=True)
        self.assertTrue(os.path.isfile('test_wf2.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf3.html --template sos-full', shell=True)
        self.assertTrue(os.path.isfile('test_wf3.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf4.html --template sos-cm', shell=True)
        self.assertTrue(os.path.isfile('test_wf4.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf5.html --template sos-full-toc', shell=True)
        self.assertTrue(os.path.isfile('test_wf5.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf6.html --template sos-report-toc', shell=True)
        self.assertTrue(os.path.isfile('test_wf6.html'))
        #
        subprocess.call('sos convert test.ipynb test_wf7.html --template sos-cm-toc', shell=True)
        self.assertTrue(os.path.isfile('test_wf7.html'))

    @unittest.skipIf(not shutil.which('xelatex'), 'No XeLatex under windows to compile pdf')
    def testConvertPDF(self):
        subprocess.call('sos convert test.ipynb test_wf.pdf', shell=True)
        self.assertTrue(os.path.isfile('test_wf.pdf'))

    def testConvertMD(self):
        subprocess.call('sos convert test.ipynb test_wf.md', shell=True)
        self.assertTrue(os.path.isfile('test_wf.md'))
        # output to stdout
        subprocess.call('sos convert test.ipynb --to md > test_wf1.md', shell=True)
        self.assertTrue(os.path.isfile('test_wf1.md'))

    def testComments(self):
        '''Test if comments before section headers are correctly extracted'''
        subprocess.call('sos convert sample_workflow.ipynb sample_workflow.sos', shell=True)
        with open('sample_workflow.sos') as sw:
            wf = sw.read()
        self.assertFalse('this is a test workflow' in wf)
        self.assertEqual(wf.count('this comment will be included but not shown in help'), 1)
        self.assertTrue(wf.count('this comment will become the comment for parameter b'), 1)
        self.assertTrue(wf.count('this comment will become the comment for parameter d'), 1)
        self.assertFalse('this is a cell with another kernel' in wf)
        self.assertFalse('this comment will not be included in exported workflow' in wf)

if __name__ == '__main__':
    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestConvert)
    # unittest.TextTestRunner().run(suite)
    unittest.main()
