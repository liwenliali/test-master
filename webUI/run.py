# 统一运行入口
import unittest
import HTMLReport
from Test_Suite import registration_suite

# 总的测试套件
suite = unittest.TestSuite()

# 将需要执行的测试加入到总的测试套件中
suite.addTests(registration_suite.return_suite())

# 执行测试并生成报告
HTMLReport.TestRunner(
    report_file_name="测试报告文件名称",
    title="测试报告标题",
    description="测试报告描述",
    thread_count=3,    # 多线程启动chromedriver运行测试用例
    thread_start_wait=3     #设置线程启动的延迟时间
).run(suite)
