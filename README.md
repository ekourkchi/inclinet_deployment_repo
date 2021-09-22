# IncliNET - 

![inclinet](https://user-images.githubusercontent.com/13570487/134272581-5720cada-75b4-4f4e-9eda-4bd9753a34e5.png)

----


## Description

IncliNET is a Python application to determine the inclination of Spiral Galaxies

- This application is hosted on EDD: [IncliNET](http://edd.ifa.hawaii.edu/inclinet/)
- [EDD: Extragalactic Distance Database](ttp://edd.ifa.hawaii.edu)


## Code Repository & Issues

https://github.com/ekourkchi/inclinet_deployment_repo


## Basic Install


Execute

```console
$ sh serverup.sh
```

## Installing from DockerHub


## Quick Usage

```bash
>>> import pycf3
>>> cf3 = pycf3.CF3()
>>> result = cf3.calculate_distance(velocity=9000, glon=283, glat=75)
>>> print(result.observed_velocity_)
9000.0
>>> result.observed_distance_
array([136.90134347])
```

For more information, read the [tutorial in the
documentation](https://pycf3.readthedocs.io).


### ABOUT THE DATA

All data exposed by the IncliNET project belongs to 

> Cosmicflows-4 program
> Copyright (C) Cosmicflows
> Team - The Extragalactic Distance Database (EDD)

Please cite:

> Cosmicflows-4: The Catalog of ∼10,000 Tully-Fisher Distances

```bib
@ARTICLE{2020ApJ...902..145K,
       author = {{Kourkchi}, Ehsan and {Tully}, R. Brent and {Eftekharzadeh}, Sarah and {Llop}, Jordan and {Courtois}, H{\'e}l{\`e}ne M. and {Guinet}, Daniel and {Dupuy}, Alexandra and {Neill}, James D. and {Seibert}, Mark and {Andrews}, Michael and {Chuang}, Juana and {Danesh}, Arash and {Gonzalez}, Randy and {Holthaus}, Alexandria and {Mokelke}, Amber and {Schoen}, Devin and {Urasaki}, Chase},
        title = "{Cosmicflows-4: The Catalog of {\ensuremath{\sim}}10,000 Tully-Fisher Distances}",
      journal = {\apj},
     keywords = {Galaxy distances, Spiral galaxies, Galaxy photometry, Hubble constant, H I line emission, Large-scale structure of the universe, Inclination, Sky surveys, Catalogs, Distance measure, Random Forests, 590, 1560, 611, 758, 690, 902, 780, 1464, 205, 395, 1935, Astrophysics - Astrophysics of Galaxies},
         year = 2020,
        month = oct,
       volume = {902},
       number = {2},
          eid = {145},
        pages = {145},
          doi = {10.3847/1538-4357/abb66b},
archivePrefix = {arXiv},
       eprint = {2009.00733},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2020ApJ...902..145K},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

## Authors


- Ehsan Kourkchi - [ekourkchi@gmail.com](ekourkchi@gmail.com)
