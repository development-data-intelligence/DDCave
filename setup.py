from setuptools import setup

setup(
    name='cave',
    version='0.1',
    install_requires=[
        'Flask',
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cave=governor:cli'
        ],
    },
)
