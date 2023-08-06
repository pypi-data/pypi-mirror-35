import os, sys, re

HOME_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(HOME_DIR, 'waelstow.py'))

# get version info from module without importing it
version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")

with open('waelstow.py') as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)

readme = os.path.join(HOME_DIR, 'README.rst')
long_description = open(readme).read()


SETUP_ARGS = dict(
    name='waelstow',
    version=version,
    description=('A small collection of tools for unit testing.  Includes '
        'methods for test suite discovery for use in your runner and contexts '
        'for capturing STDIO or STDERR and temporarily moving directories.'),
    long_description=long_description,
    url='https://github.com/cltrudeau/waelstow',
    author='Christopher Trudeau',
    author_email='ctrudeau+pypi@arsensa.com',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='test,testing,unit test,unittest,test runner',
    test_suite='load_tests.get_suite',
    py_modules = ['waelstow',],
    install_requires = [
        'six>=1.11',
    ],
    not_an_argument=True,
)

if __name__ == '__main__':
    from setuptools import setup
    setup(**SETUP_ARGS)
