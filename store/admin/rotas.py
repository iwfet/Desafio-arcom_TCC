from flask import render_template, session, redirect, request, url_for

from store import app, db


@app.route('/')
def home():
    return"ola mundo"

@app.route('/registrar')
def registrar():
    return render_template('admin/registrar.html', title="registrar user")