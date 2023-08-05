"""Setup Script"""
import setuptools


def readme():
    # type: () -> str
    """Load README.md

    Returns:
        str -- contents of README
    """
    with open("README.md", "r") as fp:  # pylint: disable=invalid-name
        return fp.read()


setuptools.setup(
    name='kinda',
    version='0.9.9',
    author='Andrew Champion',
    author_email='awchampion@gmail.com',
    description='A pythonic library for floating point number comparison',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/schmamps/Kinda/',
    packages=['kinda'],
    keywords=['floating point', 'comparison'],
    scripts=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
