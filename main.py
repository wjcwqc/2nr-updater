from random import *
import sys

import ddddocr
import requests

from staticres import *

# 验证码绕过
def verify_ocr(imgstr):
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
    with open("imgfile.gif", 'wb') as file:
        file.write(imgstr)
        file.close()
    res = ocr.classification(imgstr)
    return res

# 发送短信
def send_sms(region, phone,sms="update+validation"):
    # cookie = {"ASP.NET_SessionId": ''.join([choice(comstr) for i in range(24)])}
    # print(cookie)
    verify=requests.get(imgurl)
    # code = verify_ocr(verify.content)
    cookie=verify.cookies
    verify = requests.get(imgurl,cookies=cookie)
    code = verify_ocr(verify.content)
    rst = requests.post(shiyongurl, headers=header, cookies=cookie, data="id={}&phone={}&content={}&vcode={}".format(
        next((element for element in regionlist if element["CountryCode"] == region), None)['Id'], region + phone, sms,
        code)).text
    return rst

# 检擦发送状态
def check(rst):
    if rst.find("status=") == 0:
        rst = int(rst.split("=")[1])
        if rst > 80000:
            return True
        else:
            return rst
    else:
        return rst



def main():
    region,phone=sys.argv[1:]
    rst = check(send_sms(region, phone))
    if rst == True:
        print("True")
    elif rst == False:
        print("False")
    else:
        print("rst: ", rst)


if __name__ == '__main__':
    main()
