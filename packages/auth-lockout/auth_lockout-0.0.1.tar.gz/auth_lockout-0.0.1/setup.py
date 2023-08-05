import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auth_lockout",
    version="0.0.1",
    author="Kailey",
    author_email="author@example.com",
    description="Initial commit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbvanzomeren/pypa.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)