import requests

REQ_URL = "http://api.tushare.pro"
TOKEN = "a814fe62e85ddfb33eebb7607439e60560a3a964eac5ba9f725b5b1d"

json_data = {
    "api_name": "stock_basic",
    "token": TOKEN,
    "params": {"list_status": "L"},
    "fields": "open,high,low,close",
}
response = requests.post(REQ_URL, json=json_data)
# 输出响应内容 {"request_id":"7c339236-a483-41ce-8d52-e5cda3b606e1","code":40203,"data":null,"msg":"抱歉，您没有接口访问权限，权限的具体详情访问：https://tushare.pro/document/1?doc_id=108。"}
print(response.text)
