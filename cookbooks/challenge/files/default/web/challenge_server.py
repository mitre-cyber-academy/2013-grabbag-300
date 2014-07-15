#!/usr/bin/python
from bottle import route, run, template, error, static_file, template
import os
import random

#TODO Update this to the appropriate static directory
staticDir = '/opt/challenge/static/'
capDir = os.path.join(staticDir, os.path.join('img', 'captains'))

ships =['USS Enterprise NCC-1701', 
	'USS Enterprise NCC-1701-D',
	'USS Voyager, NCC-74656',
	'Enterprise NX-01',
	'Deep Space 9']

@route('/')
@route('/index.php')
def index():
	capPaths = os.listdir(capDir)
	capPaths = [os.path.join('/static/img/captains/', path) for path in capPaths]
	random.shuffle(capPaths)
	random.shuffle(ships)
	return template('page', caps=capPaths, ships=ships)

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root=staticDir)

@error(404)
def error404(error):
	return "Beam me up, Scotty. There's no life on this planet."

#TODO update the host
#run(host='localhost', port=80, debug=True, reloader=True)
run(host='0.0.0.0', port=80)
