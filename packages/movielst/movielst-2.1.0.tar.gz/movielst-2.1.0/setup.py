from setuptools import setup

setup(name='movielst',
      version='2.1.0',
      description='Everything about your movies within the command line.',
      url='https://github.com/Mozzo1000/movielst',
      author='Andreas Backström',
      author_email='andreas@simplymozzo.se',
      license='MIT',
      packages=['movielst'],
      entry_points={
               'console_scripts': ['movielst=movielst:main'],
           },
      install_requires=[
          'guessit',
          'terminaltables',
          'tqdm',
          'colorama',
          'xlsxwriter'
      ],
      keywords=['movies', 'CLI', 'movies-within-CLI', 'python'],
      classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Version Control',
      ],)
