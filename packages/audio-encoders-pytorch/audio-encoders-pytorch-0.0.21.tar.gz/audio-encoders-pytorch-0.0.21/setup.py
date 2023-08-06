from setuptools import find_packages, setup

setup(
    name="audio-encoders-pytorch",
    packages=find_packages(exclude=[]),
    version="0.0.21",
    license="MIT",
    description="Audio Encoders - PyTorch",
    long_description_content_type="text/markdown",
    author="Flavio Schneider",
    author_email="archinetai@protonmail.com",
    url="https://github.com/archinetai/audio-encoders-pytorch",
    keywords=["artificial intelligence", "deep learning", "audio"],
    install_requires=[
        "torch>=1.6",
        "torchaudio",
        "data-science-types>=0.2",
        "einops>=0.6",
        "einops-exts>=0.0.3",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
