

import urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Quito"
dest="Guayaquil"
key="357ZMH4n7FKnkNJ08roxGkPUbGSuVrd5"  #acceder ea todo el contenido que tien
                                        #mapquest
url=main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

print("URL: " + (url))
json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status == 0:
    print("API status: " + str(json_status)+"=A successful router call. \n")