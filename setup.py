from setuptools import setup, find_packages

setup(
    name='sae_toolkit',
    version='1.0.0',
    description='Reusable Tools for SAE Development',
    author='John Naeder',
    author_email='j.naeder@sae.edu',
    url='https://github.com/jnaederSAE/sae_toolkit',
    packages=find_packages(),
    install_requires=[
        "cachetools==5.3.0",
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "google-api-core==2.11.0",
        "google-api-python-client==2.86.0",
        "google-auth==2.17.3",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==1.0.0",
        "googleapis-common-protos==1.59.0",
        "httplib2==0.22.0",
        "idna==3.4",
        "numpy==1.24.3",
        "oauthlib==3.2.2",
        "pandas==2.0.1",
        "protobuf==4.22.4",
        "pyasn1==0.5.0",
        "pyasn1-modules==0.3.0",
        "pymssql==2.2.7",
        "pyparsing==3.0.9",
        "python-dateutil==2.8.2",
        "python-dotenv==1.0.0",
        "pytz==2023.3",
        "requests==2.30.0",
        "requests-oauthlib==1.3.1",
        "rsa==4.9",
        "six==1.16.0",
        "tzdata==2023.3",
        "uritemplate==4.1.1",
        "urllib3==2.0.2"
    ]
)
