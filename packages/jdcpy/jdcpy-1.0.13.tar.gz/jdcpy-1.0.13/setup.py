from distutils.core import setup

setup(
    name="jdcpy",
    author="JaydenFish@ThizGroup",
    author_email="xmyjd@163.com",
    version="1.0.13",
    py_modules=['jdcpy'],
    install_requires=['pandas'],
    description="jdcpy模块,吉富数据中心的python接口",
    long_description=open("jdcpy.md", encoding='utf8').read()
)
