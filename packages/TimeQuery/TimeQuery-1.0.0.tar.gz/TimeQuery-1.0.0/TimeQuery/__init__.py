import datetime
import zoneinfo
import zoneinfo._tzpath as tzpath

# TimeQuery

'''
See PyPi page for docs.
By Pigeon Nation
'''

author = 'Pigeon Nation'
version = '1.0.0'

timezone_conversions = {
    'UTC': datetime.timezone.utc
}

time_formats = {
    # Day-Month-Year
    ## Time-Inc
    'dmy date 12hr apm zone': '%d/%m/%Y %I:%M:%S%p %Z',
    'dmy date 24hr zone': '%d/%m/%Y %H:%M:%S %Z',
    'dmy date 12hr apm': '%d/%m/%Y %I:%M:%S%p',
    'dmy date 24hr': '%d/%m/%Y %H:%M:%S',
    ## No-Time
    'dmy date': '%d/%m/%Y',
    'dmy date zone': '%d/%m/%Y %Z',
    
    # Year-Month-Day
    ## Time-Inc
    'ymd date 12hr apm zone': '%Y/%m/%d %I:%M:%S%p %Z',
    'ymd date 24hr zone': '%Y/%m/%d %H:%M:%S %Z',
    'ymd date 12hr apm': '%Y/%m/%d %I:%M:%S%p',
    'ymd date 24hr': '%Y/%m/%d %H:%M:%S',
    ## No-Time
    'ymd date': '%Y/%m/%d',
    'ymd date zone': '%Y/%m/%d %Z',
    
    # Month-Day-Year
    ## Time-Inc
    'mdy date 12hr apm zone': '%m/%d/%Y %I:%M:%S%p %Z',
    'mdy date 24hr zone': '%m/%d/%Y %H:%M:%S %Z',
    'mdy date 12hr apm': '%m/%d/%Y %I:%M:%S%p',
    'mdy date 24hr': '%m/%d/%Y %H:%M:%S',
    ## No-Time
    'mdy date': '%m/%d/%Y',
    'mdy date zone': '%m/%d/%Y %Z',
    
    # Time Only
    '12hr apm': '%I:%M:%S%p',
    '24hr': '%H:%M:%S',
    '12hr apm zone': '%I:%M:%S%p %Z',
    '24hr zone': '%H:%M:%S %Z',
    '24hr / 12hr apm': '%I:%M:%S%p/%H:%M:%S',
    '24hr / 12hr apm zone': '%I:%M:%S%p/%H:%M:%S %Z',
    
    # Special - "All"
    'all dmy': '%d/%m/%Y %I:%M:%S%p/%H:%M:%S %Z',
    'all ymd': '%Y/%m/%d %I:%M:%S%p/%H:%M:%S %Z',
    'all mdy': '%m/%d/%Y %I:%M:%S%p/%H:%M:%S %Z',
    
    # Timezone [Special]
    'tz': '%Z'
}




def now_in(cont):
    return zoneinfo.ZoneInfo(cont)

def now(time_zone=datetime.timezone.utc, timestr=time_formats['all dmy']):
    #timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    now = datetime.datetime.now(time_zone)
    return now.strftime(timestr) #12-hour format

def tzfold():
    return tzpath.TZPATH

# Quick Test.
test = lambda: print(now(now_in(input('Country > ')), time_formats[input('Disp > ')]))
if __name__ == '__main__': test()