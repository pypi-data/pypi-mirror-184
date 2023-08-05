from setuptools import setup, find_packages

setup(
    name='huntydata',
    packages=find_packages(),
    version='0.2.0',
    author='Hunty Data Team: Diegui Lesmes, Santi R ft.Andrew Ferreira',
    url='https://github.com/Huntyjobs/data_library',
    project_urls={"Bug Tracker": "https://github.com/Huntyjobs/data_library/issues"},
    description='Contains functions that are useful for daily programing problems in Hunty operation',
    long_description='Contains functions that are useful for daily programing problems in Hunty operation',
    install_requires=['pandas','requests','numpy','python-dotenv'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)



