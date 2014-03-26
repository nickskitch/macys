#!/usr/bin/env python

from datetime import datetime, timedelta
tm = datetime.now() + timedelta(hours=2, minutes=40)
#print "Back up around " + '{:%I:%M%p}'.format(nine_hours_from_now)

tm = tm - timedelta(minutes=tm.minute % 10,
                             seconds=tm.second,
                             microseconds=tm.microsecond)

print "Back up around " + '{:%I:%M%p}'.format(tm)
