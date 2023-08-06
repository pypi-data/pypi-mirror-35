import setuptools
setuptools.setup(
    name="steven_private_package_for_python",
    version="0.1.0",
    url="https://github.com/myclubisclub6/python-package",
    author="Steven Nguyen",
    author_email="myclubisclub6@gmail.com",
    description="Testing to see if I can make a package.",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
