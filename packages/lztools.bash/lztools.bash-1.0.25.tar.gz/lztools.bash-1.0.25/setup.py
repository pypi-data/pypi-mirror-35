#!/usr/bin/env python3.7
from setuptools import setup
from subprocess import call
from setup_requires import apt_requires, pip_requires
call(["sudo", "apt-get", "-qq", "-y", "install", *apt_requires])

# try:
#     codecs.lookup('mbcs')
# except LookupError:
#     ascii = codecs.lookup('ascii')
#     func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
#     codecs.register(func)

setup(
    name='lztools.bash',
    author='Laz aka Zanzes',
    author_email='ubuntuea@gmail.com',
    version='1.0.25',
    license='MIT License',
    description='A collection of useful utilities by Laz aka Zanzes',
    url='',
    entry_points={
        'console_scripts': [
            'lmod = cli.lmod:main',
            'ldoc = cli.ldock:main',
            'lgit = cli.lgit:main',
            'lpy  = cli.lpy:main'
        ],
    },
    install_requires=pip_requires,
    packages=['lztools', 'cli'],
    zip_safe=False,
    include_package_data=True,
    package_data={'lztools.bash': ['resources/*']},
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

