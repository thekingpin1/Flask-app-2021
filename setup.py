from setuptools import setup

setup(
    name='Flask-app',
    version='1.0',
    long_description=__doc__,
    packages=['Flask-app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)

install_requires = [
    'Flask>=0.2',
    'SQLAlchemy>=0.6',
    'BrokenPackage>=0.7,<=1.0'
]
