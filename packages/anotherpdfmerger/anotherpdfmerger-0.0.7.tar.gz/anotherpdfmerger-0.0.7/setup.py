from setuptools import setup
from anotherpdfmerger.version import DESCRIPTION, NAME, VERSION


# Parse readme to include in PyPI page
with open('README.md') as f:
    long_description = f.read()

def capitalize(s):
    """Capitalize the first letter of a string.

    Unlike the capitalize string method, this leaves the other
    characters untouched.
    """
    return s[:1].upper() + s[1:]

setup(
    name=NAME,
    version=VERSION,
    description=capitalize(DESCRIPTION),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwiens91/anotherpdfmerger',
    author='Matt Wiens',
    author_email='mwiens91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
    ],
    data_files=[('/usr/local/man/man1', ['anotherpdfmerger.1']),],
    packages=['anotherpdfmerger'],
    entry_points={
        'console_scripts': ['anotherpdfmerger = anotherpdfmerger.anotherpdfmerger:main'],
    },
    python_requires='>=3',
    install_requires=[
        'PyPDF2',
    ],
)
