from logging import exception
import typer
import requests
import os
import random
import json
import string 

# Initialize Typer App
app = typer.Typer()

# Get Environment Variables
OKTA_ORG=os.environ.get('OKTA_ORG')                                  
OKTA_TOKEN= "SSWS "+os.environ.get('OKTA_ADMIN_TOKEN')
OKTA_USER_BULK_PASSWORD=os.environ.get('OKTA_USER_BULK_PASSWORD')    # H72bbuYYumlkPqw007


@app.command()
def create_user(firstname: str, lastname: str, email: str):
    url = OKTA_ORG+"api/v1/users?activate=true"

    payload = json.dumps({
    "profile": {
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "login": email
    }
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': OKTA_TOKEN
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions as e:
        raise SystemExit(e)
    
    if response.status_code == 200:
        print ("User {} created successfully".format(email))
    else:
        print ("User Creation Unsuccesful.")

@app.command()
def create_bulk_users(number_of_users: int):
    if number_of_users < 1:
        raise SystemExit("No. of Users cant be 0 or negative")
    else:
        for user in range(number_of_users):
            url = OKTA_ORG+"api/v1/users?activate=true"
            mydomain = "@akshay.im"

            firstname = ''.join((random.choice(string.ascii_lowercase) for x in range(8)))
            lastname = ''.join((random.choice(string.ascii_lowercase) for x in range(8)))
            email = firstname+mydomain

            payload = json.dumps({
            "profile": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email,
                "login": email
            },
            "credentials": {
                "password": {
                "value": OKTA_USER_BULK_PASSWORD
                }
            }
            })

            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': OKTA_TOKEN
            }
            try:
                response = requests.request("POST", url, headers=headers, data=payload)
            except requests.exceptions as e:
                raise SystemExit(e)
            
            if response.status_code == 200:
                print ("User {} created successfully \n".format(email))
            else:
                print ("User Creation Unsuccesful.")



@app.command()
def list_users():

    url = OKTA_ORG+"api/v1/users/"

    payload={}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': OKTA_TOKEN
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except requests.exceptions as e:
        raise SystemExit(e)

    jsonRes = response.json()
    for x in range(len(jsonRes)):
        print("FirstName:",jsonRes[x]['profile']['firstName'],"LastName:",\
            jsonRes[x]['profile']['lastName'],\
            "Username:",jsonRes[x]['profile']['login'], "Status:",jsonRes[x]['status'])


@app.command()
def delete_user(email: str):

    # Get UserID from email:
    find_user_url = OKTA_ORG+"api/v1/users/?q="+email+"&limit=1"
    payload={}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': OKTA_TOKEN
    }

    try:
        response = requests.request("GET", find_user_url, headers=headers, data=payload)
    except requests.exceptions as e:
        raise SystemExit(e)

    jsonRes = response.json()
    userid = jsonRes[0].get('id')

    if userid:
        url = OKTA_ORG+"api/v1/users/"+userid

        # Deprovision User 
        try:
            del_response = requests.request("DELETE", url, headers=headers, data=payload)
        except requests.exceptions as e:
            raise SystemExit(e)
        print("User Deprovisioned Successfully")
        #Delete User
        try:
            user_response = requests.request("GET", find_user_url, headers=headers, data=payload)
        except requests.exceptions as e:
            raise SystemExit(e)

        # Maybe a better way to implement this can be to use some kind of polling for user status.
        if user_response.status_code != 404:
            try:
                del_response = requests.request("DELETE", url, headers=headers, data=payload)
            except requests.exceptions as e:
                raise SystemExit(e)

            print("User {} deleted successfully".format(email) )
        else:
            print("User {} deleted successfully".format(email) )


if __name__ == "__main__":
    app()