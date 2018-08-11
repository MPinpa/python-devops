from flask import Flask, render_template, Blueprint, redirect
import docker

bdocker = Blueprint('docker', __name__, url_prefix='/docker')
con = docker.DockerClient('tcp://192.168.0.200:2376')


@bdocker.route('')
def index():
    #containers = con.containers.list(all=True)
    containers = con.containers.list(all=True)
    return render_template('docker.html', containers=containers)

@bdocker.route('/start/<shortid>')
def start_container(shortid):
    containers = con.containers.get(shortid)
    containers.start()
    return redirect('/docker')


@bdocker.route('/stop/<shortid>')
def stop_container(shortid):
    containers = con.containers.get(shortid)
    containers.stop()
    return redirect('/docker')



