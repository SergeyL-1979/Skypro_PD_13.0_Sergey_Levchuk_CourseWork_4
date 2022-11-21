#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py
from app import app
import config


@app.route('/')
def index():
    return 'СТАРТОВАЯ СТРАНИЦА'


if __name__ == '__main__':
    app.run(debug=True)
