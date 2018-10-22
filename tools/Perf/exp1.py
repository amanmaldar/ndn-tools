import subprocess

bashCommand = []
showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1"

echo "Starting the pings"
bashCommand[0] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 1"
bashCommand[1] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001"
bashCommand[2] = " ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001"
bashCommand[3] = " ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001"
bashCommand[4] = " ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001"
bashCommand[5] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001"
bashCommand[6] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001"

for in in range (0,7):
	output = subprocess.call(['bash', '-c', bashCommand[i]])
	output = subprocess.call(['bash', '-c', showCommand])
	print "done",i,"/7"

print "Get the results"




