#第一课
#创建自己的Python库并发布到线上


#1 创建文件夹nester，并在nester中
#2 编写jcg_nester.py
#3 创建setup.py
#4 在pypi.org社区网站创建账号
#5 在命令行工具中编译：

#	 切换到nester
#	构建一个发布文件：
	python setup.py sdist
#	将发布安装到Python本地副本中
	python setup.py install
#	到此发布就绪
#	开发发布，命令行中登录注册
	python setup.py register
#	输入pypi用户名
#	输入pypi密码
#	上传代码
	python setup.py sdist upload


#上面的方法已经不行了，咋们来试试另外的方法：
#首先安装：
python -m pip install -U setuptools

#切换到nester
#构建一个发布文件：
python setup.py sdist build
# 上传source 包
python setup.py sdist upload
# 上传pre-compiled包
python setup.py bdist_wheel upload

#上传生成的包，可以使用setuptools,或者twine上传,推荐使用twine上次，因为使用setuptools上传时，你的用户名和密码是明文或者未加密传输，安全起见还是使用twine吧
# 使用twine上传,先安装twine

# 啃爹的教程，还是看网上详情 https://pypi.org/help/#project-name
# 后面统一改成twine来发布代码了
python -m pip install -U  twine
# 项目不能重名nester改成了chaingree_nester

#	构建一个发布文件：
python setup.py sdist build
	
twine upload dist/*