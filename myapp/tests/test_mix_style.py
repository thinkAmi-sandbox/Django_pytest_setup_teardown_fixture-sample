from django.test import TestCase
import sys
import pytest

class Test_MixStyle(TestCase):
    # unittest style
    @classmethod
    def setUpClass(cls):
        print('mix style (unittest) - setup > {}'.format(sys._getframe().f_code.co_name))
        
    @classmethod
    def tearDownClass(cls):
        print('mix style (unittest) - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    def setUp(self):
        print('mix style (unittest) - setup > {}'.format(sys._getframe().f_code.co_name))
    
    def tearDown(self):
        print('mix style (unittest) - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    # classic xunit style
    @classmethod
    def setup_class(cls):
        print('mix style (classic xunit) - setup > {}'.format(sys._getframe().f_code.co_name))
        
    @classmethod
    def teardown_class(cls):
        print('mix style (classic xunit) - teardown > {}'.format(sys._getframe().f_code.co_name))
        
    def setup_method(self, method):
        print('mix style (classic xunit) - setup > {}'.format(sys._getframe().f_code.co_name))
        
    def teardown_method(self, method):
        print('mix style (classic xunit) - teardown > {}'.format(sys._getframe().f_code.co_name))
    
    
    # fixture style
    @pytest.fixture(autouse=True)
    def scope_default(self, request):
        print('mix style (fixture) - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_default():
            print('mix style (fixture) - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_default)
        
        
    @pytest.fixture(autouse=True, scope='function')
    def scope_function(self, request):
        print('mix style (fixture) - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_function():
            print('mix style (fixture) - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_function)
        
        
    @pytest.fixture(autouse=True, scope='class')
    def scope_class(self, request):
        print('mix style (fixture) - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_class():
            print('mix style (fixture) - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_class)
        
        
    @pytest.fixture(autouse=True, scope='module')
    def scope_module(self, request):
        print('mix style (fixture) - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_module():
            print('mix style (fixture) - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_module)
        
        
    @pytest.fixture(autouse=True, scope='session')
    def scope_session(self, request):
        print('mix style (fixture) - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_session():
            print('mix style (fixture) - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_session)
    
    
    # test method
    def testSpam(self):
        print('mix style > [{}]'.format(sys._getframe().f_code.co_name))
        assert True

    def testHam(self):
        print('mix style > [{}]'.format(sys._getframe().f_code.co_name))
        assert True