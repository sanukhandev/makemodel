# Python-Programs

![Python](https://img.shields.io/badge/Python-3.10-brightgreen.svg)

 Author: Sanu Khan <br>
 Scrapping web to get make models list <br>
 various operations <br>

 ## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
* Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
* Python - [Download & Install Python](https://www.python.org/downloads/). OSX and Linux machines typically have this already installed
* virtualenv - use pip to install the virtualenv 

```bash
$ pip install virtualenv
```
## Installation
Once you've downloaded the installed all the prerequisites, you're just a few steps away from starting the application.

* Frist create a virtualenv environment for running this project using below command 
```bash
$ virtualenv venv
```
* Activate virtualenv 
`windows`
```bash
$ .\venv\Scripts\activate
```
`OS X & Linux`
```bash
$ source .\venv\Scripts\activate
```

* Install dependencices using pip 
To install the dependencies, run this in the application folder from the command-line:
```bash
$ pip install req.txt
```

* That's it now just execute the script using below command

```bash
$ python scrape.py 
```