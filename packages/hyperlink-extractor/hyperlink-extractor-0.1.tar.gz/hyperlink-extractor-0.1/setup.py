from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requires = [l.strip() for l in f.readlines()]


setup(
    name='hyperlink-extractor',
    version='0.1',
    description='Simple html link extractor.',
    author='Sinan Nalkaya',
    author_email='sardok@gmail.com',
    url='https://github.com/sardok/hyperlink-extractor',
    install_requires=requires,
    packages=find_packages(exclude=('tests',)),
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
