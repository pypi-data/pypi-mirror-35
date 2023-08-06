from setuptools import setup, find_packages

setup(
    name="qindomClient",
    version="0.1.0",
    packages=find_packages(),
    description= 'qindom client, add auth and extend method, params',
    classifiers=[
              'Programming Language :: Python :: 2'
          ],
    install_requires=['requests'],
    )
