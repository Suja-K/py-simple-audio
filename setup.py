#from distutils.core import setup, Extension
from setuptools import setup, Extension
import sys

if sys.platform == 'darwin':
    platform_audio = 'simpleaudio_mac.c'
    platform_mutex = 'posix_mutex.c'
    platform_libs = ['CoreAudio']
else:
    pass
    # define a compiler macro for unsupported ?
    
simpleaudio_module = Extension(
    'simpleaudio', 
    sources=['simpleaudio.c', platform_audio, platform_mutex],
    extra_link_args=['-framework', 'AudioToolbox'])

setup(name = 'simpleaudio',
    version = '1.0',
    description = """The simpleaudio package contains the simpleaudio module 
                     which makes playing wave files in Python very simple.""",
    test_suite="tests",
    ext_modules = [simpleaudio_module])
