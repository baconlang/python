from distutils.core import setup
setup(
    name='baclang',
    packages=['baclang'],
    version='v1.0.0',
    license='MIT',
    description='Python implementation of the BACLang compiler',
    author='Caleb Martinez',
    author_email='contact@calebmartinez.com',
    url='https://github.com/baclang/python',
    download_url='https://github.com/baclang/python/archive/v1.0.0.tar.gz',
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
