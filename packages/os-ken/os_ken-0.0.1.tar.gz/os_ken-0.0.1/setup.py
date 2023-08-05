import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="os_ken",
    version="0.0.1",
    author="OpenStack",
    author_email="openstack-dev@lists.openstack.org",
    description="Component-based Software-defined Networking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.openstack.org/os-ken/latest/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ),
)
