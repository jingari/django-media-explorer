#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

from media_explorer import __version__ as version

with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-media-explorer',
    version=version,
    description='Encode and upload multimedia from the Django admin interface',
    long_description=readme,
    license='MIT',
    author='Kofi Bosque-Hamilton',
    author_email='koficharlie@gmail.com',
    url='https://github.com/oxfamamerica/django-media-explorer-coming-soon',
    download_url='https://pypi.python.org/pypi/django-media-explorer/',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data = { 'assets': [] },
    zip_safe=False,
    install_requires=[
        'django<1.7',
        'micawber==0.3.2',
        'djangorestframework==2.4.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['multimedia', 'media', 'video', 'gallery'],
)
