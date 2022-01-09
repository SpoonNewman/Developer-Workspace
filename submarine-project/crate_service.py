import requests


def getcratenumbers():
    apiaddress = 'https://my.api.mockaroo.com/spoon-newman-crate-ids.json'
    headers = {'X-API-Key': 'cf7bbbd0'}
    data = requests.get(apiaddress, headers=headers)
    return data.json()

def processcrates():
    print('Currently processing crates')
    cratenumbers = getcratenumbers()
    for crate in cratenumbers:
        if (crate['id'] == 'CR-7787'):
            senditemtoadmiral(crate)
        elif (crate['id'] == 'CR-9215'):
            sendtodistribution(crate) 
        else: 
            storeinstoragecontainer(crate)

def storeinstoragecontainer(item) -> bool:
    print('Storing Crate into Storage Container...') 
    # if this fails we want to quarantine the item

def quarantineitem(item) -> bool:
    return True
    # we assume this operation succeeds

def senditemtoadmiral(item) -> bool:
    print('Sending crate to admiral...')
    # same thing as last time

def sendtodistribution(item) -> bool:
    print('Sending container to distribution...')
    # if this fails item needs to be quarantined
