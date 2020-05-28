from pynput.keyboard import Key, Controller
import time
#tamilsongs
ponepo="CBC CBC ACB ABG CBC CBC ACB ABG CBC CBC ACB ABG CBCDC CBC ACB ABG  C G A C G A CCBC CCBC AA CB AB CCBC CCBC AA CB AB E EA GGFG FFEF DF E E EA GGFG FFEF DF E"
takita="D#DCG D#DCG D#DCG D#DCG D#DCG D#GD#D CD#D CD#D CD#D CD#D C  D D# C  D D#  "
happy="G G A G C B G G A G D C G G G E C B A F F E C D C GGAGCB GGAGDC GGGECBA FFECDC GGAGCB GGAGDC GGGECBA FFECDC "
shape="D F D D F D D F D A A A Bb Bb Bb Bb Bb Bb D D D G G G Bb Bb Bb "
cofin="A#A#A#A#DDDDCCCCFFFFGGGGGGGGGGGGcA#AFGGDCA#AAACA#AAA#GGA#AA#AA#GGDCA#AAACA#AGGA#AA#A#BBA#AA#AA#GGDCA#AAACA#AGGA#AA#A#BBA#AA#AA#A#A#A#A#A#DDDDCCCCFFFFGGGGGGGGGGGGCA#AFGGDCA#AAACA#AGG "
keyboard=Controller()
time.sleep(2)
notes=cofin
for i in range(len(notes)):
    if notes[i]=='b' and notes[i+1]!='#':
        keyboard.press('v')
        keyboard.release('v')
    if notes[i]=='C' and notes[i+1]!='#':
        keyboard.press('b')
        keyboard.release('b')
    if notes[i]=='D' and notes[i+1]!='#':
        keyboard.press('n')
        keyboard.release('n')
    if notes[i]=='F' and notes[i+1]!='#':
        keyboard.press(',')
        keyboard.release(',')
    if notes[i]=='E' :
        keyboard.press('m')
        keyboard.release('m')
    if notes[i]=='B' and notes[i+1]!='#':
        keyboard.press('v')
        keyboard.release('v')
    if notes[i]=='A' and notes[i+1]!='#':
        keyboard.press('c')
        keyboard.release('c')
    if notes[i]=='G' and notes[i+1]!='#':
        keyboard.press('x')
        keyboard.release('x')
    if notes[i]=='C' and notes[i+1]=='#':
        keyboard.press('h')
        keyboard.release('h')
        i=i+1
    if notes[i]=='D' and notes[i+1]=='#':
        keyboard.press('j')
        keyboard.release('j')
        i=i+1
    if notes[i]=='F' and notes[i+1]=='#':
        keyboard.press('l')
        keyboard.release('l')
        i=i+1
   
   
    if notes[i]=='A' and notes[i+1]=='#':
        keyboard.press('f')
        keyboard.release('f')
        i=i+1
    if notes[i]=='G' and notes[i+1]=='#':
        keyboard.press(';')
        keyboard.release(';')
        i=i+1
        
    
    time.sleep(0.20)
    
