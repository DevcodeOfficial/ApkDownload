import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="apkdownload",
 
    #version of the module
    version="0.0.6",
 
    #Name of Author
    author="Ayan Ansari",
 
    #your Email address
    author_email="TechnoAyan1234@gmail.com",
 
    #Small Description about module
    description="You can easily download apk files using this api",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://Github.com/DevcodeOfficial/ApkDownload",
    install_requires = ["requests", "bs4"],
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
