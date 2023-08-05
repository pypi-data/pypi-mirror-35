from setuptools import setup, find_packages

setup(
    name='aiogql',
    version='1.1.0',
    description='A fork of gql which uses asyncio & aiohttp for execution',
    long_description=open('README.rst').read(),
    url='https://github.com/cipriantarta/aiogql',
    author='Ciprian Tarta',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='api graphql protocol rest relay gql client',
    packages=find_packages(include=["aiogql*"]),
    install_requires=[
        'six>=1.10.0',
        'graphql-core>=2.0',
        'promise>=0.4.0',
        'aiohttp>=3.1.3',
    ],
    tests_require=['pytest>=3.5', 'mock'],
)
