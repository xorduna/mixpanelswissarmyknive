'''
Created on Jan 7, 2014

@author: xorduna
'''

from swissknife import MixSwissKnife
from plotsk import CharPlot

msk = MixSwissKnife(api_key = '3b0436edbe3fdb3eda75083e5d66301c', api_secret = '7dc6dcd26210e8dce661e4db3ec8c741')
features = ['consumption', 'cost', 'dashboard', 'mvp', 'evolution', 'bydevice', 'reports', 'alerts', 'query', 'billing', 'export excel', 'reactive']

for feature in features:    
    msk.track_users_feature(feature, '2013-10-01', '2014-01-01')

print 'there are ', msk.num_users(), 'qualified users'

#for user in msk.users():
#    print user, ':', msk.user_data[user]

plot = CharPlot(50, 50)

alfa = "abcdefghijklmnopqrstuvwxyz"
i = 0
for feature in features:
    usage, frequency = msk.analyze_feature(feature)
    print alfa[i], feature, '--> u:', usage, 'f:', frequency
    plot.put(int(usage) / 2, int(frequency) / 2, alfa[i])
    i = i + 1

plot.print_chart()