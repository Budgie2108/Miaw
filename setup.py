import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

RM = (HERE / "README.md").read_text()
from setuptools import setup
setup(name='Miaw',
      version='0.1',
      description='A module full of functions',
      url='https://github.com/RobDaMob/Kitten/',
      author='Rob The Mob',
      author_email='RobWork@gmail.com',
      license='MIT',
      packages=['Miaw'],
      zip_safe=False,
      long_description=RM,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=["os", "time", "sys"])
