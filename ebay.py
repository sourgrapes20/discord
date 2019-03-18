import requests
from bs4 import BeautifulSoup as bs
import names
import random

session = requests.session()

def watch(link, number):
    for i in range(number):
        requests.get(link)
    print("done")
        #print(i)

#watch("https://www.ebay.com/itm/312532850190", 100)



"""
fName = names.get_first_name()
lName = names.get_last_name()
email = str(random.randint(1,100000000000))+"@enugrasaio.club"
password = "testing1235"

print(fName, lName, email, password)

link = "https://reg.ebay.com/reg/PartialReg"
payload = {
    "isSug": "false",
    "countryId": "1",
    "userid": "",
    "ru": "http://www.ebay.com/",
    "firstname": fName,
    "lastname": lName,
    "email": email,
    "PASSWORD": password,
    "checkbox-default": "on",
    "mblChk": "0",
    "promotion": "true",
    "iframeMigration1": "true",
    "mode": "1",
    "frmaction": "submit",
    "tagInfo": "ht5%3DAQAAAWlLJlj8AAUxNjk3OWQwZTJjMy5hYjQ1NjBjLjViMzVkLmZmZmQ5Yzczrdyf%252FZTAjMsNiAXzsLA%252BVTPaQLA*%7Cht5new%3Dtrue%26usid%3D79d0e2c31690ab4560c5b35dfffd9c72",
    "hmvb":"",
    "isGuest": "0",
    "idlstate":"",
    "profilePicture":"",
    "agreement": "Terms and conditions",
    "signInUrl": "https%3A%2F%2Fsignin.ebay.com%2Fws%2FeBayISAPI.dll%3FSignIn%26ru%3Dhttps%253A%252F%252Fwww.ebay.com%252F%26regUrl%3Dhttps%253A%252F%252Freg.ebay.com%252Freg%252FPartialReg%253Fru%253Dhttps%25253A%25252F%25252Fwww.ebay.com%25252F",
    "personalFlag": "true",
    "isMobilePhone":"",
    "_trksid": "p2052190",
    "ets": "AQADAAAAEFIbPNfqg4fieKxm5Zlnnmc"
}
response1 = session.post(link, data = payload)
print(response1)

"""


#r = requests.get("https://www.ebay.com/itm/JBL-UA-SPORT-FLEX-Wireless-Neckband-Sport-Headphones-Grey/202597411146?_trkparms=5373%3A0%7C5374%3AFeatured")
