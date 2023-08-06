from setuptools import setup, find_packages

setup(
    name='mobius-client',
    version='1.0.0',
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
