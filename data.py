# class DataGrab:
#     def getBinanceSpot(self):
#
#         def splitPair(tickerString):
#             if tickerString[-4:] == 'USDT':
#                 return [tickerString.split('USDT')[0].lower(), 'usdt']
#             elif tickerString[-3:] == 'ETH':
#                 return [tickerString.split('ETH')[0].lower(), 'eth']
#             elif tickerString[-3:] == 'BTC':
#                 return [tickerString.split('BTC')[0].lower(), 'btc']
#             elif tickerString[-3:] == 'BNB':
#                 return [tickerString.split('BNB')[0].lower(), 'bnb']
#             return np.nan
#
#         url = 'https://api.binance.com/api/v1/ticker/24hr'
#         bnn_df = pd.DataFrame(requests.get(url).json())
#         # print(bnn_df)
#         bnn_df['symbol'] = bnn_df.apply(lambda x: splitPair(x['symbol']), axis=1)
#         bnn_df = bnn_df.dropna()
#         bnn_df['base'] = bnn_df.apply(lambda x: x['symbol'][0], axis=1)
#         bnn_df['quote'] = bnn_df.apply(lambda x: x['symbol'][1], axis=1)
#         bnn_df = bnn_df.rename(index=str, columns={'askPrice': 'ask',
#                                                    'bidPrice': 'bid',
#                                                    'lastPrice': 'price',
#                                                    })
#         columns = ['ask', 'bid', 'price', 'volume']
#         bnn_df['exchange'] = 'binance'
#         bnn_df[columns] = bnn_df[columns].astype(float)
#         bnn_df['spread'] = bnn_df.ask - bnn_df.bid
#         columns.extend(['base', 'quote', 'spread', 'exchange'])
#         bnn_df = bnn_df[columns]
#
#         bnn_df['ticker'] = bnn_df.apply(lambda x: x['base'] + '-' + x['quote'], axis=1).tolist()
#         bnn_df = bnn_df[['base', 'quote', 'exchange', 'price', 'ask', 'bid', 'spread', 'volume', 'ticker']].set_index('ticker')
#         del bnn_df.index.name
#         return bnn_df
#
# a = DataGrab().getBinanceSpot()
# print(a.head())
# print(a.to_csv('data_crypto.csv'))

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=f7f6fd1e-07d1-4a4e-875e-8d9d41936291'
print(url)


def my_assts():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=f7f6fd1e-07d1-4a4e-875e-8d9d41936291'
  asst = []
  for foo in range(6):
    t = []

    def get_latest_crypto_price():
      response = requests.get(url)
      response_json = response.json()

      return response_json['data'][foo]

    t.append((get_latest_crypto_price().get('name'), get_latest_crypto_price().get('quote').get('USD').get('price')))
    asst.append(t)

    # asst.append((get_latest_crypto_price().get('quote').get('USD').get('price'), get_latest_crypto_price().get('name')))
  return asst

print(my_assts())