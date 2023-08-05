from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="pydotfiles",
    version="0.0.0",
    author="Jason Yao",
    author_email="Hello@JasonYao.com",
    description="Fast, easy, and automatic system configuration via a configuration file/repo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JasonYao/pydotfiles",
    packages=find_packages(exclude=("git", "bin")),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",

        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: System :: Systems Administration",

        # Supported python environments
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",

        # Supported operating systems
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    license="GPLv3",

    project_urls={
        'Bug Reports': 'https://github.com/JasonYao/pydotfiles/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/JasonYao/pydotfiles',
    },

    # Installation dependencies below
    # install_requires=['docutils>=0.3'],

    # scripts=['bin/dotfiles'],
    zip_safe=True,
    python_requires='>=3.6',
    extra_require={
        'dev': [
            'pyest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }

)
