import setuptools

with open ( "README.md" , "r",encoding="utf-8" ) as fh :
    long_description = fh . read ()

setuptools . setup (
    name = "merged_excel_tools" ,
    version = "1.0" ,
    author = "zhangtao103239" ,
    author_email = "zhangtao103239@163.com" ,
    description = "merged cells excel tools" ,
    long_description = long_description ,
    long_description_content_type = "text/markdown" ,
    url = "https://github.com/zhangtao103239/read_merged_tools" ,
    packages = setuptools . find_packages (),
    classifiers = (
        "Programming Language :: Python :: 3" ,
        "License :: OSI Approved :: MIT License" ,
        "Operating System :: OS Independent" ,
    ),
    install_requires=['openpyxl']
)
