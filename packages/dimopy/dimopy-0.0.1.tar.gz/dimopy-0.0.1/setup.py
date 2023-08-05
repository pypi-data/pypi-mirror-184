from setuptools import setup, find_packages
from os import path
from io import open  # for Python 2 and 3 compatibility


this_directory = path.abspath(path.dirname(__file__))


# read the contents of README.rst
def readme():
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


# read the contents of requirements.txt
with open(path.join(this_directory, 'requirements.txt'),
          encoding='utf-8') as f:
    requirements = f.read().splitlines()
'''
https://www.cnblogs.com/maociping/p/6633948.html
'''
setup(
    name="dimopy",  # 项目名称
    version="0.0.1",  # 新的算法引入\.新的功能引入\.bug修复    项目版本信息
    author="sunshubei",
    author_email="shubei.sun@di-matrix.com",  # 作者邮箱
    description="描述信息",  # 项目简介
    long_description=readme(),  # 项目详细的介绍  这里直接读取README.md文件
    long_description_content_type="text/markdown",  # 项目详细介绍的文件类型
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    download_url="https://pypi.doban.com/simple",  # 源地址
    install_requires=requirements,
    setup_requires=['setuptools>=38.6.0'],
    package_dir={"": "../dimopy_lib"},  # 自己的包所在目录
    packages=find_packages(where="../dimopy_lib", exclude=["target"]),  # 所有模块所在目录
    python_requires=">=3.8",  # python所需要的版本
    zip_safe=False
)
