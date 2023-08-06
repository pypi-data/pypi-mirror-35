import setuptools

setuptools.setup(
    name='galaxy_dive',
    version='0.8.1',
    description='A general analysis suite for hydrodynamic galaxy simulations.',
    url='https://github.com/zhafen/galaxy-dive',
    author='Zach Hafen',
    author_email='zachary.h.hafen@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
)
