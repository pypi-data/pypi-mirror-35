from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
        name='nnlib',
        version='0.2',
        description='numpy only neural network library',
        long_description=readme(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Intended Audience :: Developers',
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Artificial Intelligence'
            ],
        keywords='machine learning neural network',
        author='Felix Zhou',
        author_email='felix990302@yahoo.ca',
        license='Apache2',
        url='https://github.com/felix990302/nnlib',
        packages=find_packages(),
        install_requires=[
            'numpy>=1.15.0'
            ]
        )
