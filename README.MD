# Strava APP
 
### Table of Contents
 
- [Project Motivation](#motivation)
- [Tech stack](#tech)
- [Quick start](#installation)
 
 
## Project Motivation<a name="motivation"></a>
 
This is a project with objective of creating an APP using the Strava API. According to Wikipedia, Strava is: "An American internet service for tracking physical exercise which incorporates social network features."
 
## Tech stack <a name="tech"></a>
- Python: programming language used to build the backend
- FastAPI: framework used to build the API, which has the goal to connect this app with the original Strava API
 
## Quick start <a name="installation"></a>
 
1. Create your account on Strava API
 
In this site - https://developers.strava.com/docs/getting-started/ - you can find all instructions to begin exploring the API.
 
2. Create your .env file
 
First of all, you need to create in the root folder the .env file, with the following content:
```
TOKEN=
REFRESH_TOKEN=
CLIENT_ID=
CLIENT_SECRET=
REFRESH_TOKEN=
```
For sure, filling all of these informations with yours.
 
3. Launch your API with Docker containers
```
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```
 
To confirm everything is running type the following code in your browser: http://127.0.0.1/api/strava/list?page=1
 
 
 
 
 
 


