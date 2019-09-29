# coding=utf-8
from macdash import __version__
from setuptools import setup, find_packages
from build_manpages import build_manpages, get_build_py_cmd, get_install_cmd
from setuptools.command.build_py import build_py
from setuptools.command.install import install

setup(
    name='macdash',
    version=__version__,
    description='Linux system information web dashboard',
    long_description='macdash is a system information web dashboard for linux using data mainly served by psutil',
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
        'build_manpages',
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

# install_requires=[
#         'Flask==0.10.1',
#         'psutil==2.1.3',
#         'glob2==0.4.1',
#         'gevent==1.0.2',
#         'zerorpc==0.4.4',
#         'netifaces==0.10.4',
#         'argparse'
#     ],
