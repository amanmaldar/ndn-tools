import subprocess

 #a nfdc route add /ndn/d-site/d 261

print "Loading FIB Entries"
for i in range(0,1000):
    bashCommand = "nfdc route add /ndn/d-site/d/"+str(i)+" "
    output = subprocess.check_output(['bash', '-c', bashCommand])

print "1000 Fib Entries Loaded"

exit()


#!/bin/bash
print "Starting the pings"
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 1 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 1 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 1/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt "
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 2/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt "
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 3/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 4/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 5/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 6/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 7/8"

bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 120001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
bashCommand = "ndnping /ndn/d-site/d -i 1 -c 5000 -n 120001 > /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
output = subprocess.check_output(['bash', '-c', bashCommand])
print "Finshed 100%"

print "Get the results"




