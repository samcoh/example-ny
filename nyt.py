import requests
import secrets #create another module, look into this file and get all the information we need
#someone has to create their own secret files in order to run this code

# gets stories from a particular section of NY times
#construct our query (base url, mame of section that we want, Api key that we have, put it all together to get the json and return it for us)
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/' #baseurl extracted from nytime documentation
    extendedurl = baseurl + section + '.json' #give us the top stories for that section
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories) # should print a big pile of json
#pile of json representing different science headlines
#the data is a big dictionary
#json will either be a dictionary with a list inside of it or a list
#inside each will be information about one of the top stories
