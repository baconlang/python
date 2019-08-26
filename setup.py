from distutils.core import setup

setup(
    name='baconlang',
    long_description_content_type='text/markdown',
    packages=['baconlang'],
    version='1.0.7',
    license='MIT',
    description='Python implementation of the BAConLang interpreter',
    long_description='''
    BAConlang is a logical programming language dedicated to evaluating constraint based expressions using only strings and square brackets. This package allows for:
    - Parsing of valid BACs using either symbol maps or evaluators
    - Generation of all possible symbol maps for a given constraint
    - Generation of all satisfactory symbol maps for a given constraint
    ''',
    author='Caleb Martinez',
    author_email='contact@calebmartinez.com',
    url='https://github.com/baconlang/python',
    project_urls={
        'Source Code': 'https://github.com/baconlang/python',
    },
    download_url='https://github.com/baconlang/python/archive/1.0.7.tar.gz',
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
