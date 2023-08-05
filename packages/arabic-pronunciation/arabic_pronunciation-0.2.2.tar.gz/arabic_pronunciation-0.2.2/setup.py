from os import path

from setuptools import setup

def readme():
    with open('README.md', encoding="utf-8") as f:
        return f.read()

setup(
    name='arabic_pronunciation',
    version="0.2.2",
    description='Pronounce Arabic words on the fly',
    long_description=readme(),
    author='Youssef Sherif',
    author_email='sharief@aucegypt.edu',
    url='https://github.com/youssefsharief/arabic_pronunciation.git',
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
    )
)
