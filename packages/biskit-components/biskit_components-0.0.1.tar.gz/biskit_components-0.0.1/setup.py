# import io
import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def _get_version():
    """Get version by parsing _version programmatically"""
    version_ns = {}
    with open(
        os.path.join(HERE, "biskit_components", "_version.py")
    ) as f:
        exec(f.read(), {}, version_ns)
    version = version_ns["__version__"]
    return version


setup(
    name="biskit_components",
    version=_get_version(),
    description="",
    long_description="",
    author="devsisters",
    author_email="web@devsisters.com",
    packages=find_packages(),
    install_requires=["dash>=2.7.0"],
    include_package_data=True,
    classifiers=[
        "Framework :: Dash",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    extras_require={"pandas": ["numpy", "pandas"]},
    python_requires=">=3.10, <4",
)
