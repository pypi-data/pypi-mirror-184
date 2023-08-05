from setuptools import setup, find_packages

setup(
    name='velait_django',
    version='0.0.1',
    license='LICENSE.md',
    packages=find_packages(),
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    requires=['django', 'djangorestframework'],
)
