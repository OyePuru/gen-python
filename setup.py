from setuptools import setup, find_packages

setup(
    name="gen-python",
    version="0.1.0",
    description="Generated Python stubs for proto files",
    packages=find_packages(),
    package_data={'gen.proto': ['gen/proto/example/*', 'gen/proto/person/*']},
    install_requires=[
        "grpcio-tools>=1.41.0",
        "mypy-protobuf>=0.8.0"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
