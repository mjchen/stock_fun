__author__ = 'mingjun'
import os
import pickle
from shared import resources
import shared.common.debug_utility as debug_util
# use useSamples as default folder for storing user sample files
samplepath = os.path.dirname(resources.__file__)
samplepath = samplepath + '\\'
logger = debug_util.logging.getLogger(__name__)
class StockIno():
    def __init__(self, symbol):
        self.symbol = symbol
        self.freecashflow = None
        self.leveredcashflow = None
        self.shares = None
        self.price = None
        self.FCFratio = None
        self.LCFratio = None
        self.profit_margin = None
        self.book_value = None
    def __str__(self):
        return self.symbol + '\t' + str(self.price)+'\t' \
                    + str(self.shares) + '\t'+str(self.FCFratio)+'\t'+str( self.LCFratio)+'\t'+str( self.profit_margin) \
                    + '\t' + str( self.book_value)
    def __repr__(self):
        return self.__str__()


def load_data( filename ="bin.dat"):
    try:
        with open(samplepath + filename) as f:
            liststockinfo = pickle.load(f)
    except:
        liststockinfo =[]
    return liststockinfo

def save_data(data, filename ="bin.dat" ):
    with open(samplepath +filename, "wb") as f:
        pickle.dump(data, f)
    logger.info("save data successful " + samplepath + filename)