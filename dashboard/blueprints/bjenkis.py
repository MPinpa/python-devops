from flask import Flask, render_template, Blueprint, redirect


jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')


@jenkins.route('')
def index():
    return render_template('jenkins.html')

@jenkins.route('update')
def update():
    return render_template('jenkins_update.html')