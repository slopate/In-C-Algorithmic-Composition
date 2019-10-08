# List of all  phrases for IN C

from music import *

# Creates a new phrase
phr00 = Phrase()
# Defines a list of pitch values
pitches00 = [C7, C7, C7, C7, C7, C7, C7, C7]
# Defines a list of note length values
durations00 = [EN, EN, EN, EN, EN, EN, EN, EN]
# Defines a list of dynamic level values
dynamics00 = [F, F, F, F, F, F, F, F]
# Adds pitch values with corresponding note lengths and dynamics values to the phrase
phr00.addNoteList(pitches00, durations00, dynamics00)

phr0 = Phrase()
pitches0 = [REST]
durations0 = [QN]
phr0.addNoteList(pitches0, durations0)
#Mod.repeat(phr0, random.randint(0, 5))

phr1 = Phrase()
pitches1 = [C4, E4, C4, E4, C4, E4]
durations1 = [TN, EN+DSN, TN, EN+DSN, TN, EN+DSN]
phr1.addNoteList(pitches1, durations1)
# Mod.repeat(phr1, random.randint(30, 70))

phr2 = Phrase()
pitches2 = [C4, E4, F4, E4]
durations2 = [TN, DSN, EN, QN]
phr2.addNoteList(pitches2, durations2) 
# Mod.repeat(phr2, random.randint(45, 105))

phr3 = Phrase()
pitches3 = [REST, E4, F4, E4]
durations3 = [EN, EN, EN, EN]
phr3.addNoteList(pitches3, durations3)
# Mod.repeat(phr3, random.randint(45, 105))

phr4 = Phrase()
pitches4 = [REST, E4, F4, G4]
durations4 = [EN, EN, EN, EN]
phr4.addNoteList(pitches4, durations4)
# Mod.repeat(phr4, random.randint(45, 105))

phr5 = Phrase()
pitches5 = [E4, F4, G4, REST]
durations5 = [EN, EN, EN, EN]
phr5.addNoteList(pitches5, durations5)
# Mod.repeat(phr5, random.randint(45, 105))

phr6 = Phrase()
pitches6 = [C5]
durations6 = [WN+WN]
phr6.addNoteList(pitches6, durations6)
# Mod.repeat(phr6, random.randint(11, 26))

phr7 = Phrase()
pitches7 = [REST, REST, C4, C4, C4, REST, REST]
durations7 = [HN, DQN, SN, SN, EN, DQN, DHN]
phr7.addNoteList(pitches7, durations7)
#Mod.repeat(phr7, random.randint(10, 23))

phr8 = Phrase()
pitches8 = [G4, F4]
# '+' symbol indicates tied note length values 
durations8 = [WN+HN, WN+WN]
phr8.addNoteList(pitches8, durations8)
#Mod.repeat(phr8, random.randint(6, 15))

phr9 = Phrase()
pitches9 = [B4, G4, REST, REST]
durations9 = [SN, SN, DQN, HN]
phr9.addNoteList(pitches9, durations9)
#Mod.repeat(phr9, random.randint(22, 52))

phr10 = Phrase()
pitches10 = [B4, G4]
durations10 = [SN, SN]
phr10.addNoteList(pitches10, durations10)
#Mod.repeat(phr10, random.randint(180, 420))

phr11 = Phrase()
pitches11 = [F4, G4, B4, G4, B4, G4]
durations11 = [SN, SN, SN, SN, SN, SN]
phr11.addNoteList(pitches11, durations11)
#Mod.repeat(phr11, random.randint(60, 140))

phr12 = Phrase()
pitches12 = [F4, G4, B4, C5]
durations12 = [EN, EN, WN, QN]
phr12.addNoteList(pitches12, durations12)
#Mod.repeat(phr12, random.randint(15, 35))

phr13 = Phrase()
pitches13 = [B4, G4, G4, F4, G4, REST, G4] 
durations13 = [SN, DEN, SN, SN, EN, DEN, SN+DHN]
phr13.addNoteList(pitches13, durations13)
#Mod.repeat(phr13, random.randint(15, 35))

phr14 = Phrase()
pitches14 = [C5, B4, G4, FS4]
durations14 = [WN, WN, WN, WN]
phr14.addNoteList(pitches14, durations14)
#Mod.repeat(phr14, random.randint(6, 13))

phr15 = Phrase()
pitches15 = [G4, REST, REST, REST]
durations15 = [SN, DEN, QN, HN]
phr15.addNoteList(pitches15, durations15)
#Mod.repeat(phr15, random.randint(22, 52))

phr16 = Phrase()
pitches16 = [G4, B4, C5, B4]
durations16 = [SN, SN, SN, SN]
phr16.addNoteList(pitches16, durations16)
#Mod.repeat(phr16, random.randint(90, 210))

phr17 = Phrase()
pitches17 = [B4, C5, B4, C5, B4, REST]
durations17 = [SN, SN, SN, SN, SN, SN]
phr17.addNoteList(pitches17, durations17)
#Mod.repeat(phr17, random.randint(60, 140))

phr18 = Phrase()
pitches18 = [E4, FS4, E4, FS4, E4, E4]
durations18 = [SN, SN, SN, SN, DEN, SN]
phr18.addNoteList(pitches18, durations18)
#Mod.repeat(phr18, random.randint(45, 105))

phr19 = Phrase()
pitches19 = [REST, G5]
durations19 = [DQN, DQN]
phr19.addNoteList(pitches19, durations19)
#Mod.repeat(phr19, random.randint(30, 70))

phr20 = Phrase()
pitches20 = [E4, FS4, E4, FS4, G3, E4, FS4, E4, FS4, E4]
durations20 = [SN, SN, SN, SN, DEN, SN, SN, SN, SN, SN]
phr20.addNoteList(pitches20, durations20)
#Mod.repeat(phr20, random.randint(30, 70))

phr21 = Phrase()
pitches21 = [FS4]
durations21 = [DHN]
phr21.addNoteList(pitches21, durations21)
#Mod.repeat(phr21, random.randint(30, 70))

phr22 = Phrase()
pitches22 = [E4, E4, E4, E4, E4, FS4, G4, A4, B4]
durations22 = [DQN, DQN, DQN, DQN, DQN, DQN, DQN, DQN, EN]
phr22.addNoteList(pitches22, durations22)
#Mod.repeat(phr22, random.randint(7, 17))

phr23 = Phrase()
pitches23 = [E4, FS4, FS4, FS4, FS4, FS4, G4, A4, B4]
durations23 = [EN, DQN, DQN, DQN, DQN, DQN, DQN, DQN, QN]
phr23.addNoteList(pitches23, durations23)
#Mod.repeat(phr23, random.randint(7, 17))

phr24 = Phrase()
pitches24 = [E4, FS4, G4, G4, G4, G4, G4, A4, B4]
durations24 = [EN, EN, DQN, DQN, DQN, DQN, DQN, DQN, EN]
dynamics24 = [MF, MF, MF, MF, MF, MF, MF, MF, MF]
phr24.addNoteList(pitches24, durations24, dynamics24)
#Mod.repeat(phr24, random.randint(9, 20))

phr25 = Phrase()
pitches25 = [E4, FS4, G4, A4, A4, A4, A4, A4, B4]
durations25 = [EN, EN, EN, DQN, DQN, DQN, DQN, DQN, DQN]
dynamics25 = [MF, MF, MF, MF, MF, MF, MF, MF, MF]
phr25.addNoteList(pitches25, durations25, dynamics25)
#Mod.repeat(phr25, random.randint(9, 20))

phr26 = Phrase()
pitches26 = [E4, FS4, G4, A4, B4, B4, B4, B4, B4]
durations26 = [EN, EN, EN, EN, DQN, DQN, DQN, DQN, DQN]
phr26.addNoteList(pitches26, durations26)
#Mod.repeat(phr26, random.randint(9, 22))

phr27 = Phrase()
pitches27 = [E4, FS4, E4, FS4, G4, E4, G4, FS4, E4, FS4, E4]
durations27 = [SN, SN, SN, SN, EN, SN, SN, SN, SN, SN, SN]
phr27.addNoteList(pitches27, durations27)
#Mod.repeat(phr27, random.randint(30, 70))

phr28 = Phrase()
pitches28 = [E4, FS4, E4, FS4, E4, E4]
durations28 = [SN, SN, SN, SN, DEN, SN]
phr28.addNoteList(pitches28, durations28)
#Mod.repeat(phr28, random.randint(45, 105))

phr29 = Phrase()
pitches29 = [E4, G4, C5]
durations29 = [DHN, DHN, DHN]
phr29.addNoteList(pitches29, durations29)
#Mod.repeat(phr29, random.randint(10, 23))

phr30 = Phrase()
pitches30 = [C5]
durations30 = [WN+HN]
phr30.addNoteList(pitches30, durations30)
#Mod.repeat(phr30, random.randint(15, 35))

phr31 = Phrase()
pitches31 = [G4, F4, G4, B4, G4, B4]
durations31 = [SN, SN, SN, SN, SN, SN]
phr31.addNoteList(pitches31, durations31)
#Mod.repeat(phr31, random.randint(60, 140))

phr32 = Phrase()
pitches32 = [F4, G4, F4, G4, B4, F4, G4]
durations32 = [SN, SN, SN, SN, SN, SN+DHN, DQN]
phr32.addNoteList(pitches32, durations32)
#Mod.repeat(phr32, random.randint(15, 35))

phr33 = Phrase()
pitches33 = [G4, F4, REST]
durations33 = [SN, SN, EN]
phr33.addNoteList(pitches33, durations33)
#Mod.repeat(phr33, random.randint(90, 210))

phr34 = Phrase()
pitches34 = [G4, F4]
durations34 = [SN, SN]
phr34.addNoteList(pitches34, durations34)
#Mod.repeat(phr34, random.randint(180, 420))

phr35 = Phrase()
pitches35 = [F4, G4, B4, G4, B4, G4, B4, G4, B4, G4, REST, REST, BF4, G5, A5, G5, B5, A5, G5, E5, G5, FS5, REST, REST, E5, F5]
durations35 = [SN, SN, SN, SN, SN, SN, SN, SN, SN, SN, DQN, HN, QN, DHN, EN, QN, EN, DQN, EN, DHN, EN, EN+DHN, QN, DQN, EN+HN, WN+HN]
phr35.addNoteList(pitches35, durations35)
#Mod.repeat(phr35, random.randint(3, 7))

phr36 = Phrase()
pitches36 = [F4, G4, B4, G4, B4, G4]
durations36 = [SN, SN, SN, SN, SN, SN]
phr36.addNoteList(pitches36, durations36)
#Mod.repeat(phr36, random.randint(60, 140))

phr37 = Phrase()
pitches37 = [F4, G4]
durations37 = [SN, SN]
phr37.addNoteList(pitches37, durations37)
#Mod.repeat(phr37, random.randint(180, 420))

phr38 = Phrase()
pitches38 = [F4, G4, B4]
durations38 = [SN, SN, SN]
phr38.addNoteList(pitches38, durations38)
#Mod.repeat(phr38, random.randint(120, 280))

phr39 = Phrase()
pitches39 = [B4, G4, F4, G4, B4, C5]
durations39 = [SN, SN, SN, SN, SN, SN]
phr39.addNoteList(pitches39, durations39)
#Mod.repeat(phr39, random.randint(60, 140))

phr40 = Phrase()
pitches40 = [B4, F4]
durations40 = [SN, SN]
phr40.addNoteList(pitches40, durations40)
#Mod.repeat(phr40, random.randint(180, 420))

phr41 = Phrase()
pitches41 = [B4, G4]
durations41 = [SN, SN]
phr41.addNoteList(pitches41, durations41)
#Mod.repeat(phr41, random.randint(180, 420))

phr42 = Phrase()
pitches42 = [C5, B4, A4, C5]
durations42 = [WN, WN, WN, WN]
phr42.addNoteList(pitches42, durations42)
#Mod.repeat(phr42, random.randint(6, 13))

phr43 = Phrase()
pitches43 = [F5, E5, F5, E5, E5, E5, E5, F5, E5]
durations43 = [SN, SN, SN, SN, EN, EN, EN, SN, SN]
phr43.addNoteList(pitches43, durations43)
#Mod.repeat(phr43, random.randint(30, 70))

phr44 = Phrase()
pitches44 = [F5, E5, E5, C5]
durations44 = [EN, QN, EN, QN]
phr44.addNoteList(pitches44, durations44)
#Mod.repeat(phr44, random.randint(30, 70))

phr45 = Phrase()
pitches45 = [D5, D5, G4]
durations45 = [QN, QN, QN]
phr45.addNoteList(pitches45, durations45)
#Mod.repeat(phr45, random.randint(30, 70))

phr46 = Phrase()
pitches46 = [G4, D5, E5, D5, REST, G4, REST, G4, REST, G4, G4, D5, E5, D5]
durations46 = [SN, SN, SN, SN, EN, EN, EN, EN, EN, EN, SN, SN, SN, SN]
phr46.addNoteList(pitches46, durations46)
#Mod.repeat(phr46, random.randint(18, 42))

phr47 = Phrase()
pitches47 = [D5, E5, D5]
durations47 = [SN, SN, EN]
phr47.addNoteList(pitches47, durations47)
#Mod.repeat(phr47, random.randint(90, 210))

phr48 = Phrase()
pitches48 = [G4, G4, F4]
durations48 = [WN+HN, WN, WN+QN]
phr48.addNoteList(pitches48, durations48)
#Mod.repeat(phr48, random.randint(6, 14))

phr49 = Phrase()
pitches49 = [F4, G4, BF4, G4, BF4, G4]
durations49 = [SN, SN, SN, SN, SN, SN]
phr49.addNoteList(pitches49, durations49)
#Mod.repeat(phr49, random.randint(60, 140))

phr50 = Phrase()
pitches50 = [F4, G4]
durations50 = [SN, SN]
phr50.addNoteList(pitches50, durations50)
#Mod.repeat(phr50, random.randint(180, 420))

phr51 = Phrase()
pitches51 = [F4, G4, BF4]
durations51 = [SN, SN, SN]
phr51.addNoteList(pitches51, durations51)
#Mod.repeat(phr51, random.randint(120, 280))

phr52 = Phrase()
pitches52 = [G4, BF4]
durations52 = [SN, SN]
phr52.addNoteList(pitches52, durations52)
#Mod.repeat(phr52, random.randint(180, 420))

phr53 = Phrase()
pitches53 = [BF4, G4]
durations53 = [SN, SN]
phr53.addNoteList(pitches53, durations53)
#Mod.repeat(phr53, random.randint(180, 420))
