"""
to simulate a progress bar
"""
import sys,time

for i in range(5):
    #sys.stdout.write(' '*10+'\r')
    #sys.stdout.flush()
    #print i
    #sys.stdout.write('{0}/5r'.format(i+1))
    #sys.stdout.write(str(i)*(5-i) + '\r')
    #sys.stdout.flush()
    sys.stdout.write('###')
    sys.stdout.flush()
    time.sleep(1)

print
