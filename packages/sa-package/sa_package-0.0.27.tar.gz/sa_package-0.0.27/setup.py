from setuptools import setup, find_packages

setup(
    name="sa_package",
    version="0.0.27",
    
    url="https://github.com/tmddk2709/sa_package",
    author="Seunga Shin",
    author_email="seungashin9275@gmail.com",

    packages=find_packages(),

    install_requires=[
        "bs4",
        "pandas",
        "gspread",
        "oauth2client",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "selenium",
        "webdriver-manager",
        "packaging",
        "pymysql"
    ]
)