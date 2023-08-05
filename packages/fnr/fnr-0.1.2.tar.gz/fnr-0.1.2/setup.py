from setuptools import setup

with open("README.md", 'r') as ld:
    long_description = ld.read()

setup(
        name = 'fnr',
        version = '0.1.2',
        packages = ['fnr'],
        author = 'Collin Choy',
        author_email = 'collinchoyccc@gmail.com',
        description = 'A command line utility to find & replace text.',
        long_description=long_description,
        url='https://github.com/collincchoy/fnr',
        classifiers=[
            'Programming Language :: Python :: 3'
        ],
        test_suite = 'fnr.tests.fnrTests',
        setup_requires = ['nose>=1.0'],
        entry_points = {
            'console_scripts': [
                'fnr = fnr.fnr_cli:main'
            ]
        }
)
