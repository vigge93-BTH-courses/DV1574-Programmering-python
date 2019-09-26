import time

year = input('What year were you born?')
month = input('What month?')
day = input('What day?')

age = time.strptime('{} {} {}'.format(year, month, day), '%Y %m %d')

age_seconds = time.mktime(age)
now_seconds = time.time()

time_diff = now_seconds - age_seconds

print('You are {} seconds old'.format(int(time_diff)))
# print('OK, then you will turn {} on {} {} in 2019!'.format(
#     2019-int(year), month, day))
