from setuptools import setup, find_packages

setup(
    name="image_processing",
    version="0.2",
    author="Agatha",
    description="Image Processing Package using Skimage",
    long_description=open("README.md").read(),  # Certifique-se de que README.md existe
    long_description_content_type="text/markdown",
    url="https://github.com/agathacrissantos/DIO-image-processing-package/tree/master",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scikit-image"
    ],
    python_requires=">=3.11",
)