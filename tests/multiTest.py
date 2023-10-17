


track1 = ["ON","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF",]
track2 = ["OFF","OFF","OFF","OFF","ON","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF","OFF",]



#sampleMap = {track1:"kick", track2:"snare"}


sampleMap = {}


LIST = [track1, track2]

def mksampleMap(trackName, sample):
    global sampleMap
    sampleMap[str(trackName)] = sample
    return sampleMap

mksampleMap(track1, 'carbon.wav')
mksampleMap(track2, 'snare.wav')

def mk_sampleList(trackList):
    sLists = []
    for t in trackList:
        sList = []
        for elem in t:
            if elem == "ON":
                sList.append(sampleMap[str(t)])
            elif elem == "OFF":
                sList.append("OFF")
                
        sLists.append(sList)
    return(sLists)

##def get_sampleList(*arg):
##    for i in range(len(arg)):
##        #print(arg[i])
##


def zip_lists(L):
    
    zip()


print(mk_sampleList(LIST))


##L =[]
##
##def get_args(*arg):
##    for i in range(len(arg)):
##        print(arg[i])
##        L.append(arg[i])
##
##
####z = list(get_args(track1, track2))
##
##get_args(track1, track2)
##
