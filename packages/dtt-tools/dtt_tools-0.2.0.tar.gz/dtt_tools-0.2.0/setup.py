from setuptools import setup

setup(
    name='dtt_tools',
    version='0.2.0',
    author = 'Patrick Godwin',
    author_email = 'patrick.godwin@ligo.org',
    description = 'script utilities related to DTT software',
    url = 'https://git.ligo.org/patrick.godwin/dtt_tools',
    scripts = ['bin/dtt2tfplot'],
    install_requires = [
        'dtt2hdf',
        'matplotlib',
        'numpy',
    ]
)
