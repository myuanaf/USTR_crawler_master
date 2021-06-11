This project is to scrape the Java script generated website using selenium

Please make sure your chrome version matches the the version of chromedriver.exe!
In this project, I use the chrome version 91.0.4472.101 and chromedriver.exe 91.0.4472.19/chromedriver_win32.zip/chromedriver.exe
Here is the link to download the right chromedriver.exe: http://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/

The environment:
Python 3.8 + Pycharm 2021.1.1
Other environment maybe also okay but not tested

Required packages:
selenium==3.141.0
lxml==4.5.2

For program running：
Just click the run button of Pycharm


The default url is  https://comments.ustr.gov/s/docket?docketNumber=USTR-2019-0005,
if you want to change to  https://comments.ustr.gov/s/docket?docketNumber=USTR-2019-0017,
please change the url string and csv name in the part:  if __name__ == '__main__':
In addition, please change the number in main() from 606 to 176


