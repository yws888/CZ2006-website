# CZ2006
 CZ2006 website

Deployed at http://wenshiuanthegod.pythonanywhere.com/

Documentation can be viewed at http://wenshiuanthegod.pythonanywhere.com/admin/doc

Login with username: a and password: a

## Setup (for Mac)
Change Directory to the root of this repository.

Create virtual environment

```
virtualenv proj_env
```

Activate virtual environment
```
source proj_env/bin/activate
```

Install dependencies (Only for 1st time or if there are additional dependencies added)
```
pip3 install -r requirements.txt
```

Start the server
```
python3 CZ2006/manage.py runserver
```

Website should then be accessible at:
```
http://localhost:8000/
```

## Setup (for Windows)
Change Directory to the root of this repository.

Set up virtual environment
```
py -m venv env
```

Install dependencies (Only for 1st time or if there are additional dependencies added)
```
py -m pip install -r requirements.txt
```

Start the server
```
py CZ2006/manage.py runserver
```

