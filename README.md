# okta-tech-assesment


## Assumptions:
i)   OKTA Token is present in an environment variable OKTA_ADMIN_TOKEN.  
ii)  OKTA Org URL is present in an environment variable OKTA_ORG. 
iii) You have Python3 and pip3 installed on your machine. 

## Envrionment:
i) Clone this repo.
ii) Create and Activate a Venv
```
python3 -m venv env
source env/bin/activate
```
iii) Install requirements
```
pip3 install -r requirements.txt
```

## Usage
We have 4 options with this CLI:



### i) Create Users:
We can use this option to create one user at a time. This option accepts 3 mandatory paramaters
i.e FirstName, Lastname and EmailID.

Example:
``` 
$> python3 main.py create-user Firstname LastName EmailID@emailproider.com
```

### ii) List Users
We can use this option to list FirstName, Lastname, Username and Status of all users in the Okta Org

Example:
```
$> python3 main.py list-users

FirstName: Sanchari LastName: Sarma Username: mail@akshay.im Status: PROVISIONED
FirstName: Akshay LastName: Patil Username: engineerakki11@gmail.com Status: ACTIVE
FirstName: kxkbpmui LastName: sfyzdlrv Username: kxkbpmui@akshay.im Status: ACTIVE
FirstName: rvvtwagl LastName: pjvaibyl Username: rvvtwagl@akshay.im Status: ACTIVE
```

### iii) Bulk Create Users
We can use this option to automatically create users in bulk. Our CLI will generate random strings to
create these users.
This option just accepts an integer as an option.

Example:
```
$> python3 main.py create-bulk-users 3

User kxkbpmui@akshay.im created successfully 

User fqemocys@akshay.im created successfully 

User rvvtwagl@akshay.im created successfully 
```

### iv) Delete USER
We can use this option to delete a single user in OKTA org.

Example:
```
$> python3 main.py delete-user rvvtwagl@akshay.im

User Deprovisioned Successfully
User rvvtwagl@akshay.im deleted successfully
```


#### Note:
i) As I have used typer to create this cli,
we can just put --help in our cli command to get more information and parameters about the cli command

Example:
```
$> python3 main.py create-user --help

Usage: main.py create-user [OPTIONS] FIRSTNAME LASTNAME EMAIL

Arguments:
  FIRSTNAME  [required]
  LASTNAME   [required]
  EMAIL      [required]

Options:
  --help  Show this message and exit.
```

ii) I have not added unit tests at the moment, 
but I can add them easily if more time is given. 