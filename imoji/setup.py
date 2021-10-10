from setuptools import find_packages, setup

setup(
    name='imoji',
    packages=find_packages(include=['imoji']),
    version='0.1.0',
    description='A emoji lib for image manipulation which works with pillow library.',
    author='Caio Madeira',
    license='MIT',
    install_requires=['pillow'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'unittest'],
    test_suite='tests',
)