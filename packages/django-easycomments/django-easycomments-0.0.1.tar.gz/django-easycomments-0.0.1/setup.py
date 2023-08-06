import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-easycomments",
    version="0.0.1",
    author="Ibrahim Konuk",
    author_email="konuk-ibrahim@hotmail.com",
    description="A simple django comment application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibrahimkonuk/django-easycomments",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
