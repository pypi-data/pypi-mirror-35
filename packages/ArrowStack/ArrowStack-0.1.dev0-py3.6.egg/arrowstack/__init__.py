import sys
import os, os.path
import pymist
import importlib
from runpy import run_path
import docker
from jinja2 import Template


def main():
    args = pymist.parse(sys.argv[1:])
    cwd = os.getcwd()
    lib_path = os.path.dirname(os.path.realpath(__file__))

    _ = args.get('_')
    if not len(_):
        print('Expected command name. Please, use following format: "arrowstack <command> [args]')
        return
    if _[0] == 'deploy':
        deployfilename = args.get('f') if args.get('f') else 'deploy.py'
        print(deployfilename)
        module_path = os.path.join(cwd, deployfilename)

        if os.path.exists(module_path):
            settings = run_path(module_path)
            print(settings.get('docker'))
        else:
            print('No deploy.py file found')

        # docker.DockerClient()
    elif _[0] == 'dockerfile':
        with open(os.path.join(lib_path, 'Dockerfile.tpl'), 'r') as f:
            template = Template(f.read())
            result = template.render(name='John Doe')
            print(result)
