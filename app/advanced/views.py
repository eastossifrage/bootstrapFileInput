# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, request, jsonify
from . import advanced


@advanced.route('/delete', methods=['GET', 'POST'])
def delete():
    key = request.form.get('key')
    print key

    return jsonify()


@advanced.route('/example_1', methods=['GET', 'POST'])
def example_1():

    return render_template('exam_1.html')


@advanced.route('/example_2', methods=['GET', 'POST'])
def example_2():

    return render_template('exam_2.html')


@advanced.route('/example_3', methods=['GET', 'POST'])
def example_3():

    return render_template('exam_3.html')


@advanced.route('/example_4', methods=['GET', 'POST'])
def example_4():

    return render_template('exam_4.html')


@advanced.route('/example_5', methods=['GET', 'POST'])
def example_5():

    return render_template('exam_5.html')


@advanced.route('/example_6', methods=['GET', 'POST'])
def example_6():

    return render_template('exam_6.html')


@advanced.route('/example_7', methods=['GET', 'POST'])
def example_7():

    return render_template('exam_7.html')


@advanced.route('/example_8', methods=['GET', 'POST'])
def example_8():

    return render_template('exam_8.html')


@advanced.route('/example_9', methods=['GET', 'POST'])
def example_9():

    return render_template('exam_9.html')


@advanced.route('/example_10', methods=['GET', 'POST'])
def example_10():

    return render_template('exam_10.html')


@advanced.route('/example_11', methods=['GET', 'POST'])
def example_11():

    return render_template('exam_11.html')
