from setuptools import setup, find_packages

setup(
    name='ArrowStack',
    version='0.1dev',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'arrowstack = arrowstack:main'
        ]
    },
    install_requires=[
        'routes',
        'webob',
        'docker',
        'pymist',
        'gunicorn',
        'Jinja2'
    ]
)
