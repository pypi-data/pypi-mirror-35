from setuptools import setup

setup(
    name='opsworks-cli',
    description='A simple python module to work with aws opsworks',
    url='https://github.com/chaturanga50/opsworks-cli',
    author='Chathuranga Abeyrathna',
    author_email='chaturanga50@gmail.com',
    package_data={'someproject': ['modules/*.py']},
    version='0.2',
    scripts=['opsworks-cli']
)
