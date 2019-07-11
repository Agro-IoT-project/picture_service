import schedule
import time 
import json
import os
import requests 
import glob

url = 'http://10.64.45.54:3000/pictures'

def photo(captureTime, cams, fieldName):
	for cam_i in cams:
		os.system('./root/services/cams/%s/webcam.sh' %cam_i)
		dataParams, files = data(captureTime, cam_i, fieldName)
		r = requests.post(url=url, files=files, data=dataParams)

def data(captureTime, camName, fieldName):
	params = {
		"field": fieldName,
		"camera": camName,
		"time": captureTime
	}

	filename = glob.glob('/root/services/cams/%s/img/*.jpg' %camName)
	files = {
		"image": open(filename[0], 'rb')
	}
	return params, files

try:
	script_dir = os.path.dirname(os.path.abspath(__file__))
	print script_dir

	# read file
	with open(script_dir + '/config.json', 'r') as myfile:
		dataStore=myfile.read()

	# parse file
	obj = json.loads(dataStore)

	# avaliable cameras
	cams = os.listdir(script_dir +'/cams/')

	# create schedulers for every time 
	for t in obj['time']:
		schedule.every().day.at(str(t)).do(photo, str(t), cams, obj['field'])

	while True:
		schedule.run_pending()
		time.sleep(1)

except KeyboardInterrupt:
	print "Kill takephoto code !!"