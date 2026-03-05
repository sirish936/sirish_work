s= {'name':'sirish','phno':[12345,67890]}
print(type(s))
print(s)
print("length of dict s is : {}".format(len(s)))
print(s["name"])
print(s.keys())
print(type(s.keys()))
print(s.values())
print(type(s.values()))
print(s.items())
print(s.pop('phno'))
print(s)
s.update({'city':'bang'})
print(s)

print('Hello')

assert ('name' in s and s['name'] is not None)

for i in s:
    print(i)

s.clear()
print(s)

import calendar
import collections
# from collections import OrderedDict
# from collections import *

temp=[36,41,39,43,46]
days = list(calendar.day_abbr)
day = list(calendar.day_name)
print('Hello')
print(type(days))
del days[-2:]
print(type(temp))
print(days)
print(day)
months = list(calendar.month_abbr)
month = months[1:]
print(months)
print(month)
lv_temps_wk = dict(zip(days, temp))
ordered_lv_temps_wk = collections.OrderedDict(zip(days, temp))
# ordered_lv_temps_wk = OrderedDict(zip(days, temp))
print("Dictionary values are:",lv_temps_wk)
print(ordered_lv_temps_wk)

actions = list()
print(type(actions))
actions.append({})
print(type(actions))
actions[0]["action"] = "PowerOnServer"
print(actions[0])
print(type(actions[0]))
request = {}
print(type(request))
request["verb"] = "performAction"
request["actions"] = actions
print(request)