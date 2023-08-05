from distutils.core import setup
from setuptools import find_packages

with open('VERSION', 'r') as f:
    version = f.readline().strip()

with open('requirements.txt', 'r') as f:
    install_requires = list()
    for line in f:
        re = line.strip()
        if re:
            install_requires.append(re)

packages = find_packages()

setup(
    name='rltk',
    version=version,
    packages=packages,
    url='https://github.com/usc-isi-i2/rltk',
    license='MIT',
    author='USC/ISI',
    author_email='',
    description='Record Linkage ToolKit',
    include_package_data=True,
    install_requires=install_requires
)
