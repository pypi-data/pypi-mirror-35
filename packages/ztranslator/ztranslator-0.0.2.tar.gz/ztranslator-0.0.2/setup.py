from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ztranslator',
    version='0.0.2',
    description='translator.',
    long_description=readme(),
    keywords='translator tradutor',
    platforms=['Linux'],
    author='andreztz',
    author_email='andreztz@gmail.com',
    url='https://github.com/andreztz/ztranslator',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={'console_scripts': ['ztranslator=translator.__main__:main'],}
)
