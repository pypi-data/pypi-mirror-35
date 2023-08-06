#!/usr/bin/env python
import unittest
from parameterized import parameterized


from vmwvro2.workflow import Workflow, MultiRun
from vmwvro2.sessions import SessionList


sl = SessionList()
sl.load()
vro = ['dev-de', 'dev-ie', 'dev-it']

class NetworkOverlapCheck_Negative(unittest.TestCase):

    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
 
        wf = Workflow()
        wf.id = "c31ba9ad-75b8-4cd2-bbd9-7d6f934c40b0"
        wf.name = "Network overlap check"

        wf.param(name="ip",value="11.10.10.0/24")

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
        
        
        self.assertEqual(out.get('overlap').value, 0.0)


    @parameterized.expand(vro)
    def test_logs(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")
        #out = wfExe.output_parameters
        
        self.assertRegexpMatches(wfExe.log, "NSX Query size", "No NSX info")
        self.assertRegexpMatches(wfExe.log, "Cramer, IP:., number of entries for this IP:", "No Cramer info");
        self.assertRegexpMatches(wfExe.log, "NetworkDB, Pool query size: .* pools", "No pools from networkDB")
        self.assertRegexpMatches(wfExe.log, "NetworkDB, Subnet query size: .* subnets", "No subnetes from networkDB")
       
        

class NetworkOverlapCheck_Positive(unittest.TestCase):

    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
 
        wf = Workflow()
        wf.id = "c31ba9ad-75b8-4cd2-bbd9-7d6f934c40b0"
        wf.name = "Network overlap check"

        wf.param(name="ip",value="10.10.10.0/24")

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
        self.assertEqual(wfExe.state, "failed")

        

    @parameterized.expand(vro)
    def test_logs(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")
        #out = wfExe.output_parameters
        
        self.assertRegexpMatches(wfExe.log, "NSX Query size", "No NSX info")
        self.assertRegexpMatches(wfExe.log, "Cramer, IP:., number of entries for this IP:", "No Cramer info");
        self.assertRegexpMatches(wfExe.log, "NetworkDB, Pool query size: .* pools", "No pools from networkDB")
        self.assertRegexpMatches(wfExe.log, "NetworkDB, Subnet query size: .* subnets", "No subnetes from networkDB")
       


        
if __name__ == '__main__':
    #unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
    unittest.main()

