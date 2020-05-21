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
        "setuptools",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
        "utilities-package_cli-metapackage@git+https://gitlab.com/terminallabs/utilitiespackage/metapackages/utilities-package_cli-metapackage.git@master#egg=utilitiespackageclimetapackage&subdirectory=utilitiespackageclimetapackage",
        "salt",
        "ansible",
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
