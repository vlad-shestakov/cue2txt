rem py cue2txt.py %1 %2

del "cue2txt_test_cue_example.txt"

py cue2txt.py^
 "cue2txt_test_cue_example.cue"^
 "cue2txt_test_cue_example.txt"

pause