from setuptools import setup

setup(
    name='sudokucli',
    version='0.1.2',
    author="a2htray",
    author_email="a2htray.yuen@gmail.com",
    description="Console 9*9 Sudoku Game",
    long_description=open("README.rst").read(),
    license="Apache License 2.0",
    url="https://github.com/a2htray/sudoku-cli",
    packages=[
        'src',
        'src.commands',
        'src.abs'
    ],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        sudokucli=src.cli:cli
    ''',
    zip_safe=True
)