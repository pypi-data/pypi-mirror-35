try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='bitcoinaverage',
    packages=['bitcoinaverage', # this must be the same as the name above
              'bitcoinaverage.clients',
              'bitcoinaverage.examples'],
    version='0.2',
    description='Library to integrate with the BitcoinAverage API',
    author='Blockchain Data LTD',
    author_email='info@bitcoinaverage.com',
    keywords=['bitcoinaverage', 'bitcoin', 'api'],  # arbitrary keywords
    classifiers=[],
    install_requires=[
        "requests",
        "six",
        "itsdangerous",
        "ws4py"
    ]
)
