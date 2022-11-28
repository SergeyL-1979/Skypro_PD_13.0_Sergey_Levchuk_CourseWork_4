#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py
from app import app


@app.route('/')
def index():
    return 'СТАРТОВАЯ СТРАНИЦА'


if __name__ == '__main__':
    app.run()
