from setuptools import setup, find_packages

setup(
    name='db_tools',
    packages=find_packages(),
    install_requires=['SQLAlchemy'],
    entry_points='''\
    [console_scripts]
    veritable-db-tools=db_tools.extract_schema:main
    '''
)