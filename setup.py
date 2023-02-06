from setuptools import setup


setup(
    name='pygelf-ex',
    version='0.0.1',
    packages=['pygelf-ex'],
    description='Logging handlers with GELF support',
    keywords='logging udp tcp ssl tls graylog2 graylog gelf',
    author='Ivan Mukhin, Anders Ågren',
    author_email='muhin.ivan@gmail.com, anders.agren@rssoftware.se',
    url='https://github.com/rs-anders-agren/pygelf-ex',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Logging',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
