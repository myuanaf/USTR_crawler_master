# Load packages
from selenium import webdriver
from lxml import etree
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
import csv
import os

# disable visualization
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# avoid detection
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# instantiate browser object
browser = webdriver.Chrome(executable_path='./chromedriver.exe',
                           chrome_options=chrome_options,
                           options=option)

# Write title to csv
def check_output(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
    with open(filePath, 'a+',newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(('Submission ID', 'Organization Name', 'Stage',
                         'HTSUS code', 'Product', 'Date Posted', 'Response Closes'))


def selenium_crawler(filePath):
    # get data
    page_text = browser.page_source
    sleep(5)
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//div[@class="slds-scrollable_y"]/table/tbody/tr')

    for tr in tr_list:
        SubmissionID = tr.xpath('./th' + xpath + 'lightning-formatted-url/a/text()')[0]
        OrganizationName = tr.xpath('./td[1]' + xpath +'lightning-base-formatted-text/text()')[0]
        Stage = tr.xpath('./td[2]' + xpath + 'lightning-base-formatted-text/text()')[0]
        HTSUScode = tr.xpath('./td[3]' + xpath + 'lightning-base-formatted-text/text()')[0]
        Product = tr.xpath('./td[4]' + xpath + 'lightning-base-formatted-text/text()')[0]
        DatePosted = tr.xpath('./td[5]' + xpath + 'lightning-formatted-date-time/text()')[0]
        ReponseCloses = tr.xpath('./td[6]' + xpath + 'lightning-formatted-date-time/text()')[0]

        with open(filePath, 'a+',newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow((SubmissionID, OrganizationName, Stage,
                             HTSUScode, Product, DatePosted, ReponseCloses))
    try:
        btn = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div/div[3]/div/div/div/c-ustrfb-public-docket/lightning-card/article/div[2]/slot/c-ustrfb-pagination-parent/div/c-paginator-bottom/div/lightning-layout/slot/lightning-layout-item[4]/slot/lightning-button/button')
        btn.click()
        sleep(5)
    except:
        pass

def main():
    check_output(filePath)
    print('The crawler is started...')
    for i in range(176): # for another url, please change from 606 to 176
        selenium_crawler(filePath)
        print('The scraping of Page {} is completed'.format(i+1))
    sleep(5)
    browser.quit()
    print('The crawler is ended...')


if __name__ == '__main__':
    url = 'https://comments.ustr.gov/s/docket?docketNumber=USTR-2019-0017' # for another url, please change url to 'https://comments.ustr.gov/s/docket?docketNumber=USTR-2019-0017'
    xpath = '/lightning-primitive-cell-factory/span/div/'
    filePath = './output/USTR-2019-0017.csv' # for another output csv, please change name to './output/USTR-2019-0017.csv'
    browser.get(url)
    sleep(5)
    main()










