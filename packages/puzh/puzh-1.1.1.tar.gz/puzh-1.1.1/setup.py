from setuptools import setup
from puzh import __version__


with open('README.rst') as file:
    readme = file.read()

setup(name='puzh',
      packages=['puzh'],
      version=__version__,
      author='lmittmann',
      description='Easily send messages to Telegram',
      long_description=readme,
      keywords=['puzh', 'push', 'telegram', 'bot', 'notification'],
      url='https://github.com/puzh/puzh.py',
      license='MIT',
      python_requires='>=3',
      install_requires=['requests>=2.19.1'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'])
