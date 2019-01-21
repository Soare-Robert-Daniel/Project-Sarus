
# A simple prototype app that use microservices arhitecture

**A simple app that use microservices arhitecture.**

**Motivation**: Using the basic functions of the Node.Js, Flask, Docker, Sqlite3 in order to understand how to create a simple web app using modern approaches.
    
**What the app does**: The web page request an email from the user. The email is sent to a server build upon Node.js via HTTP request,  after processing the email is redirected to a python server that runs locally, which will store it to the database. 

## Install

### Step 1
Clone the repository.
```sh
$ git clone https://github.com/Soare-Robert-Daniel/Project-Sarus
```
### Step 2
Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
### Step 3
Run the commands in terminal:
```sh
$ cd The-Beginning/Chapter-I/
$ docker-compose up
```
