# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
#import pandas as pd
blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    #df = pd.read_csv("count_datetimeindex.csv")
    return render_template('home/index2.html')
