from datetime import datetime
'''Use Python to compute days between start and stop date.'''

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

delta = datetime.strptime(date_stop, '%m-%d-%Y') - datetime.strptime(date_start, '%m-%d-%Y')
print delta
print delta.days
# Response: 937 days, 0:00:00
# 937


####b)
date_start = '12312013'
date_stop = '05282015'
delta = datetime.strptime(date_stop, '%m%d%Y') - datetime.strptime(date_start, '%m%d%Y')
print delta
print delta.days
# Response: 513 days, 0:00:00
# 513

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
delta = datetime.strptime(date_stop, '%d-%b-%Y') - datetime.strptime(date_start, '%d-%b-%Y')
print delta
print delta.days
# Response: 7850 days, 0:00:00
# 7850

