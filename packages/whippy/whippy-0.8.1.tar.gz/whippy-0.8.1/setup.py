from setuptools import setup, find_packages

setup(name='whippy',
      version='0.8.1',
      description='Rapidly scaffold WordPress sites on Linux NGINX servers from the command line. Unrelated to the wppy'\
                  ' project, although both fill the same hole.',
      url='https://github.com/erikcaineolson/whippy',
      author='Erik C. Olson',
      author_email='erikcaineolson@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ], )
