
import tushare as ts


# ts.set_token(token)

pro = ts.pro_api()

pro.query("stock_basic")

url = "http://api.tushare.pro/api_name=stock_basic&token=c7b68d2a726dc747e6d6c4484a42b9275b7d8389aaa252da8cf14fed"

import requests
import json
url = "http://api.tushare.pro"
token = "c7b68d2a726dc747e6d6c4484a42b9275b7d8389aaa252da8cf14fed"
#
# x1 = requests.post(url, data=json.dumps({"api_name": "stock_basic", "token": token}))
# # print(x1.status_code)
# print(x1.json())

x2 = requests.post(url, json={"api_name": "stock_basic", "token": token})
print(x2.status_code)
print(x2.json())

