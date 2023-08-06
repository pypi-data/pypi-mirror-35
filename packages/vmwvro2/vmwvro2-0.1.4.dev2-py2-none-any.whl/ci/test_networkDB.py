#!/usr/bin/env python
import unittest
from parameterized import parameterized


from vmwvro2.workflow import Workflow, MultiRun
from vmwvro2.sessions import SessionList


sl = SessionList()
sl.load()
vro = ['dev-de', 'dev-ie', 'dev-it']

class NetworkDB(unittest.TestCase):

    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
        """
        WF: test_getNetworksNetworkdb
        """
        
        wf = Workflow()
        wf.id = "bb5e3ffd-f727-4eec-83e0-a99faf3e60eb"
        wf.name = "test_getNetworksNetworkdb"

        wf.param(name="dc",value="DublinDEV")
        wf.param(name="tenant",value="VF United Kingdom")
        wf.param(name="az",value="AZ1")

        cls.mt.add(wf,sl,"dev-de")
        cls.mt.run()
        cls.mt.wait()
        cls.mt.getLogs()
        
        for alias in cls.mt.list:
            cls.mt.list[alias].print_workflow()


    @parameterized.expand(vro)
    def test_state(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")

        self.assertEqual(wfExe.state, "completed")
        
        
        
    @parameterized.expand(vro)
    def test_output(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")

        out = wfExe.output_parameters

        self.assertGreater(out.get('items').value, 0)	

        
    @parameterized.expand(vro)
    def test_logs(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")

        self.assertRegexpMatches(wfExe.log, "Connection to Network db successful")	

        
        
            
if __name__ == '__main__':
    #unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
    unittest.main()

