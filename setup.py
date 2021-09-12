# coding:utf-8

from setuptools import setup,find_packages

# or
# from distutils.core import setup

setup(
        name='znrompt',     # 包名字
        version='1.0',   # 包版本
        description='This is a package of znsound',   # 简单描述
        author='mayong',  # 作者
        author_email='znsoft@163.com',  # 作者邮箱
        url='https://https://github.com/BIT-ENGD/qmprompt',      # 包的主页
        ackages = find_packages(),              # 包
        #package_dir ={ "qmprompt": "scripts/qmprompt" },
        install_requires=[
 
        'playsound>=1.１.0',
             
        
        ],
        py_modules=['znprompt'],
        
        scripts = [ "znprompt.py" ],
        #package_dir = {'': 'lib'},

        data_files=[('wave', ['wave/train_done.wav', 'wave/train_error.wav'])]

)