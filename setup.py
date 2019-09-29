# coding=utf-8
from macdash import __version__
from setuptools import setup, find_packages
from Cython.Build import cythonize


setup(
    name='macdash',
    version=__version__,
    description='macOS system information web dashboard',
    long_description='Macdash is a system information web dashboard for macOS using data mainly served by psutil',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment:: MacOS X',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Benchmark',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities'
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
        'gevent',
        'netifaces',
        'psutil',
        'zerorpc',
    ],
    test_suite='tests',
    tests_require=['unittest2'],
    entry_points={
        'console_scripts': [
            'macdash = macdash.run:main'
        ]
    }
)
