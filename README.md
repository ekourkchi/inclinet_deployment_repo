# IncliNET

![inclinet](https://user-images.githubusercontent.com/13570487/134272581-5720cada-75b4-4f4e-9eda-4bd9753a34e5.png)

![Screenshot from 2021-09-21 19-05-20](https://user-images.githubusercontent.com/13570487/134273571-099b9f86-ffb3-450e-94a8-c3262970f51f.png)


## Description

IncliNET is a Python application to determine the inclination of Spiral Galaxies

- This application is hosted on EDD: [IncliNET](http://edd.ifa.hawaii.edu/inclinet/)
- [EDD: Extragalactic Distance Database](https://edd.ifa.hawaii.edu)


## Code Repository & Issues

https://github.com/ekourkchi/inclinet_deployment_repo


## Basic Install


Execute

```console
$ sh serverup.sh
```

## Installing from DockerHub


## API

```bash
$ curl https://edd.ifa.hawaii.edu/inclinet/api/pgc/2557
{
"status": "success",
"galaxy": {
    "pgc": "2557",
    "ra": "10.6848 deg",
    "dec": "41.2689 deg",
    "fov": "266.74 arcmin",
    "pa": "35.0 deg",
    "objname": "NGC0224"
},
"inclinations": {
    "Group_0": {
    "model4": 69.0,
    "model41": 72.0,
    "model42": 76.0,
    "model43": 71.0
    },
    "Group_1": {
    "model5": 73.0,
    "model51": 73.0,
    "model52": 74.0,
    "model53": 74.0
    },
    "Group_2": {
    "model6": 73.0,
    "model61": 76.0,
    "model62": 76.0,
    "model63": 67.0
    },
    "summary": {
    "mean": 72.83333333333333,
    "median": 73.0,
    "stdev": 2.6718699236468995
    }
},
"rejection_likelihood": {
    "model4-binary": 50.396937131881714,
    "model5-binary": 20.49814760684967,
    "model6-binary": 65.37048816680908,
    "summary": {
    "mean": 45.42185763518015,
    "median": 50.396937131881714,
    "stdev": 18.65378065042258
    }
}
}
```

For more information, read the [tutorial in the
documentation]().

### Related information

- For furhter details on various VGG models we considered in this project [click here](https://github.com/ekourkchi/incNET-data/tree/master/incNET_VGGcnn_withAugmentation).
- [Visit here](https://github.com/ekourkchi/inclinet_production_repo/blob/main/Inclinet_Deployment_Architecture.pdf) to get the full picture of the deployment plan.
- [Project proposal and motivations](https://github.com/ekourkchi/incNET-data)
- [Data Preprocessing](https://github.com/ekourkchi/incNET-data/blob/master/incNET_dataPrep/incNET_dataClean.ipynb) in order to get reliable labels
- On how to download data from the SDSS image service and preprocess them [click here](https://github.com/ekourkchi/SDSS_get)

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

## Author

- Ehsan Kourkchi - [ekourkchi@gmail.com](ekourkchi@gmail.com)

## Disclaimer <a name="Disclaimer"></a>

 * All rights reserved. The material may not be used, reproduced or distributed, in whole or in part, without the prior agreement. 