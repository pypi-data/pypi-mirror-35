from .micral_harmonic import harmonicMeasurement

from os.path import realpath, dirname
def version():
	try:
		with open(dirname(realpath(__file__))+'/version.txt') as f:
			return f.read()
	except:
		return "0.0.0"

def analyse(images, plot=False, plotTimeline=None):
    return harmonicMeasurement(images, plot, plotTimeline)