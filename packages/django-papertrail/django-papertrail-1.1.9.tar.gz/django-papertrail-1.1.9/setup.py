import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-papertrail',
    version='1.1.9',
    packages=['papertrail'],
    install_requires=[
        'Django>=1.10,<2.0;python_version<"3.0"',
        'Django>=1.10;python_version>"3.0"',
        'six',
        'django-apptemplates',
    ],
    include_package_data=True,
    license='Apache Software License',
    description='An elegant solution for keeping a relational log of chronological events in a Django application.',
    long_description=README,
    url='https://www.github.com/FundersClub/django-papertrail',
    author='Eran Rundstein / FundersClub Inc.',
    author_email='eran@fundersclub.com',
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
