# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template
from . import advanced


@advanced.route('/example_1', methods=['GET', 'POST'])
def example_1():

    return render_template('example_1.html')


@advanced.route('/example_2', methods=['GET', 'POST'])
def example_2():

    return render_template('example_2.html')


@advanced.route('/example_3', methods=['GET', 'POST'])
def example_3():

    return render_template('example_3.html')


@advanced.route('/example_4', methods=['GET', 'POST'])
def example_4():

    return render_template('example_4.html')


@advanced.route('/example_5', methods=['GET', 'POST'])
def example_5():

    return render_template('example_5.html')


@advanced.route('/example_6', methods=['GET', 'POST'])
def example_6():

    return render_template('example_6.html')


@advanced.route('/example_7', methods=['GET', 'POST'])
def example_7():

    return render_template('example_7.html')


@advanced.route('/example_8', methods=['GET', 'POST'])
def example_8():

    return render_template('example_8.html')
