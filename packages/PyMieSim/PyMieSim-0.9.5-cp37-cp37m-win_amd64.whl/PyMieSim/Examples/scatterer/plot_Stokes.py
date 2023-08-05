"""
=============================
Stokes parameters computation
=============================

"""


def run():
    from PyMieSim.Scatterer import Sphere
    from PyMieSim.Source import PlaneWave

    source = PlaneWave(wavelength=450e-9,
                       polarization=0,
                       amplitude=1)

    scatterer = Sphere(diameter=300e-9,
                       source=source,
                       index=1.4)

    Stokes = scatterer.get_stokes(sampling=100)

    Stokes.plot().show()


if __name__ == '__main__':
    run()
