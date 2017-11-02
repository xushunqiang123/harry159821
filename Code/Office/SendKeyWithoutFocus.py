import win32gui,win32api,win32con,time
# import pywinauto
'''
__author__ = "harry159821"
__email__ = "harry159821@gmail.com"

this code is not reliable, test on windows7

1.Install Office
    ja_office_professional_plus_2016_x86_x64_dvd_6968758.iso
    http://183.93.62.180/ja_office_professional_plus_2016_x86_x64_dvd_6968758.iso?fid=vGw5Q3NxP7hw28wQPy-O5mU-nzMA8DOVAAAAAGF32l4YDLicrs0fYK**rKLba0St&mid=666&threshold=150&tid=4C0E207DA3654BB833664853BD2BE9BC&srcid=119&verno=1

2.Install English Languaga And Switch UI Language To English
    setuplanguagepack.x86.en-us_.exe
    Or
    setuplanguagepack.x64.en-us_.exe

3.modify the exe path Then Run It


4.Windows10 May have Slow Process Problem
'''

result = 0
def findWindowsByTitle(title):
    global result
    result = 0
    def enumHandler(hwnd, lParam):
        global result
        if win32gui.IsWindowVisible(hwnd):
            if title in win32gui.GetWindowText(hwnd):
                result = hwnd
    win32gui.EnumWindows(enumHandler, None)
    return result
    
def findSubWindowsByClassName(hwnd,className):
    global result
    result = 0
    def enumHandler(hwnd, lparam):
        global result
        name = win32gui.GetClassName(hwnd)
        # print("child_hwnd: %d GetClassName: %s" % (hwnd, name))
        if className in name:
            result = hwnd
    win32gui.EnumChildWindows(hwnd, enumHandler, None)
    return result

# hwnd = pywinauto.findwindows.find_windows(title_re=".* - Notepad.*")
# hwnd = findSubWindowsByClassName(hwnd, "OK")

count = 10
while count:
    hwnd = findWindowsByTitle("Phonetic Guide")
    if hwnd != 0:
        break
    print "waitting"
    time.sleep(0.5)
    count = count-1

win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

'''
Office Mecro Code

Sub GetFuckShimeiji()
   
   Num = ActiveDocument.Sentences.Count
   
   For sen = 1 To Num
   
        ActiveDocument.Sentences(sen).Select
        
        ' Font Size 8
        'SendKeys "+{tab 3}", 2
        'SendKeys "+{s}", 2
        'SendKeys "{up 7}", 2
        'SendKeys "{down 4}", 2
        
        ' Offset 2
        'SendKeys "{tab}", 2
        'SendKeys "+{o}", 2
        'SendKeys "{up 2}", 2
        
        ' pass
        'SendKeys "{enter}", 4
                
        Shell ("F:\XXXXXXXXXX\SendKeyWithoutFocus.exe")
        
        Application.Run MacroName:="FormatPhoneticGuide"
   
   Next sen

End Sub
'''
