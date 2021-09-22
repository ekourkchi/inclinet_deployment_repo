# IncliNET

![inclinet_logo](https://user-images.githubusercontent.com/13570487/134275660-2585ec68-0744-4ad0-b02c-05ddb51bd9e4.png)

## Description

IncliNET is a Python application to determine the inclination of Spiral Galaxies

- This application is hosted on EDD: [IncliNET](http://edd.ifa.hawaii.edu/inclinet/)
- [EDD: Extragalactic Distance Database](https://edd.ifa.hawaii.edu)


## Code Repository & Issues

https://github.com/ekourkchi/inclinet_deployment_repo


## Basic Install 
### on a local machine using [Docker](https://www.docker.com/)

- First, you need to [install](https://docs.docker.com/compose/install/) Docker Compose. 

```bash
 pip install docker-compose
```

- Execute

```console
$ docker run -it --entrypoint /inclinet/serverup.sh -p 3030:3030  ekourkchi/inclinet
```

- Open the Application: Once the service is running in the terminal, open a browser like *Firefox* or *Google Chrome* and enter the following url: [http://0.0.0.0:3030/](http://0.0.0.0:3030/)

### On a server using Docker

- First, you need to install Docker Compose. [How to install](https://docs.docker.com/compose/install/)

- Execute

```console
$ docker run -it --entrypoint /inclinet/serverup.sh --env="WEBROOT=/inclinet/" -p pppp:3030 -v /pathTO/public_html/static/:/inclinet/static ekourkchi/inclinet
```

where `WEBROOT` is an environmental variable that points to the root of the application in the URL path. `pppp` is the port number that the service would be available to the world. `3030` is the port number of the docker container that our application uses by default. `/pathTO/public_html/static/` is the path to the `public_html` or any folder that the backend server uses to expose communicate with Internet. We basically need to mount `/pathTO/public_html/static/` to forlde `inclinet/static` whithin the container which is used internally by the application. 

**URL**: Following the above example, if the server host is accessible through `www.example.com`, then our application would be launched on `www.example.com/inclinet:pppp`. Remember `http` or `https` by default use ports 80 and 443, respectively.


### Using the codes without Docker

Just put the repository on the server or on a local machine and make sure that folder `<repository>/static` is linked to a folder that is exposed by the server to the outside world. Set `WEBROOT` prior to launching the application to point the application to the correct URL path.

Execution of `server.py` launches the application. 

```console
        $ python server.py -h


        - starting up the service on the desired host:port
        
        - How to run: 
        
            $ python server.py -t <host IP> -p <port_number> -d <debugging_mode>

        - To get help
            $ python server.py -h
        


        Options:
        -h, --help            show this help message and exit
        -p PORT, --port=PORT  the port number to run the service on
        -t HOST, --host=HOST  service host
        -d, --debug           debugging mode

```

Please refer to [the IncliNET code documentation](https://edd.ifa.hawaii.edu/static/html/server.html) for further details. 
For more information, read the [tutorial](https://edd.ifa.hawaii.edu/static/html/index.html).

![Inclinet_Deployment_flowchart](https://user-images.githubusercontent.com/13570487/134273571-099b9f86-ffb3-450e-94a8-c3262970f51f.png)

## API

- See the `API documentation` [here](https://edd.ifa.hawaii.edu/inclinet/api/docs)

- URL guery that reports all evaluated inclinations and other results in `json` format. `<PGC_id>` is the galaxy ID in the [HyperLeda](http://leda.univ-lyon1.fr/) catalog.

```bash
$ curl http://edd.ifa.hawaii.edu/inclinet/api/pgc/<PGC_id>

```

 - example:

    ```bash
    $ curl http://edd.ifa.hawaii.edu/inclinet/api/pgc/2557
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

- Given the `galaxy common name`, the following URL reports all evaluated inclinations and other results in `json` format. `<obj_name>` is the galaxy galaxy name. Galaxy name is looked up on [NASA/IPAC Extragalactic Database](https://ned.ipac.caltech.edu/) and the corresponding `PGC` number would be used for the purpose of our analysis.

```bash
$ curl http://edd.ifa.hawaii.edu/inclinet/api/objname/<obj_name>

```

 - example:

    ```bash
        $ curl http://edd.ifa.hawaii.edu/inclinet/api/objname/M33
        {
        "status": "success",
        "galaxy": {
            "pgc": 5818,
            "ra": "23.4621 deg",
            "dec": "30.6599 deg",
            "fov": "92.49 arcmin",
            "pa": "22.5 deg",
            "objname": "M33"
        },
        "inclinations": {
            "Group_0": {
            "model4": 54.0,
            "model41": 58.0,
            "model42": 54.0,
            "model43": 52.0
            },
            "Group_1": {
            "model5": 54.0,
            "model51": 55.0,
            "model52": 52.0,
            "model53": 55.0
            },
            "Group_2": {
            "model6": 56.0,
            "model61": 57.0,
            "model62": 55.0,
            "model63": 53.0
            },
            "summary": {
            "mean": 54.583333333333336,
            "median": 54.5,
            "stdev": 1.753963764987432
            }
        },
        "rejection_likelihood": {
            "model4-binary": 41.28798842430115,
            "model5-binary": 4.068140685558319,
            "model6-binary": 55.70455193519592,
            "summary": {
            "mean": 33.68689368168513,
            "median": 41.28798842430115,
            "stdev": 21.754880259382322
            }
        }
        }
    ```

- Given the `galaxy image`, the following API call reports all evaluated inclinations and other results in `json` format.

```bash
$ curl -F 'file=@/path/to/image/galaxy.jpg' http://edd.ifa.hawaii.edu/inclinet/api/file
```

where `/path/to/image/galaxy.jpg` would be replaced by the name of the galaxy image. The accepted suffixes are `'PNG', 'JPG', 'JPEG', 'GIF'` and uploaded files shoule be smaller than `1 MB`. 

 - example:

 ```bash
        $ curl -F 'file=@/path/to/image/NGC_4579.jpg' http://edd.ifa.hawaii.edu/inclinet/api/file
        {
        "status": "success",
        "filename": "NGC_4579.jpg",
        "inclinations": {
            "Group_0": {
            "model4": 47.0,
            "model41": 51.0,
            "model42": 50.0,
            "model43": 47.0
            },
            "Group_1": {
            "model5": 49.0,
            "model51": 49.0,
            "model52": 51.0,
            "model53": 52.0
            },
            "Group_2": {
            "model6": 50.0,
            "model61": 49.0,
            "model62": 49.0,
            "model63": 48.0
            },
            "summary": {
            "mean": 49.333333333333336,
            "median": 49.0,
            "stdev": 1.49071198499986
            }
        },
        "rejection_likelihood": {
            "model4-binary": 84.28281545639038,
            "model5-binary": 94.24970746040344,
            "model6-binary": 88.11054229736328,
            "summary": {
            "mean": 88.88102173805237,
            "median": 88.11054229736328,
            "stdev": 4.105278145778375
            }
        }
        }
 ```

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