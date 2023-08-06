from setuptools import setup

# dependencies = [p.rstrip('\n') for p in open('requirements/requirements.txt')]

setup(
    name='trawler',
    version='1.3.6',
    packages=['trawler', 'trawler.browsers', 'tests' ],
    url='https://github.com/rrmerugu/trawler',
    license='',
    author='Ravi RT Merugu',
    author_email='rrmerugu@gmail.com',
    description='A data gathering framework to search and get information from web sources',
    install_requires=[
        'cssselect==1.0.1',
        'lxml==4.1.0',
        'selenium==3.6.0',
        'six==1.11.0',
        'beautifulsoup4==4.6.0',
        'requests==2.18.4',
        'user-agent==0.1.9'
    ],
)