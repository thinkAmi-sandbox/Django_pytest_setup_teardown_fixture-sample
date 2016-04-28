from django.test import TestCase
import sys

class Test_UnittestStyle(TestCase):
    @classmethod
    def setUpClass(cls):
        # http://qiita.com/megmogmog1965/items/0b4ea3d58e34f1854158
        print('unittest style - setup > {}'.format(sys._getframe().f_code.co_name))
        
    @classmethod
    def tearDownClass(cls):
        print('unittest style - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    def setUp(self):
        print('unittest style - setup > {}'.format(sys._getframe().f_code.co_name))
    
    def tearDown(self):
        print('unittest style - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    
    # test method
    def testSpam(self):
        print('unittest style - setup > [{}]'.format(sys._getframe().f_code.co_name))
        assert True

    def testHam(self):
        print('unittest style - setup > [{}]'.format(sys._getframe().f_code.co_name))
        assert True