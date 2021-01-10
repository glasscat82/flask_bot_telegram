from flask import Flask
from flask_caching import Cache
from flask import request
from flask import jsonify
from flask import render_template
#from flask_sslify import SSLify

cache = Cache(config={'CACHE_TYPE': 'simple', "CACHE_DEFAULT_TIMEOUT": 300})
app = Flask(__name__)
cache.init_app(app)
# sslify = SSLify(app)