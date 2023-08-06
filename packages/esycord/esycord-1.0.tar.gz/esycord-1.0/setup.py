from setuptools import setup, find_packages


setup(
    name='esycord',
    version='1.0',
    license='MIT',
    author="EgogorGames",
    author_email='egogorgames@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/EgogorGames/EasyCord',
    keywords='esycord',
    install_requires=[
          'scikit-learn',
      ],

)
