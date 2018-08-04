from flask import Flask, render_template, Blueprint

b_docker = Blueprint('docker', __name__, url_prefix='/docker')

@b_docker.route('')
def docker():
    return render_template('docker.html')

