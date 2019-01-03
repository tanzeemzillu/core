import json
import subprocess

json_key={}


def network():
	output= subprocess.Popen(["netengine-utils ifconfig"], shell=True, stdout=subprocess.PIPE).communicate()[0]
    	print(output)

if __name__=="__main__":

    network()
