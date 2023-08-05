"""
Code here performs calculations on data from ABF objects.
"""
import numpy as np


def sweepNumbersByTime(abf, timeSec1, timeSec2):
    """
    Returns a list of sweeps containing data between the two times.
    """
    raise NotImplementedError
    return [1, 2, 3]


def averageSweep(abf, sweepNumbers=None, baselineTimeSec1=False, baselineTimeSec2=False, calculateError=False, stdErr=True):
    """
    Returns the average of the given sweeps.
    This returns a whole sweep, not just a single number.
    If you want baseline subtraction, call abf.baseline() before this.
    If calculateError is true, the returned data is [sweepAvg, sweepErr].
    """
    if sweepNumbers is None:
        sweepNumbers = abf.sweepList
    sweepAvg = np.empty((len(sweepNumbers),len(abf.sweepY)))
    for sweep in sweepNumbers:
        abf.setSweep(sweep)
        sweepAvg[sweep] = abf.sweepY
    sweepAvg = np.average(sweepAvg, 0)
    if calculateError:
        sweepErr = np.std(sweepAvg, 0)
        if stdErr:
            sweepErr = sweepErr / np.sqrt(len(sweepNumbers))
        return [sweepAvg, sweepErr]
    else:
        return sweepAvg


def averageValue(abf, timeSec1, timeSec2, sweepNumbers=None, channel=0, calcError=False, stdErr=True):
    """
    Return the average between two time points for the given sweeps.
    If calcError is True, return [AV, ERR].
    """
    if sweepNumbers is None:
        sweepNumbers = abf.sweepList
    sweepNumbers = list(sweepNumbers)
    assert len(sweepNumbers) > 0

    avs = np.full(len(sweepNumbers), np.nan)
    ers = np.full(len(sweepNumbers), np.nan)

    for sweepNumber in sweepNumbers:
        abf.setSweep(sweepNumber=sweepNumber, channel=channel)
        avs[sweepNumber] = abf.sweepAverage(timeSec1, timeSec2)
        if calcError:
            ers[sweepNumber] = abf.sweepError(timeSec1, timeSec2, stdErr)
    if calcError and stdErr:
        ers = ers / np.sqrt(len(sweepNumbers))

    if calcError:
        return [avs, ers]
    else:
        return avs
