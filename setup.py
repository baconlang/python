from distutils.core import setup

setup(
    name='baclang',
    long_description_content_type='text/markdown',
    packages=['baclang'],
    version='v1.0.6',
    license='MIT',
    description='Python implementation of the BACLang interpreter',
    long_description='''
    BAClang is a logical programming language dedicated to evaluating constraint based expressions using only strings and square brackets. This package allows for:
    - Parsing of valid BACs using either symbol maps or evaluators
    - Generation of all possible symbol maps for a given constraint
    - Generation of all satisfactory symbol maps for a given constraint
    ''',
    author='Caleb Martinez',
    author_email='contact@calebmartinez.com',
    url='https://github.com/baclang/python',
    project_urls={
        'Source Code': 'https://github.com/baclang/python',
    },
    download_url='https://github.com/baclang/python/archive/v1.0.6.tar.gz',
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
