
import sys
import os
import re
from pprint import pprint

# -----------------------------------------------------------
test_text = '''
123
sss
123123
asdasdsd
REM GENRE "rock, demo"
REM DATE 2022
REM COMMENT "ALLic for nnm-club"
PERFORMER "Fleetwood Mac"
TITLE "Demo DTS CD-Audio #11 [DTS 5.1 CD-DA]"
FILE "Demo DTS CD-Audio #11 [DTS 5.1 CD-DA].wav" WAVE
  TRACK 01 AUDIO
    TITLE "Don't Stop"
    PERFORMER "Fleetwood Mac"    
    INDEX 01 00:00:00
  TRACK 02 AUDIO
    TITLE "Juke Box Hero"
    PERFORMER "Foreigner"    
    INDEX 00 03:10:59
    INDEX 01 03:10:60
  TRACK 03 AUDIO
    TITLE "I Only Wanna Be With You"
    PERFORMER "Hootie & The Blowfish"    
    INDEX 00 07:31:56
    INDEX 01 07:31:57
  TRACK 04 AUDIO
    TITLE "Sailing To Philadelphia"
    PERFORMER "Mark Knopfler"    
    INDEX 00 11:18:59
    INDEX 01 11:18:60
  TRACK 05 AUDIO
    TITLE "Enter Sandman"
    PERFORMER "Metallica"    
    INDEX 00 16:53:38
    INDEX 01 16:53:39
  TRACK 06 AUDIO
    TITLE "Brain Damage (Alan Parsons Mix)"
    PERFORMER "Pink Floyd"    
    INDEX 00 22:26:02
    INDEX 01 22:26:03
  TRACK 07 AUDIO
    TITLE "Shallow"
    PERFORMER "Porcupine Tree"    
    INDEX 00 25:53:20
    INDEX 01 25:53:21
  TRACK 08 AUDIO
    TITLE "Another One Bites"
    PERFORMER "Queen"    
    INDEX 00 30:09:38
    INDEX 01 30:09:39
  TRACK 09 AUDIO
    TITLE "Man On The Moon"
    PERFORMER "REM"    
    INDEX 00 33:46:65
    INDEX 01 33:46:66
'''

# -----------------------------------------------------------
def extract_groups_from_string(text, pattern):
    matches = re.findall(pattern, text)
    return matches

# -----------------------------------------------------------
def show_res(tmp_dict2):

    # print ("tmp_dict2")

    for key in tmp_dict2:
        value = tmp_dict2[key]
        #print(f'Ключ: {key}')
        #print(f'Ключ: {value["track_no"]} - {value["title"]} ({value["performer"]})')
        
        track_no = value.get("track_no", "")
        title = value.get("title", "Без названия")
        performer = value.get("performer", "")
        index0 = value.get("index0", "")
        index1 = value.get("index1", "")

        print(f'{track_no}. {performer} - {title} ({index1})')
        #pprint(value)

# -----------------------------------------------------------
def run_parse(content):
        
    content = list(filter(None, content.split('\n')))

    # print(content)

    tmp_dict = dict()
    tmp_dict2 = dict()
    fields_dict = dict()
    key = 0
    old_key = 0

    for el in content:
        el2 = el.lstrip() # подрезаем пробелы
        dig = extract_groups_from_string(el2, r'\d{2}')
        title = extract_groups_from_string(el2, r'TITLE "(.*)"')
        track_no = extract_groups_from_string(el2, r'TRACK (\d{2}) AUDIO')
        title = extract_groups_from_string(el2, r'TITLE "(.*)"')
        performer = extract_groups_from_string(el2, r'PERFORMER "(.*)"')
        index0 = extract_groups_from_string(el2, r'INDEX 00 (\d{2}:\d{2}:\d{2})')
        index1 = extract_groups_from_string(el2, r'INDEX 01 (\d{2}:\d{2}:\d{2})')
        # print(dig)
        #print(f'track_no - {track_no}')
        #print(f'title - {title}')
        # print(el[0])
        if tmp_dict == {}:
            #print('starts File')
            key2 = str(key)
            tmp_dict.update({key2: []})
        elif el2.startswith("TRACK") and dig[0].isdigit():
            #print('start track = ' + dig[0])
            old_key = key
            key = int(dig[0]) # key + 1
            key2 = str(key)
            
            # print(f'  key: {key}')
            # print(f'  key2: {key2}')
            #print(f'  len(tmp_dict2): {len(tmp_dict2)}')
            #print(f'  len(fields_dict): {len(fields_dict)}')
            if len(tmp_dict2) > 0 and len(fields_dict) > 0:
                #print('  save - fields_dict')
                # print(f'    tmp_dict2: {tmp_dict2}')
                #print(f'    fields_dict: {fields_dict}')
                tmp_dict2[str(old_key)] = fields_dict
                fields_dict = {};
            
            tmp_dict.update({key2: []})
            fields_dict = dict()
            if track_no:  fields_dict["track_no"] = track_no[0]
            tmp_dict2.update({key2: []})
            # print(f'tmp_dict2: {tmp_dict2}')
        elif key > 0:
            # print('new')
            key2 = str(key)
            # print(f'  key2: {key2}')
            tmp_dict[key2].append(el2)
            # fields_dict.update({"track_no": "1"})
            # fields_dict["track_no"] = key2
            if len(title):  fields_dict["title"] = title[0]
            if len(performer):  fields_dict["performer"] = performer[0]
            if len(index0):  fields_dict["index0"] = index0[0]
            if len(index1):  fields_dict["index1"] = index1[0]
        else :
            #print('new')
            key2 = str(key)
            # print(f'  key2: {key2}')
            tmp_dict[key2].append(el2)


    #print(f'  key: {key}')
    #print(f'  key2: {key2}')
    #print(f'  len(tmp_dict2): {len(tmp_dict2)}')
    #print(f'  len(fields_dict): {len(fields_dict)}')
    if len(tmp_dict2) > 0 and len(fields_dict) > 0:
        #print('  save - fields_dict')
        #print(f'    tmp_dict2: {tmp_dict2}')
        #print(f'    fields_dict: {fields_dict}')
        tmp_dict2[str(key)] = fields_dict
        
    show_res(tmp_dict2)

# -----------------------------------------------------------
'''
import chardet

def read_file(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    
    encoding = chardet.detect(rawdata)['encoding']
    print(f'Определившаяся кодировка - {encoding}')
    if not encoding:
        raise ValueError("Не удалось определить кодировку файла.")
    
    return rawdata.decode(encoding)
'''

# -----------------------------------------------------------

def main():

    fn = ''
    fout = ''
    
    '''    
    fn = r"D:\MUSIC\_ATMOS, DTS\Демонстрационный DTS 5.1 CD-Audio #11 (2022)\Demo DTS CD-Audio #11 [DTS 5.1 CD-DA].cue"

    # С ошибкой кодировки
    fn = r"D:\R_STUDIO\PRG\python\2025-01-17 cue2txt\cue2txt\tests\Demo DTS CD-Audio #7 [ALLic].cue"
    
    fn = r"D:\R_STUDIO\PRG\python\2025-01-17 cue2txt\cue2txt\tests\Demo DTS CD-Audio #7 [ALLic]_2.cue"

    fn = r"D:\R_STUDIO\PRG\python\2025-01-17 cue2txt\cue2txt\tests\Demo DTS CD-Audio #8_2.cue"
    # Хороший
    #fn = r"D:\R_STUDIO\PRG\python\2025-01-17 cue2txt\cue2txt\tests\Demo DTS CD-Audio #11 [DTS 5.1 CD-DA]2.cue"
    '''

    if len(sys.argv) > 1:
        fn = sys.argv[1]
        
    if len(sys.argv) > 2:
        fout = sys.argv[2]
    

    if len(fn) == 0:
        print("Ошибка: укажите имя текстового файла в качестве аргумента.")
        return

    '''
    print(f'File - {fn}')
    print(f'File out - {fout}')
    print()
    
    if fout and os.path.isfile(fout):
        print("Этот файл существует")
    '''
        
    try:
        with open(fn, 'r') as file:
            content = file.read()

            '''
            # Чтение содержимого файла
            try:
                content = read_file(fn)
            except ValueError as e:
                print(f"Произошла ошибка: {e}")
                return
            '''
            
            run_parse(content)
            #print(content)
            
    except FileNotFoundError:
        print(f"Файл '{fn}' не найден.")
        

     
# -----------------------------------------------------------

if __name__ == "__main__":
    main()
