from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pboutil',
      version='0.1.1',
      description='Read and write ArmA PBO files.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://gitlab.com/arma3-server-tools/pboutil',
      author='Taneli Kaivola',
      author_email='dist@ihme.org',
      license='GPLv3',
      packages=['pboutil'],
      install_requires=[
          'construct >=2.9, <2.10',
          'arrow',
      ],
      classifiers=(
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Games/Entertainment :: First Person Shooters",
          "Topic :: System :: Archiving",
      ),
      zip_safe=True)

