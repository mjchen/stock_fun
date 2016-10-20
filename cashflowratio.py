__author__ = 'mingjun'

import yahoo_finance as ys_finance
from shared.common import get_yahookeystats as ysstats
from shared.common import getstocksymbols as st_symbol
from shared.common import stockinfo
import futures
import shared.common.debug_utility as debug_util


logger = debug_util.logging.getLogger(__name__)
slists = st_symbol.StockInfo()
print (len(slists.symbollist))

def checkstock(symbol):

    stockobj = stockinfo.StockIno(symbol)
    try :
        test = ys_finance.Share(symbol)
    except:
        return None
    stockobj.price = test.get_price()

    info = test.get_info()
    num = 0
    if 'FullTimeEmployees' in info:
        num = info['FullTimeEmployees']

 #   if num < 10:
  #      return None
    stockobj = ysstats.getbaseinfo(stockobj)
    if(stockobj.shares <100):
        return None
    marketcap = stockobj.shares*float(stockobj.price)
    bookcap = stockobj.shares*float(stockobj.book_value)
    t1 = stockobj.freecashflow/marketcap
    t2 = stockobj.leveredcashflow/marketcap

    if( t1 > 0.2 and
                t2 > 0.2 and
                marketcap > 100000000 and
                stockobj.profit_margin > 0.1):
        stockobj.FCFratio = t1
        stockobj.LCFratio = t2
        return stockobj

    return None

def get_infopool(symbollist):
    outlist=[]
    with futures.ThreadPoolExecutor(max_workers=60) as executor:
        future_to_url = dict((executor.submit(checkstock, url), url)
                             for url in symbollist)

        for future in futures.as_completed(future_to_url):
            url = future_to_url[future]
            if future.exception() is not None:
                logger.error('%r generated an exception: %s' % (url,
                                                         future.exception()))
            tmp = future.result(2)
            if tmp is not None:
                outlist.append(tmp)
                logger.info(tmp)
        return outlist

selectlist=[]
count =0
for s in slists.symbollist:
     selectlist.append(s)
#     count+=1
#     if count>1000:
#        break
logger.info(selectlist)
mylist = get_infopool(selectlist)
logger.info(mylist)
selectlist = mylists

print("===================================================")
for stock in selectlist:
    logger.nfo(stock)
stockinfo.save_data(selectlist, "overall_08012016.dat")


