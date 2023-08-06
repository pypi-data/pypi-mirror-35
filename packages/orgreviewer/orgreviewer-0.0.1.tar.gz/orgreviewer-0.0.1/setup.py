from setuptools import setup, find_packages

setup(
    name="orgreviewer",
    version="0.0.1",
    description="A tool to manage users on itsyou.online",
    packages=find_packages(),
    scripts=['orgreviewer'],
    install_requires=[
        "click==6.*",
        "pyyaml==3.*",
        "requests==2.*",
        # for iyo client
        "six==1.*",
        "python-dateutil==2.*",
    ]
)
