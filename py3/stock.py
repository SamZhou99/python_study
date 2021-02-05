stockList = [{
    'name':
    '百润股份',
    'data': [{
        "price": float(80.6),
        "num": 900
    }, {
        "price": float(74.2),
        "num": 900
    }]
}]

for stockIndex in range(0, len(stockList)):
    stock = stockList[stockIndex]
    print()
    print(stock['name'])
    total = {
        'price': 0,
        'num': 0,
        'priceTotal': 0,
    }
    for stockDataIndex in range(0, len(stock['data'])):
        stockData = stock['data'][stockDataIndex]
        d = stockData
        d['priceTotal'] = d['price'] * d['num']
        print('\t明细', d)
        total['priceTotal'] += d['priceTotal']
        total['num'] += d['num']
    total['price'] = total['priceTotal'] / total['num']
    print('\t现价', total)
