# Django_pytest_setup_teardown_fixture-sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_pytest_setup_teardown_fixture-sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# 実行
(env)path\to\dir>py.test
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.5
- pytest 2.9.1
- pytest-django 2.9.1
- factory-boy 2.7.0

　  
## 実行結果
見やすくするため、一部改行しています。

### django.test.TestCaseスタイルで書いた場合

```
(env)path\to\dir>py.test myapp/tests/test_unittest_style.py -s
...
myapp\tests\test_unittest_style.py
unittest style - setup > setUpClass
unittest style - setup > setUp
unittest style - setup > [testHam]
unittest style - teardown > tearDown
.
unittest style - setup > setUp
unittest style - setup > [testSpam]
unittest style - teardown > tearDown
.
unittest style - teardown > tearDownClass
```

　  
### pytestのxunitスタイルで書いた場合

```
(env)path\to\dir>py.test myapp/tests/test_classic_xunit_style.py -s
...
myapp\tests\test_classic_xunit_style.py
classic xunit style - setup > setup_module
classic xunit style - setup > setup_class
classic xunit style - setup > setup_method
classic xunit style > [testHam]
.
classic xunit style - teardown > teardown_method
classic xunit style - setup > setup_method
classic xunit style > [testSpam]
.
classic xunit style - teardown > teardown_method
classic xunit style - teardown > teardown_class
classic xunit style - teardown > teardown_module
```

　  
### pytestのfixtureスタイルで書いた場合

```
(env)path\to\dir>py.test myapp/tests/test_fixture_style.py -s
...
myapp\tests\test_fixture_style.py
fixture style - setup > scope_session
fixture style - setup > scope_module
fixture style - setup > scope_class
fixture style - setup > scope_default
fixture style - setup > scope_function
fixture style - setup > [testHam]
.
fixture style - teardown > fin_scope_function
fixture style - teardown > fin_scope_default
fixture style - setup > scope_default
fixture style - setup > scope_function
fixture style - setup > [testSpam]
.
fixture style - teardown > fin_scope_function
fixture style - teardown > fin_scope_default
fixture style - teardown > fin_scope_class
fixture style - teardown > fin_scope_module
fixture style - teardown > fin_scope_session
```

　  
### 上記3つのスタイルを、1つのクラスに書いた場合

```
(env)path\to\dir>py.test myapp/tests/test_mix_style.py -s
...
myapp\tests\test_mix_style.py
mix style (classic xunit) - setup > setup_class
mix style (classic xunit) - setup > setup_method
mix style (fixture) - setup > scope_session
mix style (fixture) - setup > scope_module
mix style (unittest) - setup > setUpClass
mix style (fixture) - setup > scope_class
mix style (fixture) - setup > scope_default
mix style (fixture) - setup > scope_function
mix style (unittest) - setup > setUp
mix style > [testHam]
mix style (unittest) - teardown > tearDown
.
mix style (fixture) - teardown > fin_scope_function
mix style (fixture) - teardown > fin_scope_default
mix style (classic xunit) - teardown > teardown_method
mix style (classic xunit) - setup > setup_method
mix style (fixture) - setup > scope_default
mix style (fixture) - setup > scope_function
mix style (unittest) - setup > setUp
mix style > [testSpam]
mix style (unittest) - teardown > tearDown
.
mix style (fixture) - teardown > fin_scope_function
mix style (fixture) - teardown > fin_scope_default
mix style (classic xunit) - teardown > teardown_method
mix style (fixture) - teardown > fin_scope_class
mix style (unittest) - teardown > tearDownClass
mix style (classic xunit) - teardown > teardown_class
mix style (fixture) - teardown > fin_scope_module
mix style (fixture) - teardown > fin_scope_session
```

　  
### 全部のテストを一度に流した場合

```
(env)path\to\dir>py.test -s
...
myapp\tests\test_classic_xunit_style.py classic xunit style - setup > setup_module
classic xunit style - setup > setup_class
classic xunit style - setup > setup_method
classic xunit style > [testHam]
.
classic xunit style - teardown > teardown_method
classic xunit style - setup > setup_method
classic xunit style > [testSpam]
.
classic xunit style - teardown > teardown_method
classic xunit style - teardown > teardown_class
classic xunit style - teardown > teardown_module

myapp\tests\test_fixture_style.py fixture style - setup > scope_session
fixture style - setup > scope_module
fixture style - setup > scope_class
fixture style - setup > scope_default
fixture style - setup > scope_function
fixture style - setup > [testHam]
.
fixture style - teardown > fin_scope_function
fixture style - teardown > fin_scope_default
fixture style - setup > scope_default
fixture style - setup > scope_function
fixture style - setup > [testSpam]
.
fixture style - teardown > fin_scope_function
fixture style - teardown > fin_scope_default
fixture style - teardown > fin_scope_class
fixture style - teardown > fin_scope_module

myapp\tests\test_mix_style.py mix style (classic xunit) - setup > setup_class
mix style (classic xunit) - setup > setup_method
mix style (fixture) - setup > scope_session
mix style (fixture) - setup > scope_module
mix style (unittest) - setup > setUpClass
mix style (fixture) - setup > scope_class
mix style (fixture) - setup > scope_default
mix style (fixture) - setup > scope_function
mix style (unittest) - setup > setUp
mix style > [testHam]
mix style (unittest) - teardown > tearDown
.
mix style (fixture) - teardown > fin_scope_function
mix style (fixture) - teardown > fin_scope_default
mix style (classic xunit) - teardown > teardown_method
mix style (classic xunit) - setup > setup_method
mix style (fixture) - setup > scope_default
mix style (fixture) - setup > scope_function
mix style (unittest) - setup > setUp
mix style > [testSpam]
mix style (unittest) - teardown > tearDown
.
mix style (fixture) - teardown > fin_scope_function
mix style (fixture) - teardown > fin_scope_default
mix style (classic xunit) - teardown > teardown_method
mix style (fixture) - teardown > fin_scope_class
mix style (unittest) - teardown > tearDownClass
mix style (classic xunit) - teardown > teardown_class
mix style (fixture) - teardown > fin_scope_module

myapp\tests\test_unittest_style.py unittest style - setup > setUpClass
unittest style - setup > setUp
unittest style - setup > [testHam]
unittest style - teardown > tearDown
.
unittest style - setup > setUp
unittest style - setup > [testSpam]
unittest style - teardown > tearDown
.
unittest style - teardown > tearDownClass
mix style (fixture) - teardown > fin_scope_session
fixture style - teardown > fin_scope_session
```

　  
## 関係するブログ
[Django + pytestで、setupやteardown、fixtureのscopeなどの実行タイミングについて - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/04/29/063527)