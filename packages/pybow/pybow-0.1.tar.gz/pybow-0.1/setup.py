#!/usr/bin/env python3
from setuptools import setup, find_packages


# TODO:
# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='pybow', # Req
    # PEP 440
    version='0.1', # Req
    description='A collection of archery-focused calculation methods', # Req

    long_description=long_description, # Opt
    long_description_content_type='text/markdown', # Opt
    # valid values: text/plain, text/x-rst, and text/markdown
    url='https://gitlab.com/gekitsu/pybow', # Optional
    author='R. Kretz', # Optional
    # author_email='pypa-dev@googlegroups.com', # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='archery archaeology bowyery', # Opt

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(),  # Req

    install_requires=[
        'numpy',
        'pandas',
        'ruamel.yaml'
        ], # Opt

    extras_require={ # Opt
        'dev': ['sphinx'],
        'test': ['pytest'],
    },

    #package_data={  # Optional
        #'sample': ['package_data.dat'],
    #},

    #data_files=[('my_data', ['data/data_file'])],  # Optional

    entry_points={ # Opt
        'console_scripts': [
            'pybow=pybow.cli:pybow_cli',
        ],
    },

    #project_urls={  # Optional
        #'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        #'Funding': 'https://donate.pypi.org',
        #'Say Thanks!': 'http://saythanks.io/to/example',
        #'Source': 'https://github.com/pypa/sampleproject/',
    #},
)
