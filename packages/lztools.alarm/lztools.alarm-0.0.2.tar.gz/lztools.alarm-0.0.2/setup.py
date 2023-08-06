#!/usr/bin/env python3.7
import codecs
from subprocess import call

from setuptools import setup

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

call(["sudo", "apt-get", "-qq", "-y", "install", "sox"])

setup(
    name='lztools.alarm',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='0.0.2',
    license='MIT License',
    description='A collection of useful utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙',
    url='',
    requires=["lztools"],
    entry_points={
        'console_scripts': [
            'alarm = cli.alarm:main',
        ],
    },
    packages=['cli'],
    zip_safe=False,
    include_package_data=True,
    package_data={'alarm': ['resources/*']},
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Systems Administration',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],
)

