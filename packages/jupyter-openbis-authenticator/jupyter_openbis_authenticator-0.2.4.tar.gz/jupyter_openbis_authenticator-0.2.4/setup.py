import os

from setuptools import setup

setup(name='jupyter_openbis_authenticator',
      version='0.2.4',
      description='An authenticator for Jupyterhub which authenticates against openBIS.',
      url='https://sissource.ethz.ch/sispub/jupyter-openbis-integration/',
      author='SIS | ID | ETH Zuerich',
      author_email='swen@ethz.ch',
      license='BSD',
      packages=['jupyter_openbis_authenticator'],
      install_requires=[
          'pytest',
          'jupyterhub>=0.8.0',
          'pybis>=1.5.0'
      ],
      zip_safe=True)
