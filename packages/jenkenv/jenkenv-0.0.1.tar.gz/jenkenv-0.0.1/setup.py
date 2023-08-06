from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name='jenkenv',
    author='jamesrobertalbert@gmail.com',
    version='0.0.1',
    url='https://github.com/jamesalbert/jenkenv',
    packages=['jenkenv'],
    # package_data={'jenkenv': ['jenkinsfile-runner']},
    include_package_data=True,
    install_requires=[
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'jenkenv=jenkenv.__init__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
