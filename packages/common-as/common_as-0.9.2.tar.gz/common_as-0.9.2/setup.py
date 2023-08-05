from setuptools import setup

setup(
    name='common_as',
    version='0.9.2',
    description='common modules used in Arthasangraha suite of projects',
    author='Arthasangraha',
    author_email='roopesh@arthasangraha.com',
    packages=['src'],
    install_requires=[
        'ta-lib', 'pandas', 'numpy'
    ],
)
