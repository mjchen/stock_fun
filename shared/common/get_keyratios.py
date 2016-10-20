__author__ = 'mingjun'

from urllib import request
import csv
# key ratios
#HEAD = "http://financials.morningstar.com/ajax/exportKR2CSV.html?&callback=?&t=XNAS:"
#TAIL = "&region=usa&culture=en-US&cur=&order=asc"


#http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XNAS:EXPE
#&region=usa&culture=en-US&cur=&reportType=cf&period=3&dataType=A&order=asc&columnYear=5&rounding=3&view=raw&r=540799&denominatorView=raw&number=3

# cash flows
HEAD = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XNAS:"
TAIL = "&region=usa&culture=en-US&cur=&reportType=cf&period=12&dataType=A&order=asc&columnYear=5&rounding=3&view=raw&r=195836&denominatorView=raw&number=3"

def getkeyratio_csv(symbol):


    url = HEAD + symbol + TAIL
    response = request.urlopen(url)
    csvstring= response.read()
    # Save the string to a file
    csvstr = str(csvstring).strip("b'")

    lines = csvstr.split("\\n")
    for l in lines:
        print(l)

getkeyratio_csv('EXPE')
