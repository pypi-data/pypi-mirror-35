from distutils.core import setup
setup(
  name = 'lod-executor',
  packages = ['lod',],
  version = '1.0.4',
  description = 'A program for executing other programs on behalf of elody.com',
  long_description = 'A program for executing other programs on behalf of elody.com',
  author = 'Florian Dietz',
  author_email = 'floriandietz44@gmail.com',
  url='https://elody.com',
  license = 'MIT',
  package_data={
      '': ['*.txt', # this covers both the LICENSE.txt file in this folder, and the TRUTH.txt file in the /lod/ folder
            '*.cnf',
        ],
   },
   entry_points = {
        'console_scripts': [
            'lod-executor=lod.executor:main',
        ],
    },
    install_requires=[
        'bottle',
        'cheroot',
        'docker',
        'python-dateutil',
        'pyOpenSSL',
        'requests_toolbelt',
    ],
)
