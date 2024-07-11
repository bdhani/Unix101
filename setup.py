from setuptools import setup, find_packages

setup(
    name='Unix101',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'asgiref==3.8.1',
        'certifi==2024.6.2',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'colorama==0.4.6',
        'Django==5.0.6',
        'idna==3.7',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'mysql-connector-python==8.4.0',
        'mysqlclient==2.2.4',
        'Pygments==2.18.0',
        'rich==13.7.1',
        'shellingham==1.5.4',
        'sqlparse==0.5.0',
        'typer==0.12.3',
        'typing_extensions==4.12.2',
        'tzdata==2024.1',
        'urllib3==2.2.1',
    ],
    entry_points={
        'console_scripts': [
            'richtyper = commands.richtyper:app'
        ]
    },
)
