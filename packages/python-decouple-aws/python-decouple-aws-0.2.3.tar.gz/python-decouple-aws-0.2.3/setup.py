# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['decouple_aws']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.7,<2.0', 'python-decouple>=3.1,<4.0']

setup_kwargs = {
    'name': 'python-decouple-aws',
    'version': '0.2.3',
    'description': 'AWS Extensions for Python Decouple',
    'long_description': "Python Decouple AWS\n===================\n\nAWS Extensions for Python Decouple\n\nInstallation\n------------\n::\n\n    pip install python-decouple-aws\n\n\nUsage\n-----\n::\n\n    # Import\n    from decouple import Config\n    from decouple_aws import get_config, RepositoryAwsSecretManager\n\n    # The package provides a wrapper function that will\n    # fallback to environment variables and fail gracefully\n    # if AWS Secrets Manager is not accessible for whatever\n    # reason.\n    config = get_config('your/secret/name', 'ap-southeast-2')\n\n    # Alternatively, if you would like it to fail if secrets\n    # manager is inaccessible, you can build it manually.\n    # initialise the config with the AWS repository\n    # Pass the repo your secret name and the region\n    repo = RepositoryAwsSecretManager('your/secret/name', 'ap-southeast-2')\n    config = Config(repo)\n\n    # Use decouple config like normal\n    MY_SUPER_SECRET_SETTING = config('MY_SUPER_SECRET_SETTING')\n",
    'author': 'Matt Magin',
    'author_email': 'matt.magin@cmv.com.au',
    'url': 'https://github.com/AzMoo/python-decouple-aws',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
