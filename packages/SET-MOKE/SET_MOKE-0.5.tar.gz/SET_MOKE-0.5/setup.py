import setuptools

setuptools.setup(
    name="SET_MOKE",
    version="0.5",
    author="rehab shahzadi",
    author_email="rehab.shahzadi@kics.edu.pk",
    description="An API for social media data extraction",
    url="https://github.com/rehabshahzadi/SETMOK_API",
    packages=setuptools.find_packages(),

    classifiers = (
                  "Programming Language :: Python :: 3",
                  "Operating System :: OS Independent",

              ),
     install_requires=[
        'google-api-python-client',
        'tweepy==3.6.0',
        'twitter==1.18.0',
         'moment',
         'pymysql'
    ],

)
