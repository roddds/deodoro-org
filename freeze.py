#! /usr/bin/env python
from flask_frozen import Freezer
from main import app

BASE_URL = 'http://roddds.github.io/deodoro-org/'

app.config['FREEZER_BASE_URL'] = BASE_URL
app.static_url_path = BASE_URL + 'static'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()