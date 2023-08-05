"""
======================
Far-Fields computation
======================

"""


def run():
    from PyMieSim.Scatterer import Sphere
    from PyMieSim.Source import PlaneWave

    source = PlaneWave(wavelength=1000e-9,
                       polarization=0,
                       amplitude=1)

    scatterer = Sphere(diameter=1500e-9,
                       source=source,
                       index=1.4)

    Fields = scatterer.get_far_field(sampling=100)

    Fields.plot().show()


if __name__ == '__main__':
    run()
