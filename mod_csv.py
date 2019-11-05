# import csv
# import datetime
# import requests

# with open('btcusd.csv') as csvfile:
#     readCSV = csv.reader(csvfile)
#     # next(csvfile)
#
#     for row in readCSV:
#         # print(row)
#         y = int(row[0][0:4])
#         m = int(row[0][5:7])
#         d = int(row[0][8:10])
#
#         new_date = int(datetime.datetime(y, m, d, 0, 0).timestamp())
#         print(new_date, row[2], row[3], row[4], row[5])
#
#     # with open('new_btcusd.csv') as new_file:
#     #     csv_writer = csv.writer(new_file)
#     #
#     #     for row in readCSV:
#     #         csv_writer.writerow(row)



# Date,Symbol,Open,High,Low,Close,Volume BTC,Volume USD

import requests

while True:
    # base URLs
    globalURL = "https://api.coinmarketcap.com/v1/global/"
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

    # get data from globalURL
    request = requests.get(globalURL)
    data = request.json()
    globalMarketCap = data['total_market_cap_usd']

    # menu
    print()
    print("Welcome to the CoinMarketCap Explorer!")
    print("Global cap of all cryptocurrencies: $" + str(globalMarketCap))
    print("Enter 'all' or 'name of crypto' (i.e. bitcoin) to see the name of the top 100 currencies or a specific currency")
    print()
    choice = input("Your choice: ")

    if choice == "all":
        request = requests.get(tickerURL)
        data = request.json()

        for x in data:
            ticker = x['symbol']
            price = x['price_usd']

            print(ticker + ":\t\t$" + price)
        print()

    else:
        tickerURL += '/'+choice+'/'
        request = requests.get(tickerURL)
        data = request.json()

        ticker = data[0]['symbol']
        price = data[0]['price_usd']

        print(ticker + ":\t\t$" + price)
        print()

    choice2 = input("Again? (y/n): ")
    if choice2 == "y":
        continue
    if choice2 == "n":
        break