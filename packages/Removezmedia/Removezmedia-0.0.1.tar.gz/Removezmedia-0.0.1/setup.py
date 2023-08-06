import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Removezmedia",
    version = "0.0.1",
    author = "Florian Bernard",
    author_email = "florianxbernard@gmail.com",
    description = ("An application to remove file and folder in a given directory for a given treshold "),
    license = "MIT",
    keywords = "filemanagement, datetime",
    url = "https://github.com/Hatoris/RemoveMedia",
    project_urls={ 'Documentation': 'https://hatoris.github.io/RemoveMedia/html/index.html',
                   'Source': 'https://github.com/Hatoris/RemoveMedia'},
    packages=['RemoveMedia', 'RemoveMedia/configuration'],
    install_requires=[
        'pendulum>=2.0.2',
        'fire>=0.1.3',
    ],
    long_description=read('README.rst'),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
    ],
)
