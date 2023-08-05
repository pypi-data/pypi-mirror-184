from setuptools import setup

setup(
    name='HedgehogEncoder',
    version='1.0',
    packages=[''],
    url='https://github.com/BlackSnowDot/HedgehogEncoder',
    license='MIT',
    author='BlackSnowDot',
    author_email='',
    description='A simple and secure encryption tool using the AES algorithm in CTR mode. Encrypts data using a password-generated key and encodes it as a base64 string with added random characters. Includes encode and decode methods for easy use.',
    install_requires=["cryptography"]
)
