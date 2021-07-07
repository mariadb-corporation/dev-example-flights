# Flights

**Flights** is a web application, backed by the power of the MariaDB Connectors and [MariaDB ColumnStore database](https://mariadb.com/docs/features/mariadb-columnstore/), allows you to analyze millions [flight records from the United States Department of Transportation](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time) in real time without needing to add any indexes!

<p align="center" spacing="10">
    <kbd>
        <img src="media/demo.gif" />
    </kbd>
</p>

This README will walk you through the steps for getting the Flights web application up and running using MariaDB ColumnStore. To ensure success, please follow the instructions in order.

**Note:** The code provided within this repository is completely open source. Please feel free to use it as you see fit.

# Table of Contents
1. [Requirements](#requirements)
2. [Introduction to MariaDB](#introduction)
    1. [MariaDB Platform](#platform)
    2. [MariaDB SkySQL](#skysql)
3. [Getting started](#getting-started)
    1. [Get the code](#code)
    2. [Get the data, create the schema, and load the data](#data)
    3. [Anatomy of the app](#app)
    4. [Build and run the app](#build-run)
4. [Support and contribution](#support-contribution)
5. [License](#license)

## Requirements <a name="requirements"></a>

This sample application, no matter which API project you target, will requires the following to be installed/enabled on your machine:

* [MariaDB Client](https://mariadb.com/products/skysql/docs/clients/), used to connect to MariaDB instances.
* [Bash](https://www.gnu.org/software/bash/) (if you are using Windows 10, you will need to enable the Windows Subsystem for Linux), used to run the data download script

## Introduction to MariaDB <a name="introduction"></a>

### MariaDB Platform <a name="platform"></a>
[MariaDB Platform](https://mariadb.com/products/mariadb-platform/) integrates [transactional](https://mariadb.com/products/mariadb-platform-transactional/) and [analytical](https://mariadb.com/products/mariadb-platform-analytical/) products so developers can build modern applications by enriching transactions with real-time analytics and historical data, creating insightful experiences and compelling opportunities for customers – and for businesses, endless ways to monetize data. 

<p align="center" spacing="10">
    <kbd>
        <img src="media/platform.png" />
    </kbd>
</p>

To get started using MariaDB locally you can choose one of the following options:

* [Download and install MariaDB (Community or Enterprise) directly from mariadb.com](https://mariadb.com/docs/deploy/installation/) 

* [Download and install MariaDB using the official MariaDB Community Server 10.5 Docker Image available at hub.docker.com](https://hub.docker.com/r/mariadb/columnstore)

### MariaDB SkySQL <a name="skysql">

[SkySQL](https://mariadb.com/products/skysql/) is the first and only database-as-a-service (DBaaS) to bring the full power of MariaDB Platform to the cloud, including its support for transactional, analytical and hybrid workloads. Built on Kubernetes, and optimized for cloud infrastructure and services, SkySQL combines ease of use and self-service with enterprise reliability and world-class support – everything needed to safely run mission-critical databases in the cloud, and with enterprise governance.

[Get started with SkySQL!](https://mariadb.com/products/skysql/#get-started)

<p align="center" spacing="10">
    <kbd>
        <img src="media/skysql.png" />
    </kbd>
</p>

## Getting started <a name="getting-started"></a>

In order to run the Flights application you will need to have a MariaDB instance to connect to. For more information please check out "[Get Started with MariaDB](https://mariadb.com/get-started-with-mariadb/)".

### Get the code <a name="code"></a>

Download this code directly or use [git](git-scm.org) (through CLI or a client) to retrieve the code using `git clone`:

```
$ git clone https://github.com/mariadb-corporation/dev-example-flights.git
```

### Get the data, create the schema, and load the data <a name="data"></a>

This application uses (US domestic) flight data freely available from the [Bureau of Transportation on time performance dataset](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). The [get_flight_data.sh] shell script will be used to download the flight data (between 1990 and 2020) into a folder called _data_. 

Complete the following steps.

1. Download the flight data (approx. 180 million records, ~30 GB). Depending on your internet connection this may take some time. However, you can simply modify [get_flight_data.sh](get_flight_data.sh) script to adjust the amount of flight information that is downloaded. Doing so will not disrupt subsequent steps. 

```bash 
$ ./get_flight_data.sh
```

2. Create the `flights` database, `airlines`/`airports`/`flights` tables, and load the tables with data. Be sure to include your database instance specific information (host url, port number, username, and password)

```bash
$ ./create_and_load.sh host_url port user password
```

**Note:** Remember to wrap argument values in single quotes if they contain special characters (e.g. !)

By default the [create_and_load.sh](create_and_load.sh) script has ssl enabled and assumes a MariaDB [SkySQL certificate authority chain file](https://mariadb.com/products/skysql/docs/operations/connecting/#certificate-authority) exists next to it. Feel free to modify accordingly.

### Anatomy of the app <a name="app"></a>

This application is made of two parts:

* Client
    - communicates with the API.
    - is a React.js project located in the [client](client) folder.
* API
    - uses a MariaDB Connector to connect to MariaDB.
    - contains multiple projects, located in the [api](api) folder.
        - [Node.js](api/nodejs)
        - [Python](api/python)

See the README's in [client](client/README.md) and [api](api/README.md) for more information on how to get started!

### Build and run the app <a name="build-run"></a>

1. Navigate to the [client](client) folder and execute the following CLI command to install the package dependencies for the React.js application.

```bash
$ npm install
```

2. Pick an [API](api) project and follow the instructions of the README to build and run the API project.

3. Navigate to the [client](client) folder and execute the following CLI command to start the React.js application.

```bash 
$ npm start
``` 

4. Open a browser window and navigate to http://localhost:3000.

## Support and Contribution <a name="support-contribution"></a>

Thanks so much for taking a look at the Flights app! As this is a very simple example, there's a lot of potential for customization. Please feel free to submit PR's to the project to include your modifications!

If you have any questions, comments, or would like to contribute to this or future projects like this please reach out to us directly at developers@mariadb.com or on [Twitter](https://twitter.com/mariadb).

## License <a name="license"></a>
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=plastic)](https://opensource.org/licenses/MIT)
