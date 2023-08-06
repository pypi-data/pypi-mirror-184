import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), "r", encoding="utf-8") as fp:
    long_description = fp.read()

setuptools.setup(

    # 包名称 - 注意: 使用 pypi 中存在包名会上传失败
    name="aclient",
    # 包版本号，便于维护版本
    version="1.0.0",
    # 自己项目地址，比如github的项目地址
    url="https://github.com/PengKe-x/AsyncHttpClient",
    # 作者，可以写自己的姓名
    author="PengKe",
    # 作者联系方式，可写自己的邮箱地址
    author_email="925330867@qq.com",
    # 包的简述
    description="发送大量异步请求",
    # 包的详细介绍，一般在 README.md 文件内
    long_description=long_description,
    # 文件 README.md 阅读支持类型
    long_description_content_type="text/markdown",

    # 表明当前模块依赖哪些包，若环境中没有，则会从 pypi 中下载安装
    install_requires=["aiohttp", "yarl"],
    # setup.py 本身要依赖的包，这通常是为一些setuptools的插件准备的配置
    # 这里列出的包，不会自动安装。
    setup_requires=[],
    # 用于安装setup_requires或tests_require里的软件包
    # 这些信息会写入egg的 metadata 信息中
    dependency_links=[],
     # install_requires 在安装模块时会自动安装依赖包
    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    # extras_require= {}

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 对 Python 的最低版本要求
    python_requires='>=3.6',
)