import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="payload_wtf",
    version="0.0.1",
    author="Yanwar Solahudin",
    author_email="yanwarsolah@gmail.com",
    description="simple payload with an easy format for building Python APIs (like Django).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yanwarsolah/payload-wtf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)