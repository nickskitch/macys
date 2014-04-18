__author__ = 'Nick'
import subprocess
import decimal
import time
import library

import os
def tail(f, n, offset=0):
    """Reads a n lines from f with an offset of offset lines."""
    avg_line_length = 74
    to_read = n + offset
    while 1:
        try:
            f.seek(-(avg_line_length * to_read), 2)
        except IOError:
            # woops.  apparently file is smaller than what we want
            # to step back, go to the beginning instead
            f.seek(0)
        pos = f.tell()
        lines = f.read().splitlines()
        if len(lines) >= to_read or pos == 0:
            return lines[-to_read:offset and -offset or None]
        avg_line_length *= 1.3

def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()


while True:

    if not library.isPingable('bcchanger.com'):
        break

    lastBitcoinPricef=open("/tmp/lastBitcoinPrice.txt", "r")

    oldPrice=tail(lastBitcoinPricef,1)
    lastBitcoinPricef.close()
    print oldPrice

    bitcoinPriceUrl='http://bcchanger.com/bitcoin_price_feed.php?feed_type=text&currency=USD'

    cmd2 = "curl -s "+bitcoinPriceUrl

    bitcoinPrice = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

    bitcoinPriceSplit = bitcoinPrice.split('.')
    bitcoinPrice=bitcoinPriceSplit[0]
    print bitcoinPrice

    prices = [int(bitcoinPrice),int(oldPrice[0])]

    for a, b in zip(prices[::1], prices[1::1]):
        percentDiff = 100 * (b - a) / a
        #print str(percentDiff) + "% difference"


    if (percentDiff < -10) or (percentDiff > 10):
        messageText='bitcoin price is ' + str(percentDiff) + "% difference: $" + bitcoinPrice
        message(messageText)

    num=400
    if int(bitcoinPrice) < num:
        message("bitcoin price under " + num + " $" + bitcoinPrice)

    num=500
    if int(bitcoinPrice) > num:
        message("bitcoin price under " + num + " $" + bitcoinPrice)


    lastBitcoinPricef=open("/tmp/lastBitcoinPrice.txt", "a")
    lastBitcoinPricef.writelines(bitcoinPrice+"\n")

    lastBitcoinPricef.writelines('10\n')
    lastBitcoinPricef.close()

    # if it's six AM, exit, so the next cron job can start at 7
    if time.strftime("%H") == '06':
        exit()

    time.sleep(600)
