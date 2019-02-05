#!/usr/bin/env python3

import random
import time
import datetime


foo = [
	'Peter Jenkins',
	'Jayden Sutton',
	'Ewan Richardson',
	'Luca Cox',
	'Freddie Morris',
	'Brent Phillips',
	'Cristian Castaneda',
	'Elian Gallegos',
	'Alec Hooper',
	'Osvaldo Michael'
]

for x in range(1234):
	print("{0} - {1}".format(datetime.datetime.now().time(), random.choice(foo)), flush=True)
	time.sleep(0.01)