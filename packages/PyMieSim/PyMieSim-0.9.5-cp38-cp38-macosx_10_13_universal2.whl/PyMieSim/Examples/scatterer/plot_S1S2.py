"""
==========================
S1 S2 function computation
==========================

"""


def run():
    from PyMieSim.Scatterer import Sphere
    from PyMieSim.Source import PlaneWave

    source = PlaneWave(wavelength=450e-9,
                       polarization=0,
                       amplitude=1)

    scatterer = Sphere(diameter=600e-9,
                       source=source,
                       index=1.4)

    S1S2 = scatterer.get_s1s2(sampling=200)

    S1S2.plot().show()


if __name__ == '__main__':
    run()
