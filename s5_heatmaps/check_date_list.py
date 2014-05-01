import pandas as pd
from datetime import date, timedelta as td

# 1) Open csv file, read list of dates from file
df = pd.read_csv('mtl-bike-2013.csv')
df_list = df['Date'].tolist()

# 2) Make list of dates from Jan 1 2013 to Dec 31 2013
d1 = date(2013,1,1)
d2 = date(2013,12,31)
delta = d2 - d1

date_list = []
for i in range(delta.days + 1):
    tmp = d1 + td(days=i)
    date_list += [tmp.strftime('%d/%m/%Y')]  # same format of in csv file
   
print
print 'Number of days in 2013: '+str(len(date_list))

# 3) Loop through both list, make list of missing dates
missing = []
for i in range(len(date_list)):
    if i>= len(df_list) or date_list[i]!=df_list[i]:
        missing+=[date_list[i]]


print 'first missing value: '+str(missing[0])

print 'last date in csv file: '+str(df_list[-1])
