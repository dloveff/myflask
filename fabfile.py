#coding:utf-8
__author__ = 'dong'

from fabric.api import *

env.hosts = ['192.168.23.132']
env.user = 'dong'
env.password = 'dong'

def hello():
    print ('by dong')

def deploy():
    with cd('/home/dong/public/myflask'):
        run('git pull')
        sudo('supervisorctl restart app')
        sudo('supervisorctl status')