from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Unix101',
    version='1.5.2',
    author="Bijinepalli Surat Dhani",
    author_email="bdhanirs26@gmail.com",
    description="A package to manage Unix commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdhani/unix101.git",
    packages=find_packages(),
    install_requires=[
        'certifi',
        'click',
        'colorama',
        'Django',
        'idna',
        'markdown-it-py',
        'mdurl',
        'mysql-connector-python',
        'mysqlclient',
        'Pygments',
        'rich',
        'shellingham',
        'sqlparse',
        'typer',
        'typing_extensions',
        'tzdata',
        'urllib3',
    ],
    extras_require={
        "dev":["twine>=4.0.2"]
    },
    entry_points={
        'console_scripts': [
            'unix101 = commands.richtyper:app'
        ]
    },
    python_requires='>=3.7',
)
