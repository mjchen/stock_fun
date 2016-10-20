__author__ = 'mingjun'
import os

from shared.common import stockinfo as stinfo
from shared import resources
import yahoo_finance as ys_finance

import shared.common.debug_utility as debug_util
# use useSamples as default folder for storing user sample files
samplepath = os.path.dirname(resources.__file__)
mylist = stinfo.load_data('overall_08012016.dat')
#stinfo.save_data(mylist,'conver.dat')


def getnumofemployee(symbol):
    test = ys_finance.Share(symbol)
    info = test.get_info()
    num=0
    industry = ''
    start = ''
    if 'FullTimeEmployees' in info:
        num = info['FullTimeEmployees']
    if 'Industry' in info:
        industry = info['Industry']
    if 'start' in info:
        start = info['start']
    return num, industry,start
for s in mylist:
   # t = (stinfo.StockInfo) s
    num, industry,start_date = getnumofemployee(s.symbol)
    print(s. __str__() + '\t'+ str(num)+'\t'+ str(industry)+'\t'+ str(start_date))
