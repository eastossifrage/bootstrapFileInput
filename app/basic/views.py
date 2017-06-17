# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import render_template, request, current_app, redirect, url_for
from . import basic
from werkzeug.utils import secure_filename
import os


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@basic.route('/example_1', methods=['GET', 'POST'])
def example_1():
    if request.method == 'POST':
        file = request.files['input-1']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_1.html')


@basic.route('/example_2', methods=['GET', 'POST'])
def example_2():
    if request.method == 'POST':
        file = request.files['input-2']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_2.html')


@basic.route('/example_3', methods=['GET', 'POST'])
def example_3():
    if request.method == 'POST':
        files = request.files['input-3[]']
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_3.html')


@basic.route('/example_4', methods=['GET', 'POST'])
def example_4():

    return render_template('example_4.html')


@basic.route('/example_5', methods=['GET', 'POST'])
def example_5():
    if request.method == 'POST':
        file = request.files['input-5']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_5.html')


@basic.route('/example_6', methods=['GET', 'POST'])
def example_6():
    if request.method == 'POST':
        file = request.files['input-6']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_6.html')


@basic.route('/example_7', methods=['GET', 'POST'])
def example_7():
    if request.method == 'POST':
        file = request.files['input-7']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_7.html')


@basic.route('/example_8', methods=['GET', 'POST'])
def example_8():
    if request.method == 'POST':
        file = request.files['input-8']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template('example_8.html')
