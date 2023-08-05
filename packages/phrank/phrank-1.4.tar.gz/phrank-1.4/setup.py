from setuptools import setup, find_packages

setup(name='phrank',
      version='1.4',
      description='Measuring phenotype set similarity',
      url='https://bitbucket.org/bejerano/phrank/',
      author='Bejerano Lab',
      author_email='kjag@cs.stanford.edu',
      license='MIT',
      packages=find_packages(),
      scripts=['utils.py', '__init__.py'],
      zip_safe=False)
