# %%
import setuptools

# %%
with open("README.md", "r") as fh:
    long_description = fh.read()

# %%
setuptools.setup(
    name="pyspace-resources",
    version="1.0.0",
    author="Sahin Batmaz",
    author_email="sahin.batmaz@gmail.com",
    description="pyspace_resources contains resource files for pyspace package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True
)
