# api-demo 




配置示例
```
{
    # 域名配置
    "trade_host": "http://open-jy-uat.yxzq.com",
    "quote_host": "https://open-hz-uat.yxzq.com",
    "ws_host": "wss://open-hz-uat.yxzq.com/wss/v1",
    "ws_origin": "https://open-hz-uat.yxzq.com",
    # 默认用户配置
    "default_user": {
        "X-Lang": "1",
        "X-Channel": "914",
        "areaCode": "86",
        "phoneNumber": "15210372164",
        "login_password": "qwe123456",
        "trade_passwrod": "123456",
        "public_key": "",
        "private_key": ""
       },
    # 多用户配置
    "13750062348": {
        "X-Lang": "1",
        "X-Channel": "1000193854",
        "areaCode": "86",
        "phoneNumber": "13750062348",
        "login_password": "qwe123456",
        "trade_passwrod": "123456",
        "public_key": "",
        "private_key": ""
    }
}
```

config.json 配置项
- X-Channel 分配渠道号
- areaCode  手机区号
- phoneNumber  手机号
- login_password  登录密码
- public_key  公钥
- private_key 私钥

线上host配置
- "trade_host": "http://open-jy.yxzq.com",
- "quote_host": "https://open-hz.yxzq.com:8443",
- "ws_host": "wss://open-hz.yxzq.com:8443/wss/v1",
- "ws_origin": "https://open-hz.yxzq.com",

uat配置
- "trade_host": "http://open-jy-uat.yxzq.com",
- "quote_host": "https://open-hz-uat.yxzq.com",
- "ws_host": "wss://open-hz-uat.yxzq.com/wss/v1",
- "ws_origin": "https://open-hz-uat.yxzq.com",


文件说明 <br>
/api/trade.py 可自行按照文档添加接口 <br>
/api/quote_push.py 行情推送相关 <br>
example.py 例子 <br>


