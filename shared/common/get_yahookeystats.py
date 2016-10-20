__author__ = 'mingjun'

import urllib
import shared.common.debug_utility as debug_util

logger = debug_util.logging.getLogger(__name__)

#print(res.text)
#web = urllib.request.urlopen("http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500")


TOEKN_OCF = "Operating Cash Flow (ttm):</td><td class=\"yfnc_tabledata1\">"
TOKEN_LFCF = "Levered Free Cash Flow (ttm):</td><td class=\"yfnc_tabledata1\">"
TOKEN_SO="Shares Outstanding<font size=\"-1\"><sup>5</sup></font>:</td><td class=\"yfnc_tabledata1\">"
TOKEN_PROFIT= "Profit Margin (ttm):</td><td class=\"yfnc_tabledata1\">"
TOKEN_BOOKVALUE="Book Value Per Share (mrq):</td><td class=\"yfnc_tabledata1\">"
HEAD= "https://sg.finance.yahoo.com/q/ks?s="
TAIL = "+Key+Statistics"

def getbaseinfo(stockobj):
    url = HEAD+stockobj.symbol+TAIL
    logger.info(url)
    web = urllib.urlopen(url)
    s = web.read()
    ys = str(s)

    stockobj.freecashflow =  getdata(ys,TOEKN_OCF)
    stockobj.leveredcashflow =  getdata(ys,TOKEN_LFCF)
    stockobj.shares =  getdata(ys,TOKEN_SO)
    stockobj.profit_margin = getdata(ys,TOKEN_PROFIT)
    stockobj.book_value = getdata(ys,TOKEN_BOOKVALUE)
    return stockobj

def getdata(ys, token):
    idx = ys.find(token)
    idxEnd = ys.find("<", idx+len(token))

    return convert(ys[idx+len(token):idxEnd],token)

def convert(val,token):
    lookup = {'%': 0.01,'K': 1000, 'M': 1000000, 'B': 1000000000}
    res = 0
    if len(val) > 1:
        unit = val[-1]
        try:
            number = float(val[:-1])
     #       print(val[:-1])
            if unit in lookup:
                return lookup[unit] * number
            else:
                return number
        except ValueError:
            logger.warn("parsing error: " + val + token)
    return float(res)
