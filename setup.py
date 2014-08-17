from setuptools import setup

setup(
    name='pyomxplayer',

    author='Will Price',
    author_email='will.price94+py@gmail.com',

    version='0.1',

    description='Control OMXPlayer on the Raspberry Pi',
    long_description='Control OMXPlayer on the Raspberry Pi through DBus',

    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Video',
        'Programming Lnaguage :: Python :: 2'
    ],

    keywords='omxplayer, raspberry_pi, library',

    packages=['pyomxplayerng'],
    install_requires=[],
)