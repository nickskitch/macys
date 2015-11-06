__author__ = 'Nick'
import subprocess
import decimal
import time
import library
import time

import os


library.singleton()


def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

def getBitcoinUSD():
    bitcoinPriceUrl='http://bcchanger.com/bitcoin_price_feed.php?feed_type=text&currency=USD'
    cmd2 = "curl -s "+bitcoinPriceUrl
    bitcoinPrice = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

    bitcoinPriceSplit = bitcoinPrice.split('.')
    bitcoinPrice=bitcoinPriceSplit[0]
    return bitcoinPrice

try:
    lastBitcoinPricef=open("/tmp/lastBitcoinPrice.txt", "r")
    oldPrice=lastBitcoinPricef
    lastBitcoinPricef.close()
    if not str.isdigit(oldPrice): raise Exception
except:
    oldPrice=getBitcoinUSD()

while True:


    print oldPrice

    bitcoinPrice=getBitcoinUSD()
    print bitcoinPrice +'new'

    prices = [int(bitcoinPrice),int(oldPrice)]

    for a, b in zip(prices[::1], prices[1::1]):
        percentDiff = 100 * (b - a) / a
        #print str(percentDiff) + "% difference"


    if (percentDiff < -10) or (percentDiff > 10):
        messageText='bitcoin price is ' + str(percentDiff) + "% difference: $" + bitcoinPrice
        message(messageText)

    # num=400
    # if int(bitcoinPrice) < num:
    #     message("bitcoin price under " + str(num) + " $" + bitcoinPrice)
    #
    # num=500
    # if int(bitcoinPrice) > num:
    #     message("bitcoin price over " + str(num) + " $" + bitcoinPrice)


    # if it's six AM, exit, so the next cron job can start at 7
    if time.strftime("%H") == '06':
        lastBitcoinPricef=open("/tmp/lastBitcoinPrice.txt", "w")
        lastBitcoinPricef.writelines(bitcoinPrice)
        lastBitcoinPricef.close()

    #if time.strftime(time.now()) = 08 : exit()
    time.sleep(600)
