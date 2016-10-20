__author__ = 'mingjun'
import os
from shared import resources
import shared.common.debug_utility as debug_util

# use useSamples as default folder for storing user sample files
samplepath = os.path.dirname(resources.__file__)
logger = debug_util.logging.getLogger(__name__)


class StockInfo:
    def __init__(self ):
        self.symbollist = self.loadsymbols()
        self.size = len(self.symbollist)
        logger.info('User sample file' + str(self.size))

    def loadsymbols(self):

        unimap = {}
        idxmap_nasdaq, usrlist_nasdaq = self.loadsymbols_nasdaq()
        idxmap, usrlist = self.loadsymbols_other()

        symbollist=[]
        idx = idxmap_nasdaq['Symbol']
        idxEFT = idxmap_nasdaq['ETF']
        for s in usrlist_nasdaq:
            if s[idxEFT] == "N" and s[idx] not in unimap:
                symbollist.append(s[idx])
                unimap[s[idx]] = 1

        idx = idxmap['ACT Symbol']
        idxEFT = idxmap['ETF']
        for s in usrlist:
            if s[idxEFT] == "N" and s[idx] not in unimap:
                symbollist.append(s[idx])
                unimap[s[idx]] = 1

        return symbollist
    def loadsymbols_nasdaq(self):
        nasdafile =  samplepath + '/nasdaqtraded.txt'
        iC = 1
        idxmap={}
        usrlist=[]
        with open(nasdafile, "r") as text_file:
                whole = text_file.readlines()
                for line in whole:
                    tmp = line.rstrip().split('|')
                    if iC == 1:  # read header for idx field
                        idx = 0;
                        for token in tmp:
                            idxmap[token] = idx
                            idx += 1
                        iC += 1
                        continue
                    usrlist.append(tmp)
        return idxmap, usrlist

    def loadsymbols_other(self):
        nasdafile =  samplepath + '/otherlisted.txt'
        iC = 1
        idxmap={}
        usrlist=[]
        with open(nasdafile, "r") as text_file:
                whole = text_file.readlines()
                for line in whole:
                    tmp = line.rstrip().split('|')
                    if iC == 1:  # read header for idx field
                        idx = 0;
                        for token in tmp:
                            idxmap[token] = idx
                            idx += 1
                        iC += 1
                        continue
                    usrlist.append(tmp)
        return idxmap, usrlist


