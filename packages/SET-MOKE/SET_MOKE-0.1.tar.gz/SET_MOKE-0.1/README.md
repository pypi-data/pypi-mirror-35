## SETMOKE API v-1.0 ##
## Getting Started ##
This project aims to get the basic fields of the data we parsed.If you want to parse the whole data you can change the following files(TwitterDataRetrievel.py,GooglePlusDataRetreivel.py) as per requirement. project  returns the output in **JSON format**
### Prerequisites ###
* Install python(3.5.0) , pip using the following commands
  - $ sudo apt-get update
  - $ sudo apt-get install python3.5
  - $  sudo apt install python-pip
* Your favourite IDE, e.g., [Pycharm (for Python)](https://itsfoss.com/install-pycharm-ubuntu/)
#### Importing project ####
1. Clone the repository using GIT into a local directory. The project directory **SETMOK_API** will be created.
1. Import the project into your favourite IDE. For Pycharm, follow the steps below
	- Launch Pycharm
	- Click File -> Open
	- Select the root directory (where Setmok_API project is cloned).
	- Click OK.
#### Resolving dependencies of the project ####
To install the packages required for this project ,make sure you are in **root directory**.Run the following command from here
 - $ pip install -r ../requirements.txt
Download all the packages written in this file
#### Getting API credentials #### 
Open the conf/config.ini to update with your own api_credentials
* Step 1: [Getting Twitter API keys](http://adilmoujahid.com/posts/2014/07/twitter-analytics/)
   - In order to access Twitter API, we need to get 4 pieces of information from Twitter: API key, API secret, Access token and Access token secret. Follow the steps below to get all 4 elements:
        - Create a twitter account if you do not already have one.
        - Go to https://apps.twitter.com/ and log in with your twitter credentials.
        - Click "Create New App"
        - Fill out the form, agree to the terms, and click "Create your Twitter application"
        - In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
        - Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
* Step 2: [Getting Google plus API key](https://developers.google.com/maps/documentation/embed/get-api-key)
   - Follow these steps to get an API key:
        - Go to the Google Cloud Platform Console.
        - Create or select a project.
        - Click Continue to enable the API.
        - On the Credentials page, get an API key. 
 
