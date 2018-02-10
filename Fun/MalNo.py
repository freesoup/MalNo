import requests

user = input("What is the username? ")
wanted = input("What genre are you looking for? ")
r = requests.get('https://kuristina.herokuapp.com/anime/' + user + '.json')

jsonFile = r.json()

idList = list()

#Populate idList with anime ID number
for anime in jsonFile["myanimelist"]["anime"]:
    #Only consider animes that are completed.
    if (anime["my_status"] == "2"):
        idList.append(anime["series_animedb_id"]);

count = 0;

#Iterate through all the anime IDs and print them only if their generes is the same as wanted.
for animeID in idList:
    rid = requests.get('https://api.jikan.me/anime/' + animeID)
    animeInfo = rid.json()
    for genres in animeInfo['genre']:
        if (genres['name'].lower() == wanted.lower()):
            print(animeInfo['title'])
            count += 1
            break;

print(count)
    
    
