"""
sanic-motor
--------------
Simple Motor wrapper for sanic
"""
import os
import platform
from setuptools import setup
import sanic_motor

if platform.system().startswith('Windows'):
    os.environ['SANIC_NO_UVLOOP'] = 'yes'

setup(
    name='sanic-motor',
    version=sanic_motor.__version__,
    url='https://github.com/lixxu/sanic-motor',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple Motor wrapper for sanic',
    long_description=__doc__,
    packages=['sanic_motor'],
    zip_safe=False,
    platforms='any',
    install_requires=['motor>=2.0', 'sanic>=0.4.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
