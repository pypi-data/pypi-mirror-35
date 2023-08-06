#!/usr/bin/env python

"""jenkenv

Usage:
  jenkenv list
  jenkenv run <jenkinsfile> [<version>]
  jenkenv run-jenkins [<version>]
  jenkenv use <scope> <version>
  jenkenv install (-l|<version>)
  jenkenv uninstall <version>
  jenkenv (-h | --help)
  jenkenv --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

import atexit, time, sys
from html.parser import HTMLParser
from shutil import rmtree
from subprocess import Popen, PIPE, STDOUT
import urllib.request, os, re
import zipfile


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = os.getcwd()
JENKENV_DIR = os.path.expanduser('~/.jenkenv')
RUNNER_PATH = f'{ROOT_DIR}/jenkinsfile-runner/app/target/appassembler/bin/jenkinsfile-runner'
DOWNLOAD_URL = 'https://updates.jenkins-ci.org/download/war'

processes = list()

'''parser.py'''

class VersionParser(HTMLParser):

    regex = r'war/(\d+\.\d+)/jenkins.war'

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href  = attrs[0][1]
            match = re.search(VersionParser.regex, href)
            if match:
                print(match.group(1))

'''clean.py'''

def cleanup():
    timeout_sec = 10
    for p in processes:
        p_sec = 0
        for second in range(timeout_sec):
            if p.poll() == None:
                time.sleep(1)
                p_sec += 1
        if p_sec >= timeout_sec:
            p.kill()

atexit.register(cleanup)

def check():
    if not os.path.isdir(JENKENV_DIR):
        print(f'{JENKENV_DIR} is not present; creating now...')
        os.mkdir(JENKENV_DIR)

def list_installed():
    installed = os.listdir(JENKENV_DIR)
    if not installed:
        print('no jenkins.war files installed')
    else:
        print('installed versions:')
        print('\n'.join(installed))

def _version():
    if os.path.isfile('.jenkins_version'):
        return open('.jenkins_version').read()
    elif os.path.isfile(f'{JENKENV_DIR}/.jenkins_version'):
        return open(f'{JENKENV_DIR}/.jenkins_version').read()

def sh(command):
    p = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, bufsize=1)
    processes.append(p)
    for line in iter(p.stdout.readline, b''):
        print(line.decode().strip())
    p.stdout.close()
    exit(p.wait())

def run(jenkinsfile, version=None):
    version = version or _version()
    if not version:
        raise Exception('version must be specified')
    if not os.path.isabs(jenkinsfile):
        jenkinsfile = f'{USER_DIR}/{jenkinsfile}'
    path = f'{JENKENV_DIR}/{version}'
    sh(f'{RUNNER_PATH} -w {path}/jenkins -p {path}/jenkins_home/plugins -f {jenkinsfile}')

def run_jenkins(version=None):
    version = version or _version()
    if not version:
        raise Exception('version must be specified')
    path = f'{JENKENV_DIR}/{version}'
    os.environ['JENKINS_HOME'] = f'{path}/jenkins_home'
    sh(f'java -jar {path}/jenkins.war')

def use(scope, version):
    path = f'{JENKENV_DIR}/.jenkins_version'
    if scope == 'local':
        path = f'{USER_DIR}/.jenkins_version'
    print(f'setting version at {path}')
    with open(path, 'w') as version_file:
        version_file.write(version)

def list_available():
    resp = urllib.request.urlopen(DOWNLOAD_URL)
    parser = VersionParser()
    parser.feed(str(resp.read()))

def _unzip_war(version):
    path = f'{JENKENV_DIR}/{version}'
    zip_ref = zipfile.ZipFile(f'{path}/jenkins.war', 'r')
    zip_ref.extractall(f'{path}/jenkins')
    zip_ref.close()

def install(version):
    print(f'installing jenkins-{version}...')
    url = f'{DOWNLOAD_URL}/{version}/jenkins.war'
    path = f'{JENKENV_DIR}/{version}'
    if not os.path.isdir(path):
        os.mkdir(path)
    urllib.request.urlretrieve(url, f'{path}/jenkins.war')
    _unzip_war(version)
    print(f'installed jenkins-{version} to {path}')

def uninstall(version):
    print(f'uninstalling jenkins-{version}...')
    path = f'{JENKENV_DIR}/{version}'
    rmtree(path)
    print(f'uninstalled jenkins-{version}')

def main():
    args = docopt(__doc__, version='0.0.1')
    check()
    if args['list']:
        list_installed()
    elif args['run']:
        run(args['<jenkinsfile>'], args['<version>'])
    elif args['run-jenkins']:
        run_jenkins(args['<version>'])
    elif args['use']:
        use(args['<scope>'], args['<version>'])
    elif args['install']:
        if args['-l']:
            list_available()
        else:
            install(args['<version>'])
    elif args['uninstall']:
        uninstall(args['<version>'])


if __name__ == '__main__':
    main()
