from setuptools import setup

setup(
    name='dtt_tools',
    version='0.1',
    author = 'Patrick Godwin',
    author_email = 'patrick.godwin@ligo.org',
    url = 'https://git.ligo.org/patrick.godwin/dtt_tools',
    scripts = ['bin/dtt2tfplot'],
    install_requires = [
        'dtt2hdf',
        'matplotlib',
        'numpy',
    ]
)
