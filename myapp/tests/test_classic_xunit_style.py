from django.test import TestCase
import sys

def setup_module(module):
    print('classic xunit style - setup > {}'.format(sys._getframe().f_code.co_name))
    
def teardown_module(module):
    print('classic xunit style - teardown > {}'.format(sys._getframe().f_code.co_name))

def setup_function(function):
    print('classic xunit style - setup > {}'.format(sys._getframe().f_code.co_name))
    
def teardown_function(function):
    print('classic xunit style - teardown > {}'.format(sys._getframe().f_code.co_name))


class Test_ClassicXunitStyle(TestCase):        
    @classmethod
    def setup_class(cls):
        print('classic xunit style - setup > {}'.format(sys._getframe().f_code.co_name))
        
    @classmethod
    def teardown_class(cls):
        print('classic xunit style - teardown > {}'.format(sys._getframe().f_code.co_name))
        
    def setup_method(self, method):
        print('classic xunit style - setup > {}'.format(sys._getframe().f_code.co_name))
        
    def teardown_method(self, method):
        print('classic xunit style - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    
    # test method
    def testSpam(self):
        print('classic xunit style > [{}]'.format(sys._getframe().f_code.co_name))
        assert True

    def testHam(self):
        print('classic xunit style > [{}]'.format(sys._getframe().f_code.co_name))
        assert True