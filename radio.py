__author__ = 'Manikandan'

"""
The Program uses a recursive call to assign frequency to states and whenever there is
a failure in the constraint check, it backtracks to change the assigned value
All the functions are explained when used.
Reference: Referred AIMA Berkeley Implementation of CSP to understand CSP
"""

import collections
import copy
from operator import itemgetter
import sys

#Main Program
def MainProgram():

    ReadStatesFromFile()                                # Reads given Input Data

    ApplyLegacyConstraint("Legacy-Constraints")         # Assign Value to Legacy States

    findMCV()                                           # Find the most Constrained Value

    recCall(ChooseStateToAssign(), allotFreq, count)    # Recursive Call to assign value to States

    print ("Number of backtracks is :"), count          # Statement to print the number of backtracks made

    WriteOutput()                                       # Write output data to File

#File to Read Input data
def ReadStatesFromFile():

    FileData = open("adjacent-states","r")              #Open States Data from File

    stateData = FileData.readlines()                    #Reads each line of State Data

    for state in stateData:                             #Loop to set each State and respective Adjacent States
        tempStates = state.split()
        adjStates[tempStates[0]] = tempStates[1:len(tempStates)]
        allotFreq[tempStates[0]] = ['A','B','C','D']

#Function to assign value to Legacy States
def ApplyLegacyConstraint(LegacyFile):

    try:
        LegacyFileData = open(sys.argv[1],"r")     #Open States Data from File

        LegacyData = LegacyFileData.readlines()             #Reads each line of Legacy State Data

        for state in LegacyData:
            tempState = state.split()
            allottedFreq[tempState[0]] = tempState[1]
            legacyList.append(tempState[0])

    except:
        print "Problem with Legacy Data Format"

#Function to find Most Constrained Value
def findMCV():

    tempMCV = {}                                        #Temporary Dictionary to sort based on number of adjacent states

    for state in adjStates:
        tempMCV[state] = len(adjStates[state])

    sorted_states = sorted(tempMCV.items(), key=itemgetter(1))

    for state in sorted_states:
        if state[0] not in legacyList:
            mcvList.append(state[0])

#Function to check Constraints each time a value is assigned
def constraintCheck(state, freq, allotFreq):
    if ((len(allotFreq[state]) == 0) or (len(allotFreq[state])==1 and freq in allotFreq[state])):
        return False
    return True

#Function to Update Frequency and perform constraint checks each time a value is assigned
def updateFreq(state, allotFreq, freqList):
    for tempState in adjStates[state]:
        if not constraintCheck(tempState, freqList, allotFreq):
            return False
    for tempState in adjStates[state]:
        if not updateAdjStates(allotFreq,freqList, tempState):
            if freqList in allotFreq[tempState]:
                allotFreq[tempState].append(freqList)
            return False
    return True

#Function to remove frequency Values from adjacent states
def updateAdjStates(allotFreq,freq, state):
    if freq in allotFreq[state]:
        allotFreq[state].remove(freq)
        if len(allotFreq[state])==0:
             return False
    return True

#Function to select the Most Constrained State to allot value to
def ChooseStateToAssign():
    if len(mcvList) != 0:
        return mcvList.pop()
    else:
        return -1

#Add the state to the list of assigned state
def RemoveStateToAssign(state):
    mcvList.append(state)


#Sanity checks each time a state is allotted
def validityCheck(state, freqList, allotFreq, allotted):
    if freqList in allotFreq[state] and adjCheck(state, allotted):
        return True
    return False

#Adjacent States Violation Check
def adjCheck(state,allotted):
    for tempState in adjStates[state]:
        if tempState in allottedFreq:
            if allotted==allottedFreq[tempState]:
                return False
    return True

#Recursive call to assign values to states and backtrack
def recCall(state, allotFreq, count):
    for freqList in ListofFrquencies:
        if validityCheck(state, freqList, allotFreq, freqList):
            allotFreqCopy=copy.deepcopy(allotFreq)
            if updateFreq(state, allotFreqCopy, freqList):
                allottedFreq.update({state:freqList})
                state = ChooseStateToAssign()
                if state == -1:
                    return True
                else:
                    if recCall(state, allotFreqCopy, count):
                        return True
                    else:
                        RemoveStateToAssign(state)
                        count+=1
    return False

#Funtion to write Output
def WriteOutput():
    fileWrite = open("Results.txt",'w')
    for state, freq in sorted(allottedFreq.items()):
        fileWrite.write(state + ":" + freq + '\n')
    fileWrite.close()


adjStates = {}              # Dictionary to hold list of States and adjacent states as keys
allottedFreq = {}           # Dictionary which holds the values of frequencies to states that are allotted
allotFreq = {}              # Dictionary to hold list of possible values to states that are not yet allotted
mcvList = []                # Most Constrained Values list
count=0                     # Backtrack count
legacyList=[]               # List of Legacy States
ListofFrquencies = ['A','B','C','D']

MainProgram()



