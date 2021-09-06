from logging import exception
import typer
import requests
import os
import random


app = typer.Typer()

OKTA_ORG=os.environ.get('OKTA_ORG')
OKTA_TOKEN= "SSWS "+os.environ.get('OKTA_ADMIN_TOKEN')

config = {
    'orgUrl': OKTA_ORG,
    'token': OKTA_TOKEN
}

@app.command()
def create_user(name: str = typer.Argument("World", envvar="AWESOME_NAME")):
    typer.echo(f"Testing")

@app.command()
def create_bulk_users(name: str = typer.Argument("World", envvar="AWESOME_NAME")):

    typer.echo(f"Testing")

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

if __name__ == "__main__":
    app()