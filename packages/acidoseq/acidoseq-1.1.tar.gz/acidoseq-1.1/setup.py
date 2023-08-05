from setuptools import setup

with open("README", "r") as fh:
    long_description = fh.read()

setup(name='acidoseq',
      version='1.1',
      description='Studying Acidobacteria reads',
      url='https://github.com/sap218/acidoseq',
      author='Samanthe C Pendle',
      author_email='samanfapendle@outlook.com',
      license='MIT',
      packages=["acidoseq","map"],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
      zip_safe=False
)
