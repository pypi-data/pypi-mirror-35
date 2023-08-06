import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='shongololo',
    version='1.1.3',
    author="J Wyngaard",
    author_email="r4space@gmail.com",
    description="Python application for simply sensor data capture on a Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/r4space/VTAgMonitoring/tree/master/code/shongololos",
    packages=setuptools.find_packages(),
    package_data={'': ['*.txt', '*.jsn']},
    install_requires=['serial', 'pyserial', 'simple-settings'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
    ],
)
