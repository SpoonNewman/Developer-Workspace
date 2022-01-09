#### Topics of Discussion
1. Variables
2. Conditionals
3. Loops

#### Variables
Types of variables:
- Boolean (True/False)
- Strings (string/str)
- Integers (int)
- Floating Points (float)
- Objects
- Lists (looks like [] )
- Arrays (looks like [] )

Any time you want to "know" or "keep track of" something in your program then it's going to be in a variable. So make a variable for it.
Variables will help you keep track of everything. reuse them all the time if you can. Can't stress that enough.

### Conditionals
Example of a conditional and what it does.
Lets say that your Lieutenant in the submarine dock wants you keep track of which crates are `isAuthorized` and which ones aren't. If it's authorized then we want to run the function `storeInStorageContainer()` and if it's not authorized then we want to run the function `inspectForExplosivesAndTraps()`. Use the function `isCrateAuthorized()` and pass in the ID to know whether it's authorized. This `isCrateAuthorized()` function should take in one parameter (think of this as a variable) and return a boolean.

We immediately want to "know" or "keep track of" the current crate that we're dealing with. Assume that we could be dealing with `n` number of crates. Whether n == 0, or n == 1, or n == 105

Sequence of events:
...
- put the crate in a variable. (NOTE: this is a little out of scope but good to know for future things - we typically track all complex things by an ID that we make ourselves)
- Track the crate
- Is the crate authorized

Reminder: When dealing with functions think in terms of `F(x)` where x is some argument you're passing to the function. Or in this case a function called `doStuff()` and if we pass an argument to it then it would look like `doStuff(onThisObject)`

```py
currentCrateId = 'CR-42069'
isAuthorized = 1.5

my_thing: int = 1 + isAuthorized

# The is a conditional
if ( currentCrateId == 'CR-42068' ):
    # assume it's NOT authorized
    inspectForExplosivesAndTraps(currentCrateId)
else:
    # We do OTHER stuff
    storeInStorageContainer(currentCrateId)
```

Your Lieutenant tells you that you need to pass crate `CR-420666` to the distribution center of the submarine docking bay if you come across it. To do this call the function `sendToDistribution()` and pass in the crate ID as a parameter.

ADVANCED Step: All crates that are not the correctID we're looking for should be sent to `storeInStorageContainer()`.

MORE ADVANCED: Lieutenant Daniel wants you to still perform all the checks you have in place currently, i.e. checking for the the correct ID of `CR-420666` and sending everything else to storage. Intel has come in that the Admiral has a case of fine wine arriving in crate number `CR-698121` and if that crate comes in we want to send it to him via `sendToAdmiral()`.

```py
# The first crate we look at is `CR-420666`. Because this is the correct crate this should be sent to distribution via `sendToDistribution()`
# The second crate we look at is `CR-432765`
currentCrateId = 'CR-432765'
admiralsWine = 'CR-698121'
correctIdOfDistribution = 'CR-420666'

if ( currentCrateId == correctIdOfDistribution ):
    sendToDistribution(currentCrateId)
elif ( currentCrateId == admiralsWine ):
    sendToAdmiral(currentCrateId)
else: 
    storeInStorageContainer(currentCrateId)   
```

The syntax for conditionals:
- `if ()`
- `else if ()`
- `else`


Looking at a bunch of fucking boxes and crates
```py
admiralsWine = 'CR-698121'
correctIdOfDistribution = 'CR-420666'

crateNumbers = ['CR-7435', 'CR-7121', 'CR-6824', 'CR-7647', 'CR-7524', 'CR-7192', 'CR-5144', 'CR-9274', 'CR-7495', 'CR-698121', 'CR-5572', 'CR-7880', 'CR-6366', 'CR-6289', 'CR-6025', 'CR-9520', 'CR-6081', 'CR-8645', 'CR-6531', 'CR-6417', 'CR-9420', 'CR-7887', 'CR-420666', 'CR-6993', 'CR-5979', 'CR-5911', 'CR-8699', 'CR-5628', 'CR-6520', 'CR-7650', 'CR-8163', 'CR-7524', 'CR-5012', 'CR-8365', 'CR-7551', 'CR-8101', 'CR-7635', 'CR-8883', 'CR-9403', 'CR-8224']

for currentCrateId in crateNumbers:
    if ( currentCrateId == correctIdOfDistribution ):
        sendToDistribution(currentCrateId)
    else if ( currentCrateId == admiralsWine ):
        sendToAdmiral(currentCrateId)
    else: 
        storeInStorageContainer(currentCrateId)
```

Objects
```py
crateApiAddress = 'https://api.mockaroo.com/api/f8b5e180?count=40&key=cf7bbbd0'
dataFromCrateApi = requests.get(crateApiAddress)
crateNumbers = dataFromCrateApi.text.split('\n')

class Crate:
    def __init__(this, height, width, texture, id, isAuthorized, requiresInspection):
        this.crateHeight = height
        this.crateWidth = width
        this.crateTexture = texture
        this.crateid = id
        this.isAuthorized = isAuthorized
        this.requiresInspection = requiresInspection

    crateHeight = ''
    crateWidth = ''
    crateTexture = ''
    crateid = '',
    isAuthorized = false,
    requiresInspection = false

# firstCrate = Crate('2.6', '3.5', 'thicc')
# secondCrate = Crate('3.4', '3.2', 'dry')

admiralsWine = 'CR-698121'
correctIdOfDistribution = 'CR-420666'

storeHouseOfCrates: [Crate] = []
# [0, 1, 2, 3, ..., 100]
for someNumber in range(30698):
    rHeight = getSomeRandomHeight()
    rWidth = getSomeRandomWidth()
    rTexture = getSomeRandomTexture()
    rId = getRandomeId()
    rIsAuthorized = getRandomIsAuthorized()
    rRequiresInspection = getRandomInspectionAuthorization()
    storeHouseOfCrates.append(Crate(rHeight, rWidth, rTexture, rId, rIsAuthorized, rRequiresInspection))
    # [crate1]
    # [crate1, crate2, ..., crate100]

for crate in storeHouseOfCrates:
    if (crate.isAuthorized):
        sendToDistribution(crate)
    elif (crate.requiresInspection):
        sendToBombTeam(crate)
    elif (crate.id == admiralsWine)
        sendToAdmiral(crate)
    elif (crate.id == correctIdOfDistribution)
        sendToOtherDistribution(crate)
    else:
        storeInDeepStorage(crate)
# and so on
```