# Creates all parts algorithmically and plays them together 

from music import *
from IN_C_PHRASES import *
import random

# Creates a score, defining it's title and setting tempo at 120 BPM
fullScore = Score("In C", 120)

# Creates a part, defining it's title, MIDI instrument, and MIDI channel
part0 = Part("Metronome", PIANO, 0)
# Sets panning for each part (0-1, left to right)
part0.setPan(.5)
part1 = Part("first part", PIANO, 0)
part1.setPan(.3)
part2 = Part("second part", CLARINET, 1)
part2.setPan(.4)
part3 = Part("third part", FLUTE, 2)
part3.setPan(.4)
part4 = Part("fourth part", VIOLIN, 3)
part4.setPan(.2)
part5 = Part("fifth part", VIOLA, 4)
part5.setPan(.5)
part6 = Part("sixth part", CELLO, 5)
part6.setPan(.9)
part7 = Part("seventh part", CONTRABASS, 6)
part7.setPan(.8)
part8 = Part("eighth part", TRUMPET, 7)
part8.setPan(.4)
part9 = Part("ninth part", OBOE, 8)
part9.setPan(.7)
part10 = Part("tenth part", SNARE, 9)
part10.setPan(.7)
part11 = Part("tenth part", SAX, 10)
part11.setPan(.6)
part12 = Part("eleventh part", VIBES, 11) 
part12.setPan(.4)
part13 = Part("twelth part", TROMBONE, 12)
part13.setPan(.5)
part14 = Part("thirteenth part", BASSOON, 13)
part14.setPan(.5)
part15 = Part("fourteenth part", HORN, 14)
part15.setPan(.6)
part16 = Part("fifteenth part", HARP, 15)
part16.setPan(.3)


# Creates a list of all parts 
partList = [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, part11, part12, part13, part14, part15, part16]

# List of parts that should be transposed up an octave
highParts = [part3, part4]

# List of parts that should be transposed down an octave 
lowParts = [part6, part8, part11, part15]

# List of parts that should be transposed down two octaves 
lowestParts = [part7, part13, part14]

# Creates an empty list 
phraseList = [] 


def partBuild(phr, a, b):
   """Construct each part running a series of random algorithms"""
   
   # Set x equal to a random float between 0 and 1
   x = random.random()
   
   # Empty phraseList
   phraseList = []
   
   # .15 chance of transposing up an octave
   if x < .15: 
      
      # Randomly sets dynamic level of phrase (and all repetition of it) to a random number between 25 and 100
      phr.setDynamic(random.randint(50, 85))
      
      for j in range(random.randint(a,b)):
         transposeUp(phr)
         
   # .1 chance of transposing down an octave 
   elif x > .9:
      
      phr.setDynamic(random.randint(50, 85))
      
      for j in range(random.randint(a,b)):
         transposeDown(phr)
   # .85 chance of normal octave
   
   else: 
      
      phr.setDynamic(random.randint(50, 85))
      # Add phr to phraseList somewhere between a and b number of times
      
      for j in range(random.randint(a,b)):
         # Creats copy of phrase 
         modPhr  = phr.copy()
         # Randomly adjusts the volume of each note in phrase by a factor of -10 to 10 
         Mod.shake(modPhr, 10)
         # Adds modified phrase to phraseList 
         phraseList.append(modPhr)
   
   # Add complete phraseList to part 
   i.addPhraseList(phraseList)
   
   # Empty phraseList 
   phraseList = []
   
   # Call dropout function 
   dropout()
   

def dropout():
   """Creates a chance for a part to drop out"""
   
   # Empty phraseList
   phraseList = []
   
   # .1 chance of dropping out 
   if random.random() < .15: 
      
      # Add somewhere between 40 and 80 beats of rest to phraseList
      for j in range(random.randint(40, 80)):
         phraseList.append(phr0)
         
      # Add phraseList to part 
      i.addPhraseList(phraseList)
      
      # Empty phraseList 
      phraseList = []


def transposeUp(phrUp):
   """Transposes a phrase up one octave"""
   
   # Create copy of phrase 
   modPhr = phrUp.copy()
   
   # Transpose the copy up one octave 
   Mod.transpose(modPhr, 12)
   
   # Randomly adjusts the volume of each note in phrase by a factor of -10 to 10 
   Mod.shake (modPhr, 10)
   
   # Add phrase to phraseList 
   phraseList.append(modPhr)
 
  
def transposeDown(phrDown):
   """Transposes a phrase down one octave"""
   
   # Create copy of phrase 
   modPhr = phrDown.copy()
   
   # Transpose the copy down one octave 
   Mod.transpose(modPhr, -12)
   
   # Randomly adjusts the volume of each note in phrase by a factor of -10 to 10 
   Mod.shake(modPhr, 10)
   
   # Add phrase to phraseList 
   phraseList.append(modPhr)
   
 
# Cycle through every part         
for i in partList:

   # Construct part for phr0. Will be repeated between 8 and 30 times  
   partBuild(phr0, 16, 64)
   
   # Construct part for phr1. Will be repeated between 7 and 17 times 
   partBuild(phr1, 17, 39)
   
   # cont. 
   partBuild(phr2, 25, 59)
   
   partBuild(phr3, 25, 59)
   
   partBuild(phr4, 25, 59)
   
   partBuild(phr5, 25, 59)
   
   partBuild(phr6, 6, 15)
   
   partBuild(phr7, 6, 13)
   
   partBuild(phr8, 4, 8)
   
   partBuild(phr9, 13, 29)
   
   partBuild(phr10, 102, 236)
   
   partBuild(phr11, 34, 79)
   
   partBuild(phr12, 9, 20)
   
   partBuild(phr13, 9, 20)
   
   partBuild(phr14, 3, 7)
   
   partBuild(phr15, 13, 29)
   
   partBuild(phr16, 51, 118)
   
   partBuild(phr17, 34, 79)
   
   partBuild(phr18, 25, 59)
   
   partBuild(phr19, 17, 39)
   
   partBuild(phr20, 17, 39)
   
   partBuild(phr21, 17, 39)
   
   partBuild(phr22, 4, 9)
   
   partBuild(phr23, 4, 10)
   
   partBuild(phr24, 5, 11)
   
   partBuild(phr25, 5, 11)
   
   partBuild(phr26, 5, 12)
   
   partBuild(phr27, 17, 39)
   
   partBuild(phr28, 25, 59)
   
   partBuild(phr29, 6, 13)
   
   partBuild(phr30, 9, 20)
   
   partBuild(phr31, 34, 79)
   
   partBuild(phr32, 9, 20)
   
   partBuild(phr33, 51, 118)
   
   partBuild(phr34, 102, 236)
   
   partBuild(phr35, 2, 4)
   
   partBuild(phr36, 34, 79)
   
   partBuild(phr37, 102, 236)
   
   partBuild(phr38, 68, 157)
   
   partBuild(phr39, 34, 79)
   
   partBuild(phr40, 102, 236)

   partBuild(phr41, 102, 236)
   
   partBuild(phr42, 3, 7)
   
   partBuild(phr43, 9, 20)
   
   partBuild(phr44, 9, 20)
   
   partBuild(phr45, 9, 20)
   
   partBuild(phr46, 10, 24)
   
   partBuild(phr47, 51, 118)
   
   partBuild(phr48, 3, 8)
   
   partBuild(phr49, 34, 79)
   
   partBuild(phr50, 102, 236)
   
   partBuild(phr51, 68, 157)
   
   partBuild(phr52, 102, 236)
   
   partBuild(phr53, 102, 236)
   
   # Checks if entire part needs to be transposed 
   if i in highParts:
      Mod.transpose(i, 12)
   if i in lowParts:
      Mod.transpose(i, -12)
   if i in lowestParts:
      Mod.transpose(i, -24)
   

# Adds each part to the score 
fullScore.addPart(part1)
fullScore.addPart(part2)
fullScore.addPart(part3)
fullScore.addPart(part4)
fullScore.addPart(part5)
fullScore.addPart(part6)
fullScore.addPart(part7)
fullScore.addPart(part8)
fullScore.addPart(part9)
fullScore.addPart(part10)
fullScore.addPart(part11)
fullScore.addPart(part12)
fullScore.addPart(part13)
fullScore.addPart(part14)
fullScore.addPart(part15)
fullScore.addPart(part16)

# Repeats phr00 until the end of the score plus two additional measures 
Mod.repeat(phr00, ((int(fullScore.getEndTime()) // 4) + 2))
# Adds phr00 to part 0
part0.addPhrase(phr00)
# Adds part0 to score 
fullScore.addPart(part0) 

# Plays score 
Play.midi(fullScore) 

# Export midi file 
# Write.midi(fullScore, "In C.mid")
