admiralsWine = 'CR-698121'
correctIdOfDistribution = 'CR-420666'

crateNumbers = ['CR-7435', 'CR-7121', 'CR-6824', 'CR-7647', 'CR-7524', 'CR-7192', 'CR-5144', 'CR-9274', 'CR-7495', 'CR-698121', 'CR-5572', 'CR-7880', 'CR-6366', 'CR-6289', 'CR-6025', 'CR-9520', 'CR-6081', 'CR-8645', 'CR-6531', 'CR-6417', 'CR-9420', 'CR-7887', 'CR-420666', 'CR-6993', 'CR-5979', 'CR-5911', 'CR-8699', 'CR-5628', 'CR-6520', 'CR-7650', 'CR-8163', 'CR-7524', 'CR-5012', 'CR-8365', 'CR-7551', 'CR-8101', 'CR-7635', 'CR-8883', 'CR-9403', 'CR-8224']



def sendToDistribution (crateId):
    print('This is the Distribution crate ', crateId)

def sendToAdmiral (crateId):
    print('Admirals ID: ', crateId)

def storeInStorageContainer (crateId):
    print('Storing in storage container:', crateId)



for currentCrateId in crateNumbers:
    if ( currentCrateId == correctIdOfDistribution ):
        sendToDistribution(currentCrateId)
    elif ( currentCrateId == admiralsWine ):
        sendToAdmiral(currentCrateId)
    else:
        storeInStorageContainer(currentCrateId)