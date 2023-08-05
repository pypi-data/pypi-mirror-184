from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Accessing camera on Django Webframework'
LONG_DESCRIPTION = 'A package that allows to stream camera on website through Django Webframework'

# Setting up
setup(
    name="djangocamera",
    version=VERSION,
    author="Naman Goyal (Naman82)",
    author_email="<namangoyal.developer@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'django'],
    keywords=['django','python', 'video', 'stream', 'video stream', 'camera stream','django camera','django video'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)