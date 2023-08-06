from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='photoarchive',
      version='0.5',
      description='A simple tool to archive photos',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/roseeng/photoarchive',
      author='Göran Roseen',
      author_email='goran@roseen.se',
      license='MIT',
      packages=['photoarchive'],
      install_requires=[
          'piexif',
      ],
      zip_safe=False,      
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
