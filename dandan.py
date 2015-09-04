from Parser import *
import Loader
import sys
from InternalStateProvider import *

if len(sys.argv) > 1:
	fileName = sys.argv[1]

	code = Loader.Load(fileName)

	stateProvider = InternalStateProvider()
	parser = Parser(stateProvider)

	parser.parse(code)