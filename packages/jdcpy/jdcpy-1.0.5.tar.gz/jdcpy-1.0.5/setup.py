from distutils.core import setup

setup(
    name="jdcpy",
    author="JaydenFish@ThizGroup",
    author_email="xmyjd@163.com",
    version="1.0.5",
    py_modules=['jdcpy'],
    install_requires=['pandas'],
    description="jdcpy模块,吉富数据中心的python接口",
    long_description=open("source/jdcpy.rst").read()
)
