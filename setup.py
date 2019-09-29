# coding=utf-8
from macdash import __version__
from setuptools import setup, find_packages

setup(
    name='macdash',
    version=__version__,
    description='macOS system information web dashboard',
    long_description='Macdash is a system information web dashboard for macOS using data mainly served by psutil',
    classifiers=[
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Topic :: System :: Networking :: Monitoring',
        'Development Status :: 4 - Beta',
        'Environment:: MacOS X',
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Visualization',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Benchmark',
        'Topic :: System :: Monitoring',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ],
    keywords='macOS web dashboard',
    author='Michael Treanor',
    author_email='skeptycal@gmail.com',
    url='https://github.com/skeptycal/macdash',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'psutil',
        'gevent',
        'zerorpc',
        'netifaces',
    ],
    test_suite='tests',
    tests_require=['unittest2'],
    entry_points={
        'console_scripts': [
            'macdash = macdash.run:main'
        ]
    }
)
