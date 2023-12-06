from random import *

import ddddocr
import requests

from staticres import *

def verify_ocr(imgstr):
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)
    with open("imgfile.gif", 'wb') as file:
        file.write(imgstr)
        file.close()
    # print(imgstr)
    res = ocr.classification(imgstr)
    return res


def send_sms(region, phone):
    # cookie = {"ASP.NET_SessionId": ''.join([choice(comstr) for i in range(24)])}
    # print(cookie)
    sms = "update+validation"
    # print(cookie)
    verify=requests.get(imgurl)
    # code = verify_ocr(verify.content)
    cookie=verify.cookies
    verify = requests.get(imgurl,cookies=cookie)
    code = verify_ocr(verify.content)
    rst = requests.post(shiyongurl, headers=header, cookies=cookie, data="id={}&phone={}&content={}&vcode={}".format(
        next((element for element in regionlist if element["CountryCode"] == region), None)['Id'], region + phone, sms,
        code)).text
    print(rst)
    if rst.find("status=") == 0:
        rst = int(rst.split("=")[1])
    if rst > 80000:
        return True
    elif rst < 0:
        return False
    else:
        return rst


def main():
    rst = send_sms("48", "699527124")
    if rst == True:
        print("True")
    elif rst == False:
        print("False")
    else:
        print("rst: ", rst)


def test(region):
    return next((element for element in regionlist if element["CountryCode"] == region), None)


if __name__ == '__main__':
    main()
    # print(test("48"))
