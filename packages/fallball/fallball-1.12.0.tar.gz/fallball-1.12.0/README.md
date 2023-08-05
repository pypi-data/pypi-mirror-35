# FallBall Service (backend)
[![Build Status](https://travis-ci.org/ingrammicro/fallball-service.svg?branch=master)](https://travis-ci.org/ingrammicro/fallball-service) [![PyPi Status](https://img.shields.io/pypi/v/fallball.svg)](https://pypi.python.org/pypi/fallball) [![codecov](https://codecov.io/gh/ingrammicro/fallball-service/branch/master/graph/badge.svg)](https://codecov.io/gh/ingrammicro/fallball-service)


## Overview
FallBall is the best in class file sharing service that offers cloud storage and file synchronization for small and medium businesses (SMBs) worldwide.
This dummy service helps developers to learn [APS Connect](http://aps.odin.com) technology 

## Manual Deploy
1. Create application database:
    ```
    python manage.py migrate
    ```
1. In order to run server you need to execute the following command from the root folder of the project:
    ```
    python manage.py runserver <host_name>:<port>
    ```

## Deploy into docker container
1. Run docker-compose:
    ```
    docker-compose up
    ```
1. Run kickstart script:
    ```
    docker exec -it fallballapp bash kickstart.sh
    ```

Admin token:
    ```
    d8cc06c05a6cd5d5b6156fd2eb963a6f1fdd039c
    ```

## Tests
To run tests simply execute the following command:

```
python manage.py test fallballapp.tests
```

## API Reference
In order to explore API description follow to [apiary](http://docs.fallball.apiary.io/) page