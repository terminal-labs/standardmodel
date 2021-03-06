from distutils.core import setup

pins = []

setup(
  name = 'standardmodel',
  packages = ['standardmodel'],
  version = '0.0.1',
  license='MIT',
  author = 'Terminal Labs',
  author_email="solutions@terminallabs.com",
  url = 'https://github.com/terminal-labs/standardmodel',
  download_url = 'https://github.com/terminal-labs/standardmodel/archive/master.zip',
  install_requires=pins + [
    "utilities-package-pinion@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package-pinion.git",
    "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
    "utilities-package_cli-metapackage@git+https://gitlab.com/terminallabs/utilitiespackage/metapackages/utilities-package_cli-metapackage.git",
    "finestructure@git+https://github.com/terminal-labs/finestructure.git",
    "domainwall@git+https://github.com/terminal-labs/domainwall.git",
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
