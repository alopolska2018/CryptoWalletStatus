import requests, json

coin_status = input('Coin name: ')
bittrex = requests.get('https://bittrex.com/api/v2.0/pub/currencies/GetWalletHealth').json()
bittrex_coin_status = bittrex['result']
for item in bittrex_coin_status:
    # print(item)
    coin = item['Currency']
    if coin['Currency'] == coin_status:
        coin_name = coin['Currency']
        coin_fee = coin['TxFee']
        coin_is_active = coin['IsActive']
        coin_is_restricted = coin['IsRestricted']
        print('BITTREX')
        print('Coin name: {}'.format(coin_name))
        print('Coin_fee: {}'.format(coin_fee))
        print('Coin_is_active: {}'.format(coin_is_active))
        print('Coin_is_restricted: {}'.format(coin_is_restricted))
    # if item['Currency']['Currency'] == 'XDN':
    #     print(item['Currency'][''])

binance = requests.get('https://www.binance.com/assetWithdraw/getAllAsset.html').json()
for coin in binance:
    if coin['assetCode'] == coin_status:
        coin_name = coin['assetCode']
        coin_fee = coin['transactionFee']
        coin_is_active = coin['enableWithdraw']
        coin_min_withdraw = coin['minProductWithdraw']
        print('BINANCE')
        print('Coin name: {}'.format(coin_name))
        print('Coin_fee: {}'.format(coin_fee))
        print('Coin_is_active: {}'.format(coin_is_active))
        print('Coin_min_withdraw: {}'.format(coin_min_withdraw))

hitbtc = requests.get('https://api.hitbtc.com/api/2/public/currency').json()
for coin in hitbtc:
    if coin['id'] == coin_status:
        coin_name = coin['id']
        coin_fee = coin['payoutFee']
        payinEnabled = coin['payinEnabled']
        payinPaymentId = coin['payinPaymentId']
        #Count of blocks confirmations, which are needed for deposit
        #payinConfirmations = coin['payinConfirmations']
        payoutEnabled = coin['payoutEnabled']
        payoutIsPaymentId = coin['payoutIsPaymentId']
        transferEnabled = coin['transferEnabled']
        delisted = coin['delisted']
        payoutFee = coin['payoutFee']
        print('HITBTC')
        print('Coin name: {}'.format(coin_name))
        print('Is allowed to generate addresses for a deposit: {}'.format(payinEnabled))
        print('Is required to provide additional information other than the address for deposit: {}'.format(payinPaymentId))
        print('Is withdraw allowed: {}'.format(payoutEnabled))
        print('Is providing of additional information for withdraw is allowed: {}'.format(payoutIsPaymentId))
        print('Transfer between trading account and bank account is allowed (may be disabled on maintenance): {}'.format(transferEnabled))
        print('if currency is delisted (deposit and trading are stopped): {}'.format(delisted))
        print('Default withdraw fee: {}'.format(payoutFee))