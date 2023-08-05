"""
======================
Qsca vs wavelength std
======================

"""


def run():
    import numpy as np
    from PyMieSim.Experiment import CylinderSet, SourceSet, Setup
    from PyMieSim.Materials import Silver
    from PyMieSim import Measure

    scatSet = CylinderSet(diameter=np.linspace(400e-9, 1400e-9, 10),
                          material=Silver,
                          n_medium=1)

    sourceSet = SourceSet(wavelength=np.linspace(200e-9, 1800e-9, 300),
                          polarization=[0],
                          amplitude=1)

    experiment = Setup(scatSet, sourceSet)

    Data = experiment.Get(Measure.Qsca)

    Data.plot(y=Measure.Qsca, x=sourceSet.wavelength, y_scale='log', std=scatSet.diameter).show()


if __name__ == '__main__':
    run()
