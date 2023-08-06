# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:47:22 2018

@author: eendebakpt
"""

if __name__ == '__main__':
    from qtt.instrument_drivers.simulation_instruments import SimulationDigitizer
    from qtt.instrument_drivers.simulation_instruments import SimulationAWG
    import pdb
    from imp import reload
    import matplotlib.pyplot as plt
    reload(qtt.live_plotting)
    from qtt.live_plotting import *

    pv = qtt.createParameterWidget([gates])

    reload(qtt.measurements.scans)
    verbose = 1
    multiprocess = False

    digitizer = SimulationDigitizer(
        qtt.measurements.scans.instrumentName('sdigitizer'), model=station.model)
    station.components[digitizer.name] = digitizer

    station.awg = SimulationAWG(qtt.measurements.scans.instrumentName('vawg'))
    station.components[station.awg.name] = station.awg

    if 1:
        sweepparams = ['B0', 'B3']
        sweepranges = [160, 80]
        resolution = [80, 48]
        minstrument = (digitizer.name, [0, 1])
    else:
        sweepparams = 'B0'
        sweepranges = 160
        resolution = [60]
        minstrument = (digitizer.name, [0])
    station.model.sdnoise = .1
    vm = VideoMode(station, sweepparams, sweepranges, minstrument, Naverage=25,
                   resolution=resolution, sample_rate='default', diff_dir=None,
                   verbose=1, nplots=None, dorun=True)

    self = vm
    vm.setGeometry(910, 100, 800, 800)
