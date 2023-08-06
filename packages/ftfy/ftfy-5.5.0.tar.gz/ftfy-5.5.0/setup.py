from setuptools import setup
import sys


PY2_MESSAGE = """
Sorry, this version of ftfy is no longer written for Python 2.

It is much easier to provide consistent handling of Unicode when developing
only for Python 3. ftfy is exactly the kind of library that Python 3 is
designed for, and now there is enough Python 3 usage that we can take advantage
of it and write better, simpler code.

The older version of ftfy, version 4.4, is still available and can run on
Python 2. Try this:

    pip install ftfy==4.4.3
"""

DESCRIPTION = open('README.md', encoding='utf-8').read()


if sys.version_info[0] < 3:
    print(PY2_MESSAGE)
    sys.exit(1)


setup(
    name="ftfy",
    version='5.5.0',
    maintainer='Luminoso Technologies, Inc.',
    maintainer_email='info@luminoso.com',
    license="MIT",
    url='http://github.com/LuminosoInsight/python-ftfy',
    platforms=["any"],
    description="Fixes some problems with Unicode text after the fact",
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['ftfy', 'ftfy.bad_codecs'],
    package_data={'ftfy': ['char_classes.dat']},
    install_requires=['wcwidth'],
    tests_require=['pytest'],
    python_requires='>=3.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Development Status :: 5 - Production/Stable"
    ],
    entry_points={
        'console_scripts': [
            'ftfy = ftfy.cli:main'
        ]
    },
    project_urls={
        'Documentation': 'http://ftfy.readthedocs.io',
    }
)
