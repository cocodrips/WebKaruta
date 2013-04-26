
import sys
import unittest
import os

def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/third_party/Flask-0.9/"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/third_party/Werkzeug-0.8.3/"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/third_party/python-dateutil-2.1/"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/third_party/six-1.1.0/"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/third_party/beautifulsoup4-4.1.1//"))
    sys.path.append(os.path.join(os.path.dirname(__file__), "app/"))
    main(sys.argv[1], os.path.join(os.path.dirname(os.path.realpath(__file__)), "tests"))