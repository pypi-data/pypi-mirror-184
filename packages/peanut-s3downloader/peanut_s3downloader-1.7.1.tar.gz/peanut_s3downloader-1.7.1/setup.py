from setuptools import setup, find_packages


setup(
    name='peanut_s3downloader',
    version='1.7.1',
    license='MIT',
    author="M K",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mkarys/dummy-package',
    keywords='dummy project',
    install_requires=[
          'requests',
      ],

)
