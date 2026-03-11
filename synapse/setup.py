from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="synapse-tld",
    version="1.0.0",
    author="zstickytreefrog",
    author_email="asdfbbcbbq@gmail.com",
    description="TLD/1.0 — The open standard for the full-spectrum web. Pre-compressed semantic context for AI document processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkuwandf/synapse",
    project_urls={
        "Homepage": "https://mkuwandf.github.io/synapse",
        "Whitepaper": "https://github.com/mkuwandf/synapse/blob/main/whitepaper.md",
        "Bug Reports": "https://github.com/mkuwandf/synapse/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Markup",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.7",
    keywords=[
        "TLD", "semantic compression", "AI efficiency", 
        "document processing", "machine readable", 
        "full-spectrum web", "open standard", "synapse"
    ],
)
