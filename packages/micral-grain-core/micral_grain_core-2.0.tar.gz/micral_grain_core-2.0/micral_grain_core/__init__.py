from .micral_grain_core import grainSeparatorCore

from os.path import realpath, dirname
def version():
	try:
		with open(dirname(realpath(__file__))+'version.txt') as f:
			return f.read()
	except:
		return "0.0.0"

def analyse(images, plot=True, plotFull=False, plotDetails=None, parameters=None):
    return grainSeparatorCore(images, plot, plotFull, plotDetails, parameters)