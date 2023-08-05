from .micral_summary import summaryImage

from os.path import realpath, dirname
def version():
	try:
		with open(dirname(realpath(__file__))+'version.txt') as f:
			return f.read()
	except:
		return "0.0.0"

def summary(data):
    return summaryImage(data)