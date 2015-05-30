'''
Created on Jan 3, 2014

@author: xorduna
'''

from mixpanel import Mixpanel
import math

class MixSwissKnife(object):
    
    def __init__(self, api_key, api_secret, period_threshold = 1, usage_threshold = 1, where = "true", period = "week"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api = Mixpanel(self.api_key, self.api_secret)
        #self.users = []
        self.daily_threshold = period_threshold
        self.usage_threshold = usage_threshold
        self.where = where
        self.period = period
        self.user_data = {}
        pass
    
    def track_users_feature(self, feature, from_date, to_date):
        data = self.api.request(['segmentation'], {
            'event' : feature,
            'on': 'properties["username"]',
            'where': self.where,
            'from_date': from_date,
            'to_date': to_date,
            'unit' : self.period,
            'type': 'general',
            'limit': 1000
        })
        
        print data
        user_data = data['data']['values']

        for user in user_data:

            days = 0
            for d in user_data[user]:
                if user_data[user][d] > self.daily_threshold:
                    days = days + 1

            total_days = len(user_data[user])
            
            usage = float(days * 100) / total_days
            #print user, ' --> ', "%0.2f" % usage , '%'

            #if user not in self.users:
            #    self.users.append(user)
            
            if usage > 0:
                if not self.user_data.has_key(user):
                    self.user_data[user] = {}
                self.user_data[user][feature] = usage

    '''
        How many users use a feature?
    '''
    def analyze_feature(self, feature):
        users = 0
        frequency = []
        for user in self.users():
            user_info = self.user_data[user]
            if user_info.has_key(feature) and user_info[feature] > self.usage_threshold:
                users = users + 1
                frequency.append(user_info[feature])
        usage = float(users) * 100 / len(self.users())
        
        #print users, 'out of', len(self.users())
        #print frequency
        #print self.mean(frequency), '[', max(frequency), ',', min(frequency), ']'
        
        #lets calculate frequency
        
        return usage, self.mean(frequency)
        
    def num_users(self):
        return len(self.user_data.keys())
    
    def users(self):
        return self.user_data.keys()
    
    def mean(self, l):
        return float(sum(l))/len(l) if len(l) > 0 else float('nan')

    def median(self, l):
        sorts = sorted(l)
        length = len(sorts)
        if not length % 2:
            return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
        return sorts[length / 2]
if __name__ == '__main__':
    
    msk = MixSwissKnife(api_key = 'API_KEY', api_secret = 'API_SECRET')
    
    features = ['consumption', 'cost', 'dashboard', 'mvp', 'evolution', 'bydevice', 'reports', 'alerts', 'query', 'billing', 'export excel', 'reactive']
    #features = ['consumption', 'cost', 'dashboard', 'mvp', 'evolution']
    
    for feature in features:    
        msk.track_users_feature(feature, '2013-10-01', '2014-01-02')
        #print len(msk.users)
        pass

    print 'there are ', msk.num_users(), 'qualified users'

    i = 0
    for user in msk.users():
        print i, user, ':', msk.user_data[user]
        i = i + 1

    for feature in features:
        #print '=====', feature,'====='
        usage, frequency = msk.analyze_feature(feature)
        print feature, '--> u:', usage, 'f:', frequency 
    
     #for feature in features:
     #   msk.track_feature(feature, '2013-11-01', '2014-01-02')
     
    #msk.track_feature("consumption", '2013-11-01', '2014-01-02')
    
'''

 steps

- count how many days a users uses a feature more than threshold
- store this information by feature and user
- set boundaries for often, more often in terms of %? start by 25 % ?
- set boundaries for everybody, some ofthem in terms of % ?

'''

        
    
