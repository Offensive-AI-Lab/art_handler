import setuptools
setuptools.setup(
    name="art_handler",
    version="0.0.8",
    author="MABADATA",
    author_email="mabadatabgu@gmail.com",
    description="Handle art paths",
    url="https://github.com/MABADATA/art_handler",
    package_data={"art_handler":["attack_defense_map.json"]},
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    dependency_links=[
        'https://pypi.python.org/simple'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)