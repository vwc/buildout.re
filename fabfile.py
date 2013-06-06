from __future__ import with_statement
from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import sudo


def deployment():
    env.use_ssh_config = True
    env.forward_agent = True
    env.port = '22222'
    env.user = 'root'
    env.hosts = ['sechszuvier.vorwaerts-werbung.de']
    env.webserver = '/opt/webserver/buildout.webserver'
    env.code_root = '/opt/sites/re/buildout.re'
    env.code_user = 'root'
    env.prod_user = 'www'


def ls():
    with cd(env.code_root):
        run('ls')


def update():
    with cd(env.code_root):
        run('nice git pull')


def rebuild():
    with cd(env.code_root):
        run('bin/buildout -Nc deployment.cfg')


def supervisorctl(*cmd):
    """Runs an arbitrary supervisorctl command."""
    with cd(env.webserver):
        run('bin/supervisorctl ' + ' '.join(cmd), user=env.prod_user)
