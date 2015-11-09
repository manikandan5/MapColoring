__author__ = 'Manikandan'

import random

def ReadStatesFromFile():

    stateList = []      #List of 50 States
    adjStates = {}      #List of adjacent states to the states which are stored in Key Values
    allotFrequency = {}

    FileData = open("adjacent-states","r")      #Open States Data from File

    stateData = FileData.readlines()            #Reads each line of State Data

    for state in stateData:                     #Loop to set each State and respective Adjacent States
        tempStates = state.split()
        stateList.append(tempStates[0])
        adjStates[tempStates[0]] = tempStates[1:len(tempStates)]
        allotFrequency[tempStates[0]] = ['A','B','C','D']

    return stateList, adjStates, allotFrequency

def ApplyLegacyConstraint(stateList, adjStates, allotFrequency):

    LegacyFileData = open("Legacy-Constraints","r")

    LegacyData = LegacyFileData.readlines()

    for state in LegacyData:
        tempState = state.split()
        allotFrequency[tempState[0]] = [tempState[1]]
        printCheckConstraint(stateList, allotFrequency, adjStates)
        try:
            allotFrequency = RemoveFrequency(stateList, adjStates, tempState[0], allotFrequency)
        except:
            continue
        print tempState[0]
        stateList.remove(tempState[0])
    return allotFrequency, stateList

def RemoveFrequency(stateList, adjStates, assignedState, allotFrequency):

    neighbours = adjStates[assignedState]

    FrequencyToRemove = allotFrequency[assignedState][0]


    for neighbour in neighbours:
        try:
            allotFrequency[neighbour].remove(FrequencyToRemove)
            if len(allotFrequency[neighbour]) == 1:
                stateList.remove(neighbour)
        except:
            continue

    return allotFrequency

def CheckConstraints(stateList, allotFrequency, adjStates):

    for state in stateList:
        try:
            check = allotFrequency[state]
            neighbours = adjStates[state]
            if len(check)== 1 and len(neighbours)>0:
                for neighbour in neighbours:
                    if (allotFrequency[neighbour] == check):
                        print neighbour, allotFrequency[neighbour], check
                        return False
        except:
            continue
    return True

def printCheckConstraint(stateList, allotFrequency, adjStates):
    if(CheckConstraints(stateList, allotFrequency, adjStates)):
        return True
    else:
        return False

def ChooseStateToAssign(stateList, adjStates):
    count = len(adjStates[stateList[0]])
    chosenState = stateList[0]
    for state in stateList:
        if len(adjStates[state]) > count :
            chosenState = state

    return chosenState

def ApplyValueToChosenState(stateList, adjStates, allotFrequency, chosenState):

    Frequencies = allotFrequency[chosenState]

    allotFrequency[chosenState] = Frequencies[0]

    printCheckConstraint(stateList, allotFrequency, adjStates)

    allotFrequency = RemoveFrequency(stateList, adjStates, chosenState, allotFrequency)

    stateList.remove(chosenState)

    return allotFrequency, stateList

def backtracking(currState, stateDomain):
    return False


stateList = []
adjStates = {}
allotFrequency = {}

stateList, adjStates, allotFrequency = ReadStatesFromFile()

allotFrequency, stateList = ApplyLegacyConstraint(stateList, adjStates, allotFrequency)

chosenState = ChooseStateToAssign(stateList, adjStates)
check = 0

tempAllotFrequency = allotFrequency




#print len(stateList)

#print allotFrequency