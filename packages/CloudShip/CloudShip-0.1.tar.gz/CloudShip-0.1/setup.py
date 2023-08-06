from setuptools import setup

setup(
    name="CloudShip",
    version='0.1',
    py_modules=['shipment'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        CloudShip=cli:cli
    ''',
)