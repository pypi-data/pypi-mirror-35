jdcpy模块
本模块是吉富数据中心的python版接口
提供下载基金相关信息的功能
大致使用方法如下:
from jdcpy import jdcpy
jdcpy.login('username','password')
jdcpy.info(基金list,基本信息list,投资分布信息list,业绩表现list)
jdcpy.nav(基金list,起始日期,最终日期,信息类别list)