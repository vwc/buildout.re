from fabric.api import task
from fabric.api import cd
from fabric.api import env
from fabric.api import run

from ade25.fabfiles import project

env.use_ssh_config = True
env.forward_agent = True
env.port = '22222'
env.user = 'root'
env.hosts = ['6zu4']
env.webserver = '/opt/webserver/buildout.webserver'
env.code_root = '/opt/sites/buildout.re'
env.local_root = '/Users/cb/dev/erben/buildout.re'
env.sitename = 'plonesite'
env.code_user = 'root'
env.prod_user = 'www'


def supervisorctl(*cmd):
    """Runs an arbitrary supervisorctl command."""
    with cd(env.webserver):
        run('bin/supervisorctl ' + ' '.join(cmd))


@task
def deploy():
    """ Deploy current master to production server """
    project.site.update()
    project.site.estart()


@task
def deploy_full():
    """ Deploy current master to production and run buildout """
    project.site.update()
    project.site.build()
    project.site.restart()


@task
def rebuild():
    """ Deploy current master and run full buildout """
    project.site.update()
    project.site.build_full()
    project.site.restart()
