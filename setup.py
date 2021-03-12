import setuptools

setuptools.setup(
    name='pytzstats',
    version='0.0.1',
    description='Python wrapper for Tzstats',
    long_description=open('README.md').read().strip(),
    author='IDerr',
    packages=['pytzstats'],
    install_requires=['requests'],
    license='MIT License',
)
