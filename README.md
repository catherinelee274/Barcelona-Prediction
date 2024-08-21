# Barcelona Prediction
Predicting accidents or air pollution with Barcelona dataset

full.csv - combined weather,precipitation features 

# Commands to deploy
*requires python3, pip3, virtualenv 

If you don't have virtualenv `pip install virtualenv`

```
$ virtualenv venv
$ source venv/bin/activate
```
 
`$ pip install -r requirements.txt` to download dependencies (listed below). requirements.txt is in the repo. Make sure you are in the directory)

`$ flask run`

If it gives an error that says `Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.`, change to the `app` directory with `cd app`  and `flask run` again

# Edit Flask web app

Edit controllers/ to update how to receive and reply to requests.

Edit templates/ to update the layout and styling.

Edit models/ to update how the data is stored.


# Dependencies (Deployment)
- Flask 
- Flask-SQLAlchemy
- alembic
- certifi
- cffi
- chardet
- Click
- Flask-Misaka
- gunicorn
- idna
- itsdangerous
- Jinja2
- Mako
- MarkupSafe
- misaka
- pycparser
- python-dotenv
- requests
- urllib3
- Werkzeug

# Dependencies (Jupyter Notebook)
- TODO

# Paths
`/notebooks  ` all jupyter notebooks 

`/notebooks/data` path used for *DATASETS* used by jupyter nb so put all data here

`notebooks/main.ipynb` - main nb with modeling

`noteboooks/barcelona_eda.ipynb` - eda nb 

`/notebooks/index2.html` front page d3js code

`/app/app.py` main app

`/app/templates` html templates

`/app/templates/home/index2.html` front page d3js code



