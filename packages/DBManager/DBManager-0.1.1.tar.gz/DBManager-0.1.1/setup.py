from setuptools import setup
import dbmanager

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name="DBManager",
      author=dbmanager.__author__,
      url="https://github.com/LeCuay/DBManager.py",
      description="Make Database Managing easier!",
      version=dbmanager.__version__,
      long_description=readme,
      long_description_content_type="text/markdown",
      packages=['dbmanager'],
      classifiers=
      [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
      ]
    )
