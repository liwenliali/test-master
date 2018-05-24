import unittest

from Test_Case.registration_case import registrationcase


def return_suite():
    # 测试套件
    suite = unittest.TestSuite()
    # 加载器
    loader = unittest.TestLoader()
    # 通过使用加载器，将测试用例添加到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(registrationcase))

    # 返回测试套件
    return suite
