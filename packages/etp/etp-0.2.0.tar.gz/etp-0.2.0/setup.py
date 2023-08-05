import setuptools

with open("README.markdown", "r") as fh:
    long_description = fh.read()


setuptools.setup(
      name='etp',
      version='0.2.0',
      description='A ThreadPool extension',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/dobbleg1000/enhanced_threadpool',
      author='DobbleG1000',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
      ],
      zip_safe=False)
