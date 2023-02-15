from setuptools import setup, find_packages

setup(
    name='app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.1.0',
        'Flask-Cors==3.0.10'
    ]
)
