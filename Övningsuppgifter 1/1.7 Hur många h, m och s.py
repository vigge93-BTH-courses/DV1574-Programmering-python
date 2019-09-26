time = int(input('How many seconds? '))

if time < 0:
    exit(1)

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60

hours = time // SECONDS_PER_HOUR

remaining = time % SECONDS_PER_HOUR

minutes = remaining // SECONDS_PER_MINUTE

seconds = remaining % SECONDS_PER_MINUTE

print('{} seconds are {} hour(s), {} minute(s) and {} second(s)'.format(
    time, hours, minutes, seconds))
