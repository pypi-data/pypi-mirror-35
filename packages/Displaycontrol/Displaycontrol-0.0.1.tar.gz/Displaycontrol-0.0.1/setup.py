from distutils.core import setup

setup(
    name='Displaycontrol',
    version='0.0.1',
    packages=['displaycontrol'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Package to control displays and projectors via serial and ethernet connection.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TopRedMedia/displaycontrol',
    author='Mirko Haaser',
    author_email='mirko@topred.media',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)
