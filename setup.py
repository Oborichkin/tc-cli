from setuptools import setup

setup(
    name='tcli',
    version='0.1',
    py_modules=['tcli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tcli=tcli.cli:main
    ''',
)
