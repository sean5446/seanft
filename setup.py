from setuptools import setup, find_packages

setup(
    name='seanft',
    version='1.0.0',
    url='https://google.com',
    author='sean5446',
    author_email='author@gmail.com',
    description='A game server',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests',
        'gunicorn',
        'trdg',
    ],
)

