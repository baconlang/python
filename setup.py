from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='baclang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['baclang'],
    version='v1.0.3',
    license='MIT',
    description='Python implementation of the BACLang interpreter',
    author='Caleb Martinez',
    author_email='contact@calebmartinez.com',
    url='https://github.com/baclang/python',
    download_url='https://github.com/baclang/python/archive/v1.0.3.tar.gz',
    keywords=['language', 'interpreter', 'constraint', 'logic'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
