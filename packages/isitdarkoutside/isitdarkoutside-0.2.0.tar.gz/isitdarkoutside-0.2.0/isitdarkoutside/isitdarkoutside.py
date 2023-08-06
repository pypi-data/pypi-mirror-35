import geocoder
from urllib import urlopen
import datetime
from dateutil import tz

def checkifdarkoutside():

    g = geocoder.ip('me')
    h = geocoder.google(g.latlng, method='reverse')

    response = urlopen("http://api.sunrise-sunset.org/json?lat=%s&lng=%s&formatted=0" % (h.latlng[0], h.latlng[1]))
    timestring = response.read()

    utcsunrise = timestring[34:39]
    utcsunset = timestring[71:76]

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    now = datetime.datetime.now()

    localsunrise = datetime.datetime.strptime(str(utcsunrise), '%H:%M')
    localsunset = datetime.datetime.strptime(str(utcsunset), '%H:%M')
    localsunrise = localsunrise.replace(tzinfo=from_zone, year=now.year, month=now.month, day=now.day)
    localsunset = localsunset.replace(tzinfo=from_zone, year=now.year, month=now.month, day=now.day)

    sunrisecentral = localsunrise.astimezone(to_zone)
    sunsetcentral = localsunset.astimezone(to_zone)

    #c_rise = list(str(sunrisecentral))
    #c_set = list(str(sunsetcentral))

    #print "Sunrise is at %s " % ''.join(c_rise[:-6])
    #print "Sunset is at %s " % ''.join(c_set[:-6])

    if now > sunrisecentral.replace(tzinfo=None):
        if now < sunsetcentral.replace(tzinfo=None):
            print "Nope, it isn't."

        elif now > sunsetcentral.replace(tzinfo=None):
            print "Yes, it is."

        elif now == sunsetcentral.replace(tzinfo=None):
            print "It's sunset."

        else:
            pass

    elif now < sunrisecentral.replace(tzinfo=None):
        print "Yes, it is."

    elif now == sunrisecentral.replace(tzinfo=None):
        print "It's sunrise."

    else:
        pass

checkifdarkoutside()
