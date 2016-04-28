from django.test import TestCase
import pytest
import sys

class Test_PytestFixtureStyle(TestCase):
    @pytest.fixture(autouse=True)
    def scope_default(self, request):
        print('fixture style - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_default():
            print('fixture style - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_default)
        
        
    @pytest.fixture(autouse=True, scope='function')
    def scope_function(self, request):
        print('fixture style - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_function():
            print('fixture style - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_function)
        
        
    @pytest.fixture(autouse=True, scope='class')
    def scope_class(self, request):
        print('fixture style - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_class():
            print('fixture style - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_class)
        
        
    @pytest.fixture(autouse=True, scope='module')
    def scope_module(self, request):
        print('fixture style - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_module():
            print('fixture style - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_module)
        
        
    @pytest.fixture(autouse=True, scope='session')
    def scope_session(self, request):
        print('fixture style - setup > {}'.format(sys._getframe().f_code.co_name))
        
        def fin_scope_session():
            print('fixture style - teardown > {}'.format(sys._getframe().f_code.co_name))
        request.addfinalizer(fin_scope_session)
        
        
    # test method
    def testSpam(self):
        print('fixture style - setup > [{}]'.format(sys._getframe().f_code.co_name))
        assert True

    def testHam(self):
        print('fixture style - setup > [{}]'.format(sys._getframe().f_code.co_name))
        assert True