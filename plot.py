'''
Created on Jan 7, 2014

@author: xorduna
'''

import matplotlib.pyplot as plt
from datetime import datetime

from swissknife import MixSwissKnife

where_clause = 'properties["partner"]=="Satel Spain" or properties["partner"]=="Pointverde" or properties["partner"]=="UPCnet" or properties["partner"]=="PGIGrup" or properties["partner"]=="Optima Group"' 

msk = MixSwissKnife(api_key = '3b0436edbe3fdb3eda75083e5d66301c', api_secret = '7dc6dcd26210e8dce661e4db3ec8c741', period_threshold = 2, period = 'day')
features = ['consumption', 'cost', 'dashboard', 'mvp', 'evolution', 'bydevice', 'reports', 'alerts', 'query', 'billing', 'export excel', 'reactive', 'passive']



start = datetime(2014, 1, 1)
end = datetime(2015, 4, 1)

while end > start:
	print 'working on ', start, '->', end
	if start.month == 12:
		next_month = datetime(start.year+1, 1, 1)
	else:
		next_month = datetime(start.year, start.month+1, 1)

	for feature in features:    
	    msk.track_users_feature(feature, start.strftime("%Y-%m-%d"), next_month.strftime("%Y-%m-%d"))

	print 'there are ', msk.num_users(), 'qualified users'

	plt.xlabel("users")
	plt.ylabel("frequency")
	#plt.axis([0.0, 100, 0, 100])

	for feature in features:
	    usage, frequency = msk.analyze_feature(feature)
	    print feature, '--> u:', usage, 'f:', frequency
	    plt.plot(usage, frequency, 'o')
	    plt.text(usage + 1, frequency - 0.5, feature)
	    


	plt.savefig('sak-'+start.strftime("%Y-%m")+'.png')
	plt.clf()
	start = next_month