# barcelona_predict
Predicting accidents or air pollution with Barcelona dataset

full.csv - combined weather,precipitation features (needs to add air quality feature later) 
# Edit Flask web app

Edit controllers/ to update how to receive and reply to requests.

Edit templates/ to update the layout and styling.

Edit models/ to update how the data is stored.

# Commands to deploy

```
$ virtualenv venv
$ source venv/bin/activate
```
 
`$ pip install -r requirements.txt` to download dependencies
`npm install d3-timeseries --save` 

`$ flask run`

If it gives an error that says `Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.`, change to the `app` directory with `cd app`

# Dependencies 
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

# Paths
`/notebooks  ` all jupyter notebooks 

`/notebooks/data` datasets

`/app/app.py` main app

`/app/templates` html templates

`/app/templates/home/index2.html` front page d3js code

