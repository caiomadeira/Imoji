from setuptools import find_packages, setup

classifiers = [
    'status :: BETA/unstable',
    'Operating System :: Microsoft :: Windows :: Windows 10 and above',
    'Porgramming Language :: Python :: 3'
]

setup(
    name='imoji',
    packages=find_packages(include=['imoji']),
    version='0.9.0',
    description='A emoji lib for image manipulation which works with pillow library.',
    url='',
    classifiers=classifiers,
    keywords='',
    author='Caio Madeira',
    license='MIT',
    install_requires=['pillow',],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'unittest'],
    test_suite='tests',
)
