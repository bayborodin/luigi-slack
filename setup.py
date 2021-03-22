try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="luigi-slack",
    version="1.1.4",
    description="Send summary messages of your Luigi jobs to Slack.",
    long_description=open("README.md").read(),
    license="MIT",
    packages=['luigi_slack'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="luigi",
    install_requires=["requests", "luigi"],
    entry_points={
        "console_scripts": ["luigi-slack=luigi_slack.luigi_slack:run"]
    }
)
