import time
import requests

inputtedUrl = input("Enter the url you want to be checked(must include https://)\n")
url = inputtedUrl

def getoldHtml():
    oldhtml = requests.get(url).text
    return oldhtml


TOldHtml = getoldHtml()
print(getoldHtml())
while True:

    currenthtml = requests.get(url).text
    print(currenthtml)
    if currenthtml != TOldHtml:
        print("Html Changed")
        TOldHtml = getoldHtml()
    else:
        print("Html Same")
    time.sleep(4)
