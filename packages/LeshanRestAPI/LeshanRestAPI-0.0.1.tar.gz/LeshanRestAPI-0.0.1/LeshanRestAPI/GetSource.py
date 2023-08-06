from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from bs4 import BeautifulSoup
import json
import os


def getSource(url,refresh):
    '''returns the source from a file if available or the html if not
    Keyword arguments:
    url -- the url of the leshan client page
    refresh -- get a fresh copy of the dictionary from the html even if we have the client cached.
    '''
    client = url.split(r'/')[-1]
    if not refresh:
        # check if we have a chached dictionary of this client
        for file_name in os.listdir('cached_clients'):       
            if file_name == client+'.json':
                return json.load(open('cached_clients\\' + file_name))
    # if we dont then we have to do the more time consuming option of scraping the html
    return getSourceFromHTML(url, client)


def getSourceFromHTML(url, client):
    '''returns the dictionary of page_objects from the html of the client page
    Keyword arguments:
    url -- the url of the leshan client page
    client -- the name of the client gotten from the url
    '''
    # launch headless chrome
    driver = setBrowser()
    # get the raw html from the webpage
    encoded_source = fetchHTML(driver, url)
    # parse the url into json
    object_dict = parseHTML(BeautifulSoup(encoded_source, 'html.parser'))
    # raise error if parsing was not successful
    if len(object_dict) == 0:
        raise IOError("URL was not rendered into a dictionary")
    # cache the page_objects of this client so we dont have to connect to its server again to fetch html
    cacheClient(object_dict, client)
    return object_dict


def fetchHTML(driver, url):
    '''helper method of getSourceFromHTML that returns the html from the leshan client page
    Keyword arguments:
    url -- the url of the leshan client page
    driver -- selenium webdriver object 
    '''
    driver.get(url)
    #wait until the dom fully renders. We can check that we can find the object-name
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.object-name')))
    # html page is encoded in utf-8 so we must make that explicit
    encoded_source = driver.page_source.encode('utf-8')
    driver.close()
    return encoded_source


def setBrowser():
    '''helper method of getSourceFromHTML() that configures the browser'''
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    return webdriver.Chrome(chrome_options=options)


def cacheClient(object_dict, client):
    '''cache the page_object dictionary of the client so we don't need to scrape the html on future querries
    Keyword arguments:
    object_dict -- dictionary of page_objects that are sent to output file
    client -- name of the client file to store object_dict
    '''
    # convert the dictionary to json string
    page_objects = json.dumps(object_dict)
    # open and write the json string to file
    f = open('cached_clients\\' + client + '.json', 'w')
    f.write(page_objects)


def parseHTML(page_source):
    '''parses the url of the leshan client webpage into a dictionary containing each object, instance and resource.
    Keyword arguments:
    page_source -- raw html to parse and return page_objects dictionary
    '''
    object_dict = {}
    # the Leshan html is a tree structure with elements given as objects>instances>resources
    objects = page_source.find_all(
        attrs={'ng-repeat': 'object in objects'})
    # for each object we find all elements that contain the instances
    for object_ in objects:
        instances = object_.find_all(
            attrs={'ng-repeat': 'instance in object.instances'})
        instance_dict = {}
        # for each instance element we find we find all resources attached to that resource
        for i in range(len(instances)):
            resources = instances[i].find_all(
                attrs={'ng-repeat': 'resource in instance.resources'})
            resource_dict = {}
            # find the resource_name and id and put that into the dictionary
            for resource in resources:
                resource_name = resource.find(
                    class_='resource-name').text.strip()
                resource_id = resource.find(
                    'button').attrs['tooltip-html-unsafe'].split('>')[1]
                resource_dict[resource_name] = resource_id
            instance_dict[i] = resource_dict
        # we put all the resource objects into a nested dictionary of object>instance>resources
        object_name = object_.find(class_='object-name').text.strip()
        object_dict[object_name] = instance_dict

    return object_dict
