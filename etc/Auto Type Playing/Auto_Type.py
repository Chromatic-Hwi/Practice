import pyautogui
import pyperclip
import time
#========================================================================================

note2key = {"C04":"Z", "C#4":"S", "D04":"X", "D#4":"D", "E04":"C",
            "F04":"V", "F#4":"G", "G04":"B", "G#4":"H", "A04":"N", "A#4":"J", "B04":"M",
            "C05":"Q", "C#5":"2", "D05":"W", "D#5":"3", "E05":"E",
            "F05":"R", "F#5":"5", "G05":"T", "G#5":"6", "A05":"Y", "A#5":"7", "B05":"U",
            "XXX":""}

code2ms_key = ["n1\n", "N1\n", "n2\n", "N2\n", "n4\n", "N4\n", "n8\n", "N8\n"]
#=========================================================================================

file = open("sheet1.txt", 'r')

idx = 0
while True:
    if idx == 0:
        song = file.readline()
        info = pyautogui.alert(text=f"Song : {song}", title='Info', button='OK')
        print(info)
        time.sleep(3)
        
    elif idx == 1:
        bpm = float(file.readline())  # cal playtime ms using bpm
        n4 = round(60/bpm, 2)         # quarter note
        N4 = round(n4/2*3, 2)         # dotted quarter note
        n1 = round(n4 * 4, 2)         # whole note
        N1 = round(n1/2*3, 2)
        n2 = round(n4 * 2, 2)         # half note
        N2 = round(n2/2*3, 2)
        n8 = round(n4/2, 2)           # eighth note
        N8 = round(n8/2*3, 2)
        
        code2ms_val = [n1, N1, n2, N2, n4, N4, n8, N8]
        code2ms = {k:v for k,v in zip(code2ms_key, code2ms_val)}

        print(code2ms)
        time.sleep(1)
        
    else:
        line = file.readline()
        if not line: break
        if line=="\n":
            pass
        else:
            key = note2key[line[:3]]
            ms = code2ms[line[4:]]
            #print(key, ms)
            if key == "XXX":
                #쉼표
                time.sleep(ms)
                pass
            else:
                pyautogui.keyDown(key)
                time.sleep(ms)
                pyautogui.keyUp(key)

    idx += 1
    
file.close()

