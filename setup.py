from distutils.core import setup
setup(
  name = 'standardmodel',
  packages = ['standardmodel'],
  version = '0.0.1',
  license='MIT',
  author = 'Terminal Labs',
  author_email="solutions@terminallabs.com",
  url = 'https://github.com/terminal-labs/standardmodel',
  download_url = 'https://github.com/terminal-labs/standardmodel/archive/master.zip',
  install_requires=[
    "setuptools<=45",
    "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
    "utilities-package_cli-metapackage@git+https://gitlab.com/terminallabs/utilitiespackage/metapackages/utilities-package_cli-metapackage.git@master#egg=utilitiespackageclimetapackage&subdirectory=utilitiespackageclimetapackage",
    "rambo-vagrant@git+https://github.com/terminal-labs/rambo.git",
    "tornado<5.0,>=4.2.1",
    "pyzmq<17.1.0",
    "salt==2018.3.3",
    "ansible==2.9.0",
  ],
  classifiers=[  # Optional
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
  entry_points="""
      [console_scripts]
      standardmodel=standardmodel.cli:main
   """,
)
