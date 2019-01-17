## DemoAPI
本文总结介绍接口测试框架开发，环境使用python3+selenium3+unittest测试框架及ddt数据驱动，采用Excel管理测试用例等集成测试数据功能，以及使用HTMLTestRunner来生成测试报告，目前有开源的poman、Jmeter等接口测试工具，为什么还要开发接口测试框架呢？因接口测试工具也有存在几点不足。
* 测试数据不可控制。比如接口返回数据不可控，就无法自动断言接口返回的数据，不能断定是接口程序引起，还是测试数据变化引起的错误，所以需要做一些初始化测试数据。接口工具没有具备初始化测试数据功能，无法做到真正的接口测试自动化。
* 无法测试加密接口。实际项目中，多数接口不是可以随便调用，一般情况无法摸拟和生成加密算法。如时间戳和MDB加密算法，一般接口工具无法摸拟。
* 扩展能力不足。开源的接口测试工具无法实现扩展功能。比如，我们想生成不同格式的测试报告，想将测试报告发送到指定邮箱，又想让接口测试集成到CI中，做持续集成定时任务。

## 测试框架处理流程
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/frame.JPG)

测试框架处理过程如下：
* 首先初始化清空数据库表的数据，向数据库插入测试数据；
* 调用被测试系统提供的接口，先数据驱动读取excel用例一行数据；
* 发送请求数据，根据传参数据，向数据库查询得到对应的数据；
* 将查询的结果组装成JSON格式的数据，同时根据返回的数据值与Excel的值对比判断，并写入结果至指定Excel测试用例表格；
* 通过单元测试框架断言接口返回的数据，并生成测试报告，最后把生成最新的测试报告HTML文件发送指定的邮箱。

## 测试框架结构目录介绍
目录结构介绍如下：
* config/:                 文件路径配置
* database/:               测试用例模板文件及数据库和发送邮箱配置文件
* db_fixture/:             初始化接口测试数据
* lib/:                    程序核心模块。包含有excel解析读写、发送邮箱、发送请求、生成最新测试报告文件
* package/:                存放第三方库包。如HTMLTestRunner，用于生成HTML格式测试报告
* report/:                 生成接口自动化测试报告
* testcase/:               用于编写接口自动化测试用例
* run_demo.py:             执行所有接口测试用例的主程序

## 测试结果展示
* HTML报告
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/report1.JPG)
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/report.JPG)
* Excel用例结果
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/excel.JPG)
* 邮件收到的测试报告
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/mail.JPG)
