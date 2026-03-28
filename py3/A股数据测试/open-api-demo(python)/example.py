# -*- coding: utf-8 -*-
import time
from api import trade
from api.quote_push import QuoteContext







def trade_main():
    # 登录
    ctx = trade.get_context_by_phonenumber()
    # ctx = trade.get_context_by_phonenumber(phoneNumber="13750062348")
    ctx.login()

    # 交易相关
    ctx.trade_login()
    ctx.entrust_order(entrustAmount='100', entrustPrice='250', entrustProp='0', 
            entrustType='0', exchangeType='0', stockCode='03690', forceEntrustFlag=True)

    ctx.modify_order(actionType='0', entrustAmount='0', entrustId="aaaa", 
            entrustPrice='0', forceEntrustFlag=True)

    ctx.today_entrust(exchangeType='0')
    
    # IPO相关
    ctx.ipo_list(status=0)
    ctx.apply_ipo(applyQuantity=100, applyType=1, ipoId="1303001330712207360")
    ctx.ipo_record_list(applyTimeMin="2021-01-25 00:00:00", applyTimeMax="2021-01-27 00:00:00")
    ctx.ipo_record(applyId="1354026198750011392")

    # 行情相关
    ctx.marketstate(market='sh')
    ctx.realtime(secuIds=["sz000001", "hk00700"])
    ctx.timeline(secuId="sz000001", type=0)
    ctx.kline(secuId="sz000001", type=7, start=20201221160000000, count=2, right=0)
    ctx.tick(secuId="sz000001", tradeTime=20201221160000000, seq=0, count=2, sortDirection=1)
    ctx.orderbook(secuId="sz000001")


def quote_push_main():
    # 行情推送
    token = trade.get_context_by_phonenumber().login()
    ctx = QuoteContext(token)
    
    testTopics = ["rt.hk.00700", "ob.hk.00700", "tk.hk.00700"]
    ctx.set_handler(my_handler)
    ctx.start()
    ctx.subscribe(testTopics)
    # time.sleep(30)
    # ctx.unsubscribe(testTopics)
    # time.sleep(60)
    # ctx.stop()

    # 等待线程结束
    ctx.run_thread.join()


def my_handler(topic, data):
    # 自定义的回调函数，topic与订阅主题相同，data返回数据
    # tk: tick，逐笔成交 / rt: realtime，实时行情 / ob: orderbook，买卖盘
    if topic[:2] in ('tk'):
        print('deal tk', topic, data)
    if topic[:2] in ('rt'):
        print('deal rt', topic, data)
    if topic[:2] in ('ob'):
        print('deal ob', topic, data)



if __name__ == "__main__":
    # trade_main()
    quote_push_main()
    # pass

