from .micral_utils import printDict, removeEmptyDict, formatInput, loadData, checkParameter

from os.path import realpath, dirname
def version():
	try:
		with open(dirname(realpath(__file__))+'version.txt') as f:
			return f.read()
	except:
		return "0.0.0"