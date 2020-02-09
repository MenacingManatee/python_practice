#!/usr/bin/python
import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
print 'Your script can\'t be stopped with CTRL+C'
while 1:
    continue
