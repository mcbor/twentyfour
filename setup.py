from setuptools import setup, find_packages

setup(
    name='twentyfour',
    version='0.1',
    packages=find_packages(),
    include_packages_data=True,
    install_requires=[
        'click>=6.7,<7.0'
    ],
    entry_points='''
        [console_scripts]
        twentyfour=twentyfour:main
    '''
)
