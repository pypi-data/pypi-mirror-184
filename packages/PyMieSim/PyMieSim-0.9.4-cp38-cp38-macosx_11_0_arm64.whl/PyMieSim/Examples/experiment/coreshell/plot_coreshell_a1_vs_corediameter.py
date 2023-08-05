"""
===================
a1 vs core diameter
===================

"""


def run():
    import numpy as np
    from PyMieSim.Experiment import SourceSet, Setup, CoreShellSet
    from PyMieSim.Materials import BK7, Silver
    from PyMieSim import Measure

    scatSet = CoreShellSet(core_diameter=np.geomspace(100e-09, 600e-9, 400),
                           shell_diameter=800e-9,
                           core_material=Silver,
                           shell_material=BK7,
                           n_medium=1)

    sourceSet = SourceSet(wavelength=[800e-9, 900e-9, 1000e-9],
                          polarization=0,
                          amplitude=1)

    experiment = Setup(scatterer_set=scatSet, source_set=sourceSet)

    data = experiment.Get([Measure.a1])

    data.plot(y=Measure.a1, x=scatSet.core_diameter, y_scale='log').show()


if __name__ == '__main__':
    run()
