import setuptools

with open(r"arasents\README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arasents",
package_data = {
    'arasents': ['*.txt','*.db']},
    version="0.0.B",
    author="muhamed hachoum",
    author_email="arab@muslim.com",
    description="A small package for sentiments analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)