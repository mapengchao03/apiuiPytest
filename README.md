# API-UI 自动化测试示例

---

## UI框架设计

- pytest
- selenium
- POM页面对象模型（Page Object Model）

---

## API框架设计

- pytest
- XXX
- XXX

---

## 目录结构

    allure-report             ——allure报告目录
    allure-result             ——allure结果目录
    base                      ——基础类
        basepage              ——基础页面对象类
        baserequest           ——基础API对象类
    commom                    ——公共方法
    config                    ——配置文件
    data                      ——测试数据
        api                   ——API测试数据
           case1_data
           ...
        ui                    ——UI测试数据
           case2_data
           ...
    logs                      ——日志目录
    myenv                     ——虚拟环境
    page_object               ——封装页面对象
        case2_object
           ...
    testcase                  ——测试用例
        api                   ——API测试用例
            case1
            ...
        ui                    ——UI测试用例
            case2
            ...
    .gitignore                ——git忽略文件
    conftest.py               ——pytest胶水文件
    pytest.ini                ——pytest配置文件
    README.md                 ——项目说明文件
    requirements.txt          ——项目依赖文件
    run.py                    ——项目运行文件

---

## 运行
### mac虚拟环境创建（建议，不强制要求）
- 先安装virtualenv工具
```shell
pip3 install virtualenv
```
- 然后在项目根目录下创建虚拟环境
```shell
#创建虚拟环境，指定Python版本为3.x
virtualenv my_virtualenv /usr/bin/python3
#这将在当前目录下创建一个名为my_virtualenv的文件夹，里面包含了独立的Python环境。
#要激活虚拟环境，使用以下命令：
source my_virtualenv/bin/deactivate
#你会看到命令行提示符变了，表明虚拟环境已经激活。现在你可以安装包，运行Python脚本，而不会影响到系统中的全局Python环境。
#要退出虚拟环境，使用命令：
deactivate
```

### 安装依赖
- 终端执行，在项目根路径下
```shell
pip3 install -r requirements.txt
```

### 执行主文件
- 在项目根目录执行`run.py`文件即可运行项目

## allure参数说明
- pytest main (--alluredir `结果目录`)
    - --clean-alluredir 清除历史生成记录
- allure generate + allure open 需要结合使用
    - allure generate `结果目录`
        - -c 生成报告前删除上一次生成的报告
        - -o 指定生成的报告目录
    - allure open `报告目录`
        - -h 对应host启动报告
        - -p 对应端口启动报告
- allure serve + 结果目录
    - 启动allure服务,并打开aluure报告
     
## 其他
### 生成requirements.txt
- 终端执行，在项目根路径下
- 有新安装的依赖或者升级了某个依赖版本，及时生成最新依赖文件
```shell
pip3 freeze > requirements.txt
```
### pytest.ini配置
- 参考地址：https://www.cnblogs.com/jinbiaobowen/p/17780765.html
```
[pytest]
addopts = -vs -n 2  #命令行的参数，用空格分隔
testpaths =./test_case #测试用例的路径 
python_files = test_*.py  #模块名的规则 
python_classes = Test*  #类名的规则 
python_functions = test  #方法名的规则 
markers =              
     smoke:冒烟用例  
　   usermanage:用户管理模块
     productmanage:商品管理模块
```

### pytest main ([option1,option2,...])配置
- -s：表示输出调试信息，包括print打印的信息
- -v：显示更详细的信息
- -q: 输出简化信息
- -vs：这两个参数一起用
- -n：支持多线程或者分布式运行测试用例 
- -reruns NUM：失败用例重跑
- -x：表示只要要一个用例报错，那么测试停止。
- -maxfail=2   出现两个用例失败就停止。
