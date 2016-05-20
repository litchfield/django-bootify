from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-bootify',
    version=VERSION,
    description="Bootstrap 3 support for Django 1.6+",
    long_description="Automagically bash Django 1.6+ with some sense of Bootstrap 3 friendliness, plus some tools.",
    author="Simon Litchfield",
    author_email="simon@s29.com.au",
    url="http://github.com/litchfield/django-bootify",
    license="MIT License",
    platforms=["any"],
    packages=['bootify'],
    #data_files=[(template_dir, templates)],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
