![Version develop](https://img.shields.io/badge/flask--restplus-0.12.1-green)

# mowl 

mowl is an open-source project to help conference organizers analyze their historical sales data. 
Named after Mopcon and owl, mowlr would be a very simple way to help you manage the most important metrics for the ticket campaigns.

## Table of Contents
- [Environment](#environment)
- [Build](#build)
- [Deployment](#deployment)

## Environment
```
> virtualenv venv
> source venv/bin/activate
> source .config
```

Note that you will need to add your own system variables in .config as follows:
```
export BIND_PORT=8080
```

## Build 
```
> docker-compose up -d
```


## Deployment
Running toolman with AWS serverless endpoint.

```
> zappa deploy dev
```

To stop app

```
> zappa undeploy dev
```
