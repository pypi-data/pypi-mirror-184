# FifeUtil
Package of Python utilities I find handy.

[FifeUtil](https://github.com/jmfife/fifeutil) is the place to keep utilities that I would like to re-use 
across projects.

## Installation

To install directly from GitHub:
```
python3 -m pip install "git+https://github.com/jmfife/fifeutil.git"
```

If you have cloned or forked the repo already to your local directory and want to use it in live (editable mode):
```
python3 -m pip install -e "."
```

## Quickstart

Install the package from GitHub:
```
python3 -m pip install "git+https://github.com/jmfife/fifeutil.git"
```

Now we see an example of using the one of the timer utilities that synchronizes events with the hour.
First run the Python interpreter, then:
```
>>> from fifeutil import timing
>>> timer1 = timing.TimerSyncHour(3600/5)
>>> import datetime
>>> def printtime():
...     print(datetime.datetime.now())
... 
>>> timer1.triggercallback(printtime)
2020-05-31 17:25:10.001249
2020-05-31 17:25:15.001348
2020-05-31 17:25:20.000543
2020-05-31 17:25:25.000405
```
We see the timer triggering at 5-second intervals synchronized with the top of the hour and with the 
minute in this case.

