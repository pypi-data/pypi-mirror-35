#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='qitian-django-starting',
    description=(
        'Qitian django web project basic apps '
        'quick setup usercenter system sites and so on.'
    ),
    version='0.0.1',
    author='Peter Han',
    author_email='peter@qitian.com',
    url='https://gitee.com/qtch/starting_django_framework',
    license='MIT License',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'Django>=2.0',
        'pycryptodomex==3.6.5',
        'django-js-asset==1.1.0',
        'django-mptt==0.9.1',
        'django-smart-selects==1.5.3',
        'django-uuslug==1.1.8',
        'easy-thumbnails==2.5',
        'textrank4zh==0.3',
        'yunpian-python-sdk==1.0.0',
        'urllib3==1.23',
        'beautifulsoup4==4.6.0',
        'environ==1.0',
        'shortuuid==0.5.0',
    ],
    python_requires=">=3.6, !=3.0.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Utilities',
    ],
)
