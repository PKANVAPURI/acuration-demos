""" nsetools is a library for collecting real time data from National Stock Exchange of India. 
It can be used in various types of projects which requires fetching live quotes for a given stock or index or building large data sets for further data analytics. 
We can also build command line interface applications which can provide us live market details at a blazing fast speeds, much faster than any browser. 
The accuracy of data is only as correct as provided on http://www.nseindia.com """

pip install nsetools
# importing nse from nse tools
from nsetools import Nse
# creating a Nse object
nse = Nse()
# printing Nse object
print(nse)

# OUTPUT - Driver Class for National Stock Exchange (NSE)

# importing nse from nse tools
from nsetools import Nse
# creating a Nse object
nse = Nse()
# getting quote of the sbin
quote = nse.get_quote('sbin')
# printing company name
print(quote['companyName'])
# printing buy price
print("Buy Price : " + str(quote['buyPrice1']))

# OUTPUT - State Bank of India
#          Buy Price : 191.45

# importing nse from nse tools
from nsetools import Nse
# creating a Nse object
nse = Nse()
# getting quote of the sbin
quote = nse.get_quote('sbin')
# printing company name
print(quote['companyName'])
# printing average price
print("Average Price : " + str(quote['averagePrice']))

# OUTPUT - State Bank of India
#          Average Price : 193.9
