#!/usr/bin/env python
# !coding:utf-8
import sys

class TelecomCarrier_Util:
    #判断电话号码是属于哪个运营商的
    # chinamobile= ['139', '138', '136', '135','137', '134', '159', '150','151', '152','158','157','159','178','188','187','183','182','184','147']
    chinamobile= ['134','135','136','137','138','139','147','150','151','152','157','158','159','182','183','184','187','188','178','198','148']
    unicomobile=['186','185','156','131','130','155','132','176','145','171','166','146','175']
    telecomobile=['133','153','180','181','189','173','177','199']

    viturechinamobile=["1703",'1705','1706']
    vitureunicomobile=['1704','1707','1708','1709']
    vituretelecomobile=['1700','1701','1702']

    iotchinamobile=["1440",]
    iotunicomobile=["1400"]
    iottelecombile=['1410',]



    def __init__(self):
        pass

    def ischinamobile(self,phone):
        phone=phone[:3]
        if phone in self.chinamobile:
            return True
        else:
            return False

    '''
    查询运营商号段：
    输入：
        电话号码
    输出：
        号码错误:-1
        未知：0
        移动：1
        联通：2
        电信：3
    '''

    @staticmethod
    def carrieroperator(phone):
        try:
            # 如果是86开头的号码则去掉前面的两位
            if len(phone) >11:
                phone=phone[-11:]
            # print phone
            #使用正则表达式判断号码是否合法
            if  phone.isdigit():
                if phone[:1] == "1":
                    SectionNo = phone[:3]
                    if SectionNo in TelecomCarrier_Util.chinamobile:
                        return 1
                    elif SectionNo in TelecomCarrier_Util.unicomobile:
                        return 2
                    elif SectionNo in TelecomCarrier_Util.telecomobile:
                        return 3
                    else:
                        SectionNo = phone[:4]
                        if SectionNo in TelecomCarrier_Util.viturechinamobile:
                            return 1
                        elif SectionNo in TelecomCarrier_Util.vitureunicomobile:
                            return 2
                        elif SectionNo in TelecomCarrier_Util.vituretelecomobile:
                            return 3
                        else:
                            return 0
            return -1
        except:
            print sys.exc_info()



