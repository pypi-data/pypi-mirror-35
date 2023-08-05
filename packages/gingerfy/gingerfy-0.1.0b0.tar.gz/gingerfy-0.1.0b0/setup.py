import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='gingerfy',
      version='0.1.0-beta',
      description='Remove broken colours from strings and replace them with the one true colour, GINGER!!',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/RobDWaller/gingerfy',
      author='RobDWaller',
      author_email='rdwaller1984@googlemail.com',
      license='MIT',
      packages=setuptools.find_packages(exclude=['tests*']),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ])
