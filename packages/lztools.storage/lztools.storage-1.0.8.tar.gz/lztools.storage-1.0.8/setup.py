#!/usr/bin/env python3.7
import codecs
from setuptools import setup
from resources.packs import pip_requires

try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

setup(
    name='lztools.storage',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.0.8',
    license='MIT License',
    description='Template',
    url='',
    entry_points={
        'console_scripts': [
            'lstorage = cli.lstorage:main'
        ],
    },
    install_requires=pip_requires,
    packages=['cli'],
    zip_safe=False,
    include_package_data=True,
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

