
# SixtyFour Data Intelligence LLP

Assignment for a back-end development internship 

Objective:
1.	Registers a user and creates the user in the database of your choice.
Create an end point to register a user - /register
Capture the following fields:
User name  - user input
Email – user input
Expiry date – should be 1 year from register date.
API – create a 10 digit alpha numeric API key for the user and store it encrypted in DB.

2.	Authenticates the user on login through swagger UI
/user/authenticate endpoint should take the API key as input on clicking the default Authorise button in docs 

3.	Authorise the user on accessing this url and return user name and email address Using the end point /getUserData
Handle error scenarios with appropriate status codes like 400, 402 500 for – 1. User does not exits. 2. Invalid API key 3. Key expired 

4.	If possible, implement session cookie-based authentication so that each request is not routed to DB.

## Run Locally

Clone the project

```bash
  git clone https://github.com/mogiiee/AI-planet.git
```

Go to the project directory

```bash
  cd AI planet
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn app.main:app --reload
```

## Using docker

Or you could simply run 
```
    docker-compose up
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. I have included a .env.sample file already in the projet where you will see the variables needed to go throuh with the process.

`CLUSTER`=

`DB`=

`collection` = 


#jwt


`secret` =

`algorithm` =

## Deployment

If you dont want to go though getting all the environment variables ready, you could always see the deployed project on RENDER (RIP HEROKU😭🫡)

```bash
  https://six4-task.onrender.com/docs
```
keep in mind this is my personal account on the free tier so please dont spam as i have only certain amount of storage on the DB 🥺😩. 

RENDER takes about 2 minuites to start up when it has 0 activity from the past 15 mins so please wait patiently as the deployed site loads (AGAIN RIP HEROKU😭🫡).


## Contributing

Contributions are always welcome!


## License

[MIT](https://choosealicense.com/licenses/mit/)



