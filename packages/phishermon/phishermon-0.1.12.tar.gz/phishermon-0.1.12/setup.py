import platform
from setuptools import setup

# Base dependencies for all platforms
install_requires = ['python-evtx', 'xmltodict', 'electus']

if platform.system() == 'Windows':
    install_requires.append(['psutil', 'easygui', 'pywintrace'])

setup(name='phishermon',
      version='0.1.12',
      description='A tool to create and take action on behavioural signatures from sysmon data.',
      url='https://gitlab.com/gclenden/phishermon',
      author='Graham Clendenning',
      author_email='graham.clendenning@uoit.net',
      license='MIT',
      packages=['phishermon'],
      entry_points={'console_scripts':['phishermon=phishermon.commandline:phishermon_cmdline', 
                                       'sysmon-parser=phishermon.commandline:sysmon_parser_cmdline']},
      install_requires = install_requires,
      classifiers = ["Natural Language :: English",
            'Development Status :: 4 - Beta',
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6"],
      zip_safe=False)