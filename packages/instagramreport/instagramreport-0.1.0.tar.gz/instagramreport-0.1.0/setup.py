from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "instagramreport",
    version = "0.1.0",
    author = "Daniel Corvalán",
    author_email = "corvalanlara@protonmail.com",
    description = "App for creating an Instagram Business account performance report (in spanish)",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/corvalanlara/",
    packages = find_packages(),
    entry_points = {
        'gui_scripts':[
            'instagramreport = instagramreport.reportmaker:main'
        ]
    },
    install_requires = ['python-docx', 'certifi', 'facebook-sdk', 'requests', 'urllib3'],
    include_package_data = True,
    classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ),
)
