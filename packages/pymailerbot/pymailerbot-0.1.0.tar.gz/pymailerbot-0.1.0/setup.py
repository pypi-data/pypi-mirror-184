from setuptools import setup

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Developers',
  'Operating System :: Windows :: Windows 10 :: MacOS :: MacOS X :: Linux',
  'Programming Language :: Python :: 3'
]

setup(
    name='pymailerbot',
    version='0.1.0',
    description='The python3 emailer bot for internal uses.',
    url='https://github.com/unbxd/pymailerbot',
    author='Tushar Gupta',
    author_email='tushar.gupta@unbxd.com',
    py_modules=['emailer'],
)