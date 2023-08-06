import matplotlib
from operator import itemgetter, attrgetter
import numpy as np
from numpy import linspace
from numpy.polynomial.polynomial import polyfit
from numpy.random import normal
from math import *
from random import random
from multiprocessing import Pool as ThreadPool
#from multiprocessing.dummy import Pool as ThreadPool 
from itertools import repeat
import sys, resource, json
import timeit
try:
    from utility import *
except Exception:
    from lgad.utility import *

#7.6*10**-4
'''
Run the simulation with a .1 radiation length for the scoring plane.
'''

THCK=THICKNESS=.00076
BE=BEAMENERGY=12500 #12.5GeV
'''
| Notes on Radiation Thickness

From arXiv:1603.09669v2,
the plates are:
 5.5e-3cm Silicon; radlen 9.37cm
 5.0e-3cm Kapton;  radlen 28.6cm
 fiberglass; radlen ___cm?
Plates are .0055/9.37 + 0.0050/28.6 = 7.6x10^-4 radlen
'''


'''
Eight plates of 300-500 micron silicon evenly spaced.
1/16" of fiberglass as the detector; with and without.


Set resolution to zero, the RMS should grow by sqrt(2)*rms(plate1);
'''
        
def getScatterRMS(radlength,velocity=BE):
    if radlength == 0: return 0
    v=velocity
    out=(13.6)/(v) * sqrt(radlength) * (1+.088*log(radlength))
    return out

def getScatterAngle(radlength, use=True):
    if use is False: return 0
    rms=getScatterRMS(radlength)
    try:
        theta=normal(0,rms)
    except Exception:
        return normal(0,0)
    return theta
#14.6MeV/p /sqrt(radlen)    
def getPosition(positions,radlens, use=True):
    track=[]
    theta=0
    previous_x=0
    y=0
    for x,radlen in zip(positions,radlens):
        d=x-previous_x
        y+=d*tan(theta)
        track.append(y)
        theta+=getScatterAngle(radlen, use)
        previous_x=x
    return track

class Result:
    def __init__(self,realTrack,measurement,score,risidual,positions):
        self.realTrack=realTrack
        self.measurement=measurement
        self.score=score
        self.risidual=risidual
        self.positions=positions


def getMeasurement(real_track, resolution):
    return [ normal(y,res) for y,res in zip(real_track,resolution) ] 

def getEvent(positions, radlengths, resolutions, testPoint, togglePlates, useCoulomb):
    realTrack   = getPosition ( positions, radlengths, useCoulomb )
    measurement = getMeasurement( realTrack, resolutions)
    score       = getTestPoint( positions, measurement, testPoint, togglePlates )
    risidual    = getRisidual ( positions, measurement, testPoint, togglePlates , realTrack)
    return Result(realTrack,measurement,score,risidual,positions)


#scoringPlane is of the type Plate.
def simulate(scoringPlane=None, events=1,plates=None, resolution=.00471, plt=None, toggle=None, title=None, use=True, threads=8):
    if plates is None:
        raise Exception("Please supply the simulation with plates using the commands loadPlateFile, getPlates")
    if toggle is None: toggle=(0,len(plates))
    #PLZ Simplify
    positions=[ plate.pos for plate in plates ]
    radlens=[ plate.radlen for plate in plates ]
    res=[ resolution for plate in plates ]
    pos=[ positions for i in range(events) ]
    # //
    sensorPosition=0
    if scoringPlane is not None: sensorPosition=scoringPlane.pos
    if scoringPlane is None:
        for plate in plates:
            if plate.isScoringPlane:
                sensorPosition=plate.pos
    params=zip(pos,repeat(radlens),repeat(res),repeat(sensorPosition),repeat(toggle),repeat(use))
    
    with ThreadPool(threads) as pool:
        results=pool.starmap(getEvent,params)
        
    #Currently debugging a lot of risidual RMS so it is prioriy;
    #Thats why simulate() retuns a tuple instead of a single object.
    risiduals = [result.risidual for result in results]
    rms=getRMS(risiduals)

    if plt is not None:
        plotSingle(results, scoringPlane, events, rms)
    return results, rms

#scoringPlane is of the type Plate.
def extractRMS(scoringPlane,results,plates,toggle,threads=8):
    if toggle is None: toggle=(0,len(plates))
    positions=[ plate.pos for plate in plates ]
    testPoint=scoringPlane.pos
    params=zip(repeat(positions),results,repeat(testPoint),repeat(toggle))
    with ThreadPool(threads) as pool:
        residuals=pool.starmap(getRisidualFromResult,params)
    return getRMS(residuals)



def plotSingle(res, scoringPlane, events, resolution):
    import matplotlib.pyplot as plt
    if scoringPlane is not None:
        sensor=scoringPlane.position
    _positions=[datum.positions for datum in res]
    _real_track=[datum.realTrack for datum in res]
    _measured_track=[datum.measurement for datum in res]
    positions=[]
    real_track=[]
    measured_track=[]

    for i in range(len(_real_track)):
        positions+=_positions[i]
        real_track+=(_real_track[i])
        measured_track+=(_measured_track[i])
    vals=[datum.risidual for datum in res]
    


    matplotlib.rcParams.update({'font.size': 14, 'font.family': 'Ubuntu'})

    plt.subplot(221)
    plt.plot(positions, real_track, marker='.', linestyle='None')
    if scoringPlane is not None:
        plt.plot([sensor,sensor], [min(measured_track),max(measured_track)], 'r')
    plt.title("Real Track",fontstyle='italic')
    plt.ylabel("Hit Location (mm)")
    
    plt.subplot(222)
    plt.plot(positions, measured_track,marker='.', linestyle='None')
    if scoringPlane is not None:
        plt.plot([sensor,sensor], [min(measured_track),max(measured_track)], 'r')
    plt.title("Measured Track",fontstyle='italic')
    plt.xlabel("Plate Positions (mm)")
    if scoringPlane is not None:
        plt.subplot(223)
        plt.hist(vals,linspace(min(vals),max(vals),100))
        plt.xlabel("Residual - Distance from Actual to Reconstructed (mm)")
        plt.ylabel("Number of Particles")
        #plt.title("Hits Line of Best Fit at x=%s"%sensor)

    plt.subplot(224)
    plt.axis("off")
    plt.annotate(xy=(.3,.8),s="%s Events"%events)

    plt.annotate(xy=(.3,.6),s="Resolution is %.03e"%resolution)
    if scoringPlane is not None:
        plt.annotate(xy=(.3,.7),s="Sensor is at %smm"%sensor)
        plt.annotate(xy=(.3,.5),s="Sensor Radlen is %.03e"%scoringPlane.radlen)
    plt.show()

