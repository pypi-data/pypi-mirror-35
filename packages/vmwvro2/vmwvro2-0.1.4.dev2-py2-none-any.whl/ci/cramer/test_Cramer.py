#!/usr/bin/env python
import unittest
from parameterized import parameterized


from vmwvro2.workflow import Workflow, MultiRun
from vmwvro2.sessions import SessionList


sl = SessionList()
sl.load()
vro = ['dev-de', 'dev-ie', 'dev-it']

class IPSubnetExist(unittest.TestCase):

    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
        """
        WF: "Cramer, Does IPSubnet Exist?"
        """

        wf = Workflow()
        wf.id = "e6458f98-e092-4f18-98b6-abb2d79d362a"
        wf.name = "Cramer, Does IPSubnet Exist?"

        wf.param(name="ipSubnetName",value="*")
        wf.param(name="ipRangeName",value="10.105.0.0/16")
        wf.param(name="spaceName",value="*")

        cls.mt.add(wf,sl,"dev")
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
        
        self.assertTrue(out.get('statusCode'))



class GetInfoForAnIP(unittest.TestCase):


    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
        """
        WF: "Cramer, Get info for an IP"
        """
        
        wf = Workflow()
        wf.id = "2294b1f0-46de-47dc-b740-f17d5d857502"
        wf.name = "Cramer, Get info for an IP"

        wf.param(name="ipAddress",value="10.10.10.10")
        wf.param(name="ipSubnetName",value="*")
        wf.param(name="ipRangeName",value="*")
        wf.param(name="spaceName",value="*")

        cls.mt.add(wf,sl,"dev")
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

        
class UpdateAnIPManualy(unittest.TestCase):

    mt = MultiRun()

    @classmethod
    def setUpClass(cls):
        """
        WF: "Cramer, update an IP Manualy"
        """
        
        wf = Workflow()
        wf.id = "338beefa-9f7f-469b-89d4-914031ffbfb6"
        wf.name = "Cramer, update an IP Manualy"

        wf.param(name="ipAddress", value="10.10.10.10")
        wf.param(name="newStatus", value="In Service")
        wf.param(name="description", value="TestingCramer")
        wf.param(name="mailAddressList", value="")

        cls.mt.add(wf,sl,"dev")
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
    def test_logs(self,alias):
        
        try:
            wfExe = self.mt.list[alias]
        except:
            raise unittest.SkipTest("Not performed")
        #out = wfExe.output_parameters
        
        self.assertRegexpMatches(wfExe.log, "Duplicated", "No detected duplicated IP for 10.10.10.10")	

        
        
            
if __name__ == '__main__':
    #unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
    unittest.main()

