#!/usr/bin/python3
from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
