import sys
from setuptools import setup

def _get_file_content(file_name):
    with open(file_name, 'r') as file_handler:
        return file_handler.read()
def get_long_description():
    return _get_file_content('README.md')
def get_requirements():
    return list(filter(lambda line: line != '' and not line.startswith('#'), _get_file_content('requirements.txt').split('\n')))


setup(
    name="youtube-data-api",
    packages=['youtube_api'],
    py_modules=['youtube_api'],
    version='0.0.0.1',
    description="youtube-data-api is a Python wrapper for the YouTube Data API.",
    long_description=get_long_description(),
    author="leon yin, megan brown",
    author_email="",
    url="https://github.com/mabrownnyu/youtube-data-api",
    keywords='youtube data api, wrapper',
    license="MIT",
    install_requires=get_requirements()
)
