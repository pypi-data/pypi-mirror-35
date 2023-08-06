import setuptools
from setuptools import setup

setup(
    name='carball',
    version='0.1.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pandas==0.23.4', 'protobuf==3.6.1'],
    url='https://github.com/SaltieRL/ReplayAnalysis',
    keywords=['rocket-league'],
    license='Apache 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    author='Matthew Mage, Harry Xie, David Turner',
    author_email='sciguymjm@gmail.com',
    description='Rocket League replay parsing and analysis.',
    exclude_package_data={'': ['.gitignore', '.git/*', '.git/**/*', 'replays/*']}
)
