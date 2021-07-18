# View bot


=======Buildpacks==========   
   https://github.com/heroku/heroku-buildpack-google-chrome   
   https://github.com/heroku/heroku-buildpack-chromedriver      



==========Keys=============   
CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver      
GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome   

Options = webdriver.ChromeOptions()   
Options.binary_location = os.environ['GOOGLE_CHROME_BIN']   
Options.add_argument('--headless')   
Options.add_argument('--disable-dev-sh-usage')   
Options.add_argument('--no-sandbox')   

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER_PATH'], chrome_options=Options)   
