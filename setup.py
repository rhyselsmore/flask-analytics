from setuptools import setup

requires = ['requests','flask']

setup(
    name='flask-analytics',
    description='Analytics Collector.',
    author='Not the NSA',
    author_email='rjones@nsa.gov',
    py_modules=['flask_analytics'],
    install_requires=requires,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)