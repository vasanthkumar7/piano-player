from pynput.keyboard import Key, Controller
import time
#tamilsongs
ponepo="CBC CBC ACB ABG CBC CBC ACB ABG CBC CBC ACB ABG CBCDC CBC ACB ABG  C G A C G A CCBC CCBC AA CB AB CCBC CCBC AA CB AB E EA GGFG FFEF DF E E EA GGFG FFEF DF E"
takita="D#DCG D#DCG D#DCG D#DCG D#DCG D#GD#D CD#D CD#D CD#D CD#D C  D D# C  D D#  "
happy="AA BADC# AA BAED AA A F# D C# B GG F# D E D AA B A D C# AA B A E D AA B F# D C# B GG F# D E D "

keyboard=Controller()
time.sleep(2)
notes=happy
for i in range(len(notes)):
    if notes[i]=='C' and notes[i+1]!='#':
        keyboard.press('i')
        keyboard.release('i')
    if notes[i]=='D' and notes[i+1]!='#':
        keyboard.press('o')
        keyboard.release('o')
    if notes[i]=='F' and notes[i+1]!='#':
        keyboard.press('r')
        keyboard.release('r')
    if notes[i]=='E' :
        keyboard.press('p')
        keyboard.release('p')
    if notes[i]=='B' and notes[i+1]!='#':
        keyboard.press('u')
        keyboard.release('u')
    if notes[i]=='A' and notes[i+1]!='#':
        keyboard.press('y')
        keyboard.release('y')
    if notes[i]=='G' and notes[i+1]!='#':
        keyboard.press('t')
        keyboard.release('t')
    if notes[i]=='C' and notes[i+1]=='#':
        keyboard.press('9')
        keyboard.release('9')
        i=i+1
    if notes[i]=='D' and notes[i+1]=='#':
        keyboard.press('0')
        keyboard.release('0')
        i=i+1
    if notes[i]=='F' and notes[i+1]=='#':
        keyboard.press('5')
        keyboard.release('5')
        i=i+1
   
   
    if notes[i]=='A' and notes[i+1]=='#':
        keyboard.press('7')
        keyboard.release('7')
        i=i+1
    if notes[i]=='G' and notes[i+1]=='#':
        keyboard.press('f')
        keyboard.release('f')
        i=i+1
        
    
    time.sleep(0.30)
    
