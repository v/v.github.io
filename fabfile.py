from fabric.api import local, env, hosts
from fabric.operations import run, put

def build():
    local('jekyll build')

@hosts('vverna@vi.cs.rutgers.edu')
def ilab():
    put('_site/*', '/ilab/users/vverna/public_html')

@hosts('vverna@vverma.net')
def site():
    put('_site/*', '/var/www/servers/vverma.net')

@hosts('vv@new.vverma.net')
def do():
    put('_site/*', '/var/www/servers/vverma.net')
