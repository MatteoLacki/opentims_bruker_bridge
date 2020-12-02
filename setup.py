# This Python file uses the following encoding: utf-8
from setuptools import setup, find_packages

setup(  name='opentims_bruker_bridge',
        packages=find_packages(),
        version='1.0.1',
        description='Bruker dll and so files.',
        long_description='Files needed to run conversion: time of flight to mass over charge and scan number to drift time.',
        author='MatteoLacki',
        author_email='matteo.lacki@gmail.com',
        url='https://github.com/MatteoLacki/opentims_bruker_bridge.git',
        keywords=['Great module', 'Devel Inside'],
        classifiers=['Development Status :: 1 - Planning',
                     'License :: OSI Approved :: BSD License',
                     'Intended Audience :: Science/Research',
                     'Topic :: Scientific/Engineering :: Chemistry',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7'],
	package_dir={'opentims_bruker_bridge':'opentims_bruker_bridge'},
        package_data = {'opentims_bruker_bridge':
                [
                    'win32/timsdata.dll',
                    'win64/timsdata.dll',
                    'libtimsdata.so'
                ]},
        zip_safe=False
)
