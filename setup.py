f = open(README)
LD = f.read()
from setuptools import setup
setup(name='Miaw',
      version='0.1',
      description='A module full of functions',
      url='https://github.com/RobDaMob/Kitten/',
      author='Rob The Mob',
      author_email='RobWork@gmail.com',
      license='MIT',
      packages=['Kitty'],
      zip_safe=False,
      long_description=LD,
      long_description_content_type="text/markdown")
