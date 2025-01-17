# CUE to TXT conver

Python приложение преобразует файлы CUE (Трек-лист компакт-диска) в текстовый формат

**Формат запуска приложения**

    py cue2txt.py CUE_FILE_NAME [TXT_FILE_NAME]

, где

    CUE_FILE_NAME - Путь к файлу .CUE
    TXT_FILE_NAME - Путь к файлу вывода


***Формат выходного файла:***

    TRACK. PERFORMER - TITLE (INDEX 01)
    ...
    
**, например:**

    01. Seal 2007 - Amazing (00:00:00)
    02. Groove Armada 2001 - Drifted (03:27:63)
    03. The Doobie Brothers 1973 - Long Train Runnin (08:24:04)
    04. Sheryl Crow 1986 - Everyday Is A Winding Road (11:42:44)
    05. Groove Armada 2001 - Fogma (16:06:69)
    06. Lady Gaga 2008 - Poker Face (23:02:00)
    07. Netherlands Philharmonic Orchestra 2003 - Antonin Dvorak - Symphony No. 9 (27:01:05)
    08. Pas De Deux - Tchaikovsky - The Nutcracker (38:49:56)
    09. Groove Armada 2001 - Lazy Moon (43:07:26)
    10. Tears For Fears 1985 - Shout (49:43:34)
    11. Fine Young Cannibals 1989 - She Drives Me Crazy (56:20:61)
    12. Groove Armada 2001 - Edge Hill (59:46:49)
    13. Foreigner 1977 - Cold As Ice (66:41:69)
    14. San Francisco Symphony - Ludwig van Beethoven - Symphony No. 5 (70:02:27)
        
***Требования для компиляции и запуска:***

1) Установить Python

***Известные проблемы:***

Ошибка неверных символов

  * Описание - Появляется ошибка с парсингом символов, если в тексте CUE файла есть непечатные символы.
  * Решение - Удалить или исправить сбойные символы в исходном файле
