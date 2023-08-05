from setuptools import setup


setup(
        name='nnlib',
        version='0.1',
        description='numpy only neural network library',
        author='Felix Zhou',
        author_email='felix990302@yahoo.ca',
        license='Apache2',
        url='https://github.com/felix990302/nnlib',
        packages=['nnlib'],
        install_requires=[
            'numpy>=1.15.0'
            ]
        )
