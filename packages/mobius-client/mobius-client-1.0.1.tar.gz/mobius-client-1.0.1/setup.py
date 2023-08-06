from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mobius-client',
    version='1.0.1',
    url="https://github.com/mobius-network/mobius-client-python",
    author="Mobius Team",
    author_email="developers@mobius.network",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'PyJWT',
        'stellar-base',
    ],
)
