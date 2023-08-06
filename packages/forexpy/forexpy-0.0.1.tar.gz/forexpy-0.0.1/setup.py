from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Forex trading with python'
LONG_DESCRIPTION = 'Backtesting on historical data or live trading'

# Setting up
setup(
    name="forexpy",
    version=VERSION,
    author="Carlos Lorenzo",
    author_email="<clorenzozuniga@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'mplfinance', 'pyaudio'],
    keywords=['python', 'forex', 'trading', 'backtesting', 'finance'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)