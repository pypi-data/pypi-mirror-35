import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_pseudo_j",
    version="0.6.6",
    author="David Fagneray",
    author_email="david.fagneray@gmail.com",
    description="A Java8 compiler to Pseudo",
    long_description=long_description,
    url="https://github.com/dfagneray/pseudo_java",
    keywords=['compiler', 'generation', 'c++', 'ruby', 'c#', 'javascript', 'go', 'python', 'pseudo'],
    packages=['pseudo_java'],
    install_requires=[
        'PyYAML',
        'colorama',
        'termcolor',
        'pseudo>=0.2.3'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'test_pseudo_j=pseudo_java.main:main',
        ],
    },
)
