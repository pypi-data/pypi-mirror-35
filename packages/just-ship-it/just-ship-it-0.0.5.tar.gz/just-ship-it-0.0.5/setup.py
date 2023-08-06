import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="just-ship-it",
    version="0.0.5",
    author="Grant Stafford",
    description="For when you just need to ship your Python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gstaff/just-ship-it",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='demo',
    install_requires=['flask-ngrok', 'flask-restplus'],
    py_modules=['just_ship_it']
)
