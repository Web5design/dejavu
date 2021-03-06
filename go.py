from dejavu.control import Dejavu
from ConfigParser import ConfigParser
import warnings
warnings.filterwarnings("ignore")

# load config
config = ConfigParser()
config.read("dejavu.cnf")

# create Dejavu object
dejavu = Dejavu(config)
dejavu.fingerprint("va_us_top_40/mp3", "va_us_top_40/wav", [".mp3"], 5)

# recognize microphone audio
from dejavu.recognize import Recognizer
recognizer = Recognizer(dejavu.fingerprinter, config)

# recognize song playing over microphone for 10 seconds
song = recognizer.listen(seconds=5, verbose=True)
print song