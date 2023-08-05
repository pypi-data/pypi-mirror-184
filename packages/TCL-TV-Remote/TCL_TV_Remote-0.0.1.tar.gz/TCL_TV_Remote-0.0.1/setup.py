import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="TCL_TV_Remote",
    version="0.0.1",
    author="Patrik Johansson",
    author_email="tcltvremote@popeen.com",
    description="Remote control for TCL Smart TVs",
    long_description="Remote control for TCL Smart TVs",
    long_description_content_type="text/markdown",
    url="https://github.com/popeen/TCL-TV-Remote",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)