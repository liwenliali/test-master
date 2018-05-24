

#python3+selenium3+unittest+ddt+HTMLReport webUI自动化测试框架。

环境搭建这里就不赘述了，网上资料大把抓，注意对应的驱动版本就行

### 1、简单介绍下框架以及目录结构吧：  ###

这里使用python写测试脚本，selenium WebDriver驱动浏览器，unittest组织测试用例，ddt作为数据驱动，HtmlReport生成测试报告

    	├─.idea
    	│  
    	├─Business		#封装业务逻辑流程
    	│
    	├─Common		#存放公共、通用的方法
    	│ 
    	├─Page_Object	#封装页面对象
    	│ 
    	├─report		#存放测试报告、日志和截图
    	│ 
    	├─Test_Case		#测试用例
    	│
    	├─Test_Data		#存放测试数据
    	│
    	├─Test_Suite	#测试套件
    	│
    	├─Run.py		#测试执行总入口


上传的源代码是用本机搭建了个大商创电商项目写了个注册的demo，能看清楚本框架的能力，大家可以自行阅读理解。

###2、日志长成这样： 

下图中16行的错误是由于测试数据最后一行多了一行空行，请忽略

![](https://i.imgur.com/lcOhta8.png)




 