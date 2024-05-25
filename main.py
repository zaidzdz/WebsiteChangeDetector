import time
import requests

inputdUrl = input("Enter the url you want to be checked(must include https://)\n")
inputTime = input("Enter the number of seconds between checks:\n")
url = inputUrl

def getoldHtml():
    oldhtml = requests.get(url).text
    return oldhtml


TOldHtml = getoldHtml()
print(getoldHtml())
while True:

    currenthtml = requests.get(url).text
    print(currenthtml)
    if currenthtml != TOldHtml:
        print("Webpage Changed")
        TOldHtml = getoldHtml()
    else:
        print("Webpage didn't change")
    time.sleep(inputTime)
