# -*- coding: utf-8 -*-
import os
import json
from common import req_util





class tradeContext(req_util.RequestUtil):


    def trade_login(self):
        """解锁交易"""
        api = '/user-server/open-api/trade-login'
        params = {
            "password": self.encryptUtil.rsa_encrypt(self.trade_passwrod)
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs
    
    def entrust_order(self, entrustAmount, entrustPrice, entrustProp, entrustType, exchangeType, stockCode, forceEntrustFlag):
        """下单"""
        api = '/stock-order-server/open-api/entrust-order'
        params = {
            'serialNo': self.encryptUtil.gen_serialno_str(),
            'entrustAmount': entrustAmount,
            'entrustPrice': entrustPrice,
            'entrustProp': entrustProp,
            'entrustType': entrustType,
            'exchangeType': exchangeType,
            'stockCode': stockCode,
            'password': self.encryptUtil.rsa_encrypt(self.trade_passwrod),
            'forceEntrustFlag': forceEntrustFlag
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs

    def modify_order(self, actionType, entrustAmount, entrustId, entrustPrice, forceEntrustFlag):
        """委托改单/撤单"""
        api = '/stock-order-server/open-api/modify-order'
        headers = {
            'Authorization': self.token,
            'X-Request-Id': self.encryptUtil.gen_unix_time_str(16)
        }
        
        params = {
            'actionType': actionType,
            'entrustAmount': entrustAmount,
            'entrustId': entrustId,
            'entrustPrice': entrustPrice,
            'forceEntrustFlag': forceEntrustFlag,
            'password': self.encryptUtil.rsa_encrypt(self.trade_passwrod)
        }
        rs = self.post_with_sign_by_trade(api, params, headers=headers)
        return rs

    def today_entrust(self, exchangeType, pageNum='0', pageSize='20', stockCode=''):
        """今日订单分页查询"""
        api = '/stock-order-server/open-api/today-entrust'
        
        params = {
            'exchangeType': exchangeType,
            'pageNum': pageNum,
            'pageSize': pageSize,
            'stockCode': stockCode
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs

    def apply_ipo(self, applyQuantity, applyType, ipoId, cash=0):
        """新股认购"""
        api = '/stock-order-server/open-api/apply-ipo'
        
        params = {
            'applyQuantity': applyQuantity,
            'applyType': applyType,
            'ipoId': ipoId,
            'cash': cash,
            'serialNo': self.encryptUtil.gen_serialno_str()
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs

    def ipo_list(self, pageNum=1, pageSize=10, status=1):
        """获取ipo列表-分页"""
        api = '/stock-order-server/open-api/ipo-list'
        
        params = {
            'pageNum': pageNum,
            'pageSize': pageSize,
            'status': status
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs

    def ipo_record(self, applyId):
        """ipo申购明细"""
        api = '/stock-order-server/open-api/ipo-record'
        
        params = {
            'applyId': applyId
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs

    def ipo_record_list(self, applyTimeMin, applyTimeMax, pageNum=1, pageSize=10):
        """ipo申购明细-分页"""
        api = '/stock-order-server/open-api/ipo-record-list'
        
        params = {
            'pageNum': pageNum,
            'pageSize': pageSize,
            'applyTimeMin': applyTimeMin,
            'applyTimeMax': applyTimeMax
        }
        rs = self.post_with_sign_by_trade(api, params)
        return rs
    



    def marketstate(self, market):
        """市场状态接口"""
        api = "/quotes-openservice/api/v1/marketstate"
        params = {"market": market}
        rs = self.post_with_sign_by_quote(api, params)
        return rs
    
    def basicinfo(self, market):
        """基础信息接口"""
        api = "/quotes-openservice/api/v1/basicinfo"
        params = {
            "market": market
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs
    
    def realtime(self, secuIds=[]):
        """实时行情接口"""
        api = "/quotes-openservice/api/v1/realtime"
        params = {
            "secuIds": secuIds
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs
    
    def timeline(self, secuId, type=0):
        """分时接口"""
        api = "/quotes-openservice/api/v1/timeline"
        params = {
            "secuId": secuId,
            "type": type
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs
    
    def kline(self, secuId, type, start, right, count):
        """K线接口"""
        api = "/quotes-openservice/api/v1/kline"
        params = {
            "secuId": secuId,
            "type": type,
            "start": start,
            "right": right,
            "count": count
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs

    def tick(self, secuId, tradeTime, seq, count, sortDirection):
        """逐笔接口"""
        api = "/quotes-openservice/api/v1/tick"
        params = {
            "secuId": secuId,
            "tradeTime": tradeTime,
            "seq": seq,
            "count": count,
            "sortDirection": sortDirection
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs
    
    def orderbook(self, secuId):
        """买卖盘接口"""
        api = "/quotes-openservice/api/v1/orderbook"
        params = {
            "secuId": secuId
        }
        rs = self.post_with_sign_by_quote(api, params)
        return rs



def load_config():
    with open(os.environ['API_DEMO_HOMEPATH']+'/conf/config.json', 'r') as f:
        return json.load(f)

def get_context_by_phonenumber(phoneNumber="default_user"):
    """
    从配置中取指定用户信息
    初始化实例
    """
    config = load_config()
    trade_host = config["trade_host"]
    quote_host = config["quote_host"]
    user_config = config[phoneNumber]
    X_Lang = user_config["X-Lang"]
    X_Channel = user_config["X-Channel"]
    areaCode = user_config["areaCode"]
    phoneNumber = user_config["phoneNumber"]
    login_password = user_config["login_password"]
    trade_passwrod = user_config["trade_passwrod"]
    public_key  = user_config["public_key"]
    private_key = user_config["private_key"]

    return tradeContext(trade_host, quote_host, X_Lang, X_Channel, areaCode, 
                phoneNumber, login_password, trade_passwrod, public_key, private_key)
    