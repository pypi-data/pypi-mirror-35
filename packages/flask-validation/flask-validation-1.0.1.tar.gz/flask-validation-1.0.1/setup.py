from setuptools import setup

setup(
    name='flask-validation',
    description='A Pythonic way for validate requested JSON payload of Flask',
    version='1.0.1',
    url='https://github.com/callsign-viper/Flask-Validation',
    license='Apache License 2.0',
    author='PlanB, devArtoria',
    author_email='mingyu.planb@gmail.com',
    maintainer='PlanB, devArtoria',
    maintainer_email='mingyu.planb@gmail.com',
    install_requires=[
        'Flask',
        'jsonschema'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=['flask_validation']
)
