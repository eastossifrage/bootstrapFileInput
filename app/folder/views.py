# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, request, jsonify
from . import folder


@folder.route('/example_1', methods=['GET', 'POST'])
def example_1():

    return render_template('ex_1.html')


@folder.route('/example_2', methods=['GET', 'POST'])
def example_2():

    return render_template('ex_2.html')

