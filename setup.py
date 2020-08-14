import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_smile",
    version="0.1.1",

    description="A CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Kay Hau",

    package_dir={"": "cdk_smile"},
    packages=setuptools.find_packages(where="cdk_smile"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-lambda",
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
