#Giant dictonary to hold key name and VK value
#VK_CODE = {'backspace':0x08,
#           'tab':0x09,
#           'clear':0x0C,
#           'enter':0x0D,
#           'shift':0x10,
#           'ctrl':0x11,
#           'alt':0x12,
#           'pause':0x13,
#           'caps_lock':0x14,
#           'esc':0x1B,
#           'spacebar':0x20,
#           'page_up':0x21,
#           'page_down':0x22,
#           'end':0x23,
#           'home':0x24,
#           'left_arrow':0x25,
#           'up_arrow':0x26,
#           'right_arrow':0x27,
#           'down_arrow':0x28,
#           'select':0x29,
#           'print':0x2A,
#           'execute':0x2B,
#           'print_screen':0x2C,
#           'ins':0x2D,
#           'del':0x2E,
#           'help':0x2F,
#           '0':0x30,
#           '1':0x31,
#           '2':0x32,
#           '3':0x33,
#           '4':0x34,
#           '5':0x35,
#           '6':0x36,
#           '7':0x37,
#           '8':0x38,
#           '9':0x39,
#           'a':0x41,
#           'b':0x42,
#           'c':0x43,
#           'd':0x44,
#           'e':0x45,
#           'f':0x46,
#           'g':0x47,
#           'h':0x48,
#           'i':0x49,
#           'j':0x4A,
#           'k':0x4B,
#           'l':0x4C,
#           'm':0x4D,
#           'n':0x4E,
#           'o':0x4F,
#           'p':0x50,
#           'q':0x51,
#           'r':0x52,
#           's':0x53,
#           't':0x54,
#           'u':0x55,
#           'v':0x56,
#           'w':0x57,
#           'x':0x58,
#           'y':0x59,
#           'z':0x5A,
#           'numpad_0':0x60,
#           'numpad_1':0x61,
#           'numpad_2':0x62,
#           'numpad_3':0x63,
#           'numpad_4':0x64,
#           'numpad_5':0x65,
#           'numpad_6':0x66,
#           'numpad_7':0x67,
#           'numpad_8':0x68,
#           'numpad_9':0x69,
#           'multiply_key':0x6A,
#           'add_key':0x6B,
#           'separator_key':0x6C,
#           'subtract_key':0x6D,
#           'decimal_key':0x6E,
#           'divide_key':0x6F,
#           'F1':0x70,
#           'F2':0x71,
#           'F3':0x72,
#           'F4':0x73,
#           'F5':0x74,
#           'F6':0x75,
#           'F7':0x76,
#           'F8':0x77,
#           'F9':0x78,
#           'F10':0x79,
#           'F11':0x7A,
#           'F12':0x7B,
#           'F13':0x7C,
#           'F14':0x7D,
#           'F15':0x7E,
#           'F16':0x7F,
#           'F17':0x80,
#           'F18':0x81,
#           'F19':0x82,
#           'F20':0x83,
#           'F21':0x84,
#           'F22':0x85,
#           'F23':0x86,
#           'F24':0x87,
#           'num_lock':0x90,
#           'scroll_lock':0x91,
#           'left_shift':0xA0,
#           'right_shift ':0xA1,
#           'left_control':0xA2,
#           'right_control':0xA3,
#           'left_menu':0xA4,
#           'right_menu':0xA5,
#           'browser_back':0xA6,
#           'browser_forward':0xA7,
#           'browser_refresh':0xA8,
#           'browser_stop':0xA9,
#           'browser_search':0xAA,
#           'browser_favorites':0xAB,
#           'browser_start_and_home':0xAC,
#           'volume_mute':0xAD,
#           'volume_Down':0xAE,
#           'volume_up':0xAF,
#           'next_track':0xB0,
#           'previous_track':0xB1,
#           'stop_media':0xB2,
#           'play/pause_media':0xB3,
#           'start_mail':0xB4,
#           'select_media':0xB5,
#           'start_application_1':0xB6,
#           'start_application_2':0xB7,
#           'attn_key':0xF6,
#           'crsel_key':0xF7,
#           'exsel_key':0xF8,
#           'play_key':0xFA,
#           'zoom_key':0xFB,
#           'clear_key':0xFE,
#           '+':0xBB,
#           ',':0xBC,
#           '-':0xBD,
#           '.':0xBE,
#           '/':0xBF,
#           '`':0xC0,
#           ';':0xBA,
#           '[':0xDB,
#           '\\':0xDC,
#           ']':0xDD,
#           "'":0xDE,
#           '`':0xC0}
#AHU  - 450M
#BAC  - 500M
#CEH  - 150M
#CEM  - 150M
#CHAC - 250M
#CIR  - 150M
#EOM  - 450M
#FEO  - 150M
#GAR  - 150M
#IGNI - 250M
#JAH  - 500M
#KRY  - 400M
#LAC  - 400M
#LITH - 250M
#LUM  - 150M
#MET  - 250M
#MONI - 150M
#MOT  - 250M
#NAGU - 450M
#NEO  - 150M
#NER  - 200M
#NOC  - 200M
#OHM  - 500M
#POC  - 150M
#QAX  - 200M
#QUA  - 100M
#QUE  - 300M
#TAL  - 100M
#TAM  - 300M
#TEB  - 100M
#TEC  - 100M
#THUL - 200M
#TON  - 250M
#TUN  - 150M
#TZIC - 400M
#VEX  - 300M
#WAT  - 200M
#XAL  - 300M
#XAN  - 300M
#XOL  - 400M
#YAX  - 100M
#YOM  - 200M
#YUL  - 150M
#ZAN  - 100M
#ZEC  - 100M

import win32api, win32con, time, multiprocessing

controller = False

def other_skills():
    global controller
    while True:
        if win32api.GetKeyState(0xBD)<0: # "-" Key closes the autobuffer.
            break

        if win32api.GetKeyState(0x79)<0: # "F10" Key activate the autobuffer.
            controller = True

        if win32api.GetKeyState(0x78)<0: # "F9" Key deactivate the autobuffer.
            controller = False


        if controller:
            if win32api.GetKeyState(0x02)<0:
                win32api.keybd_event(0x51, 0, 0, 0)
                win32api.keybd_event(0x51, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(0x45, 0, 0, 0)
                win32api.keybd_event(0x45, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(0x52, 0, 0, 0)
                win32api.keybd_event(0x52, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(0x46, 0, 0, 0)
                win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(0x31, 0, 0, 0)
                win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(0x20, 0, 0, 0)
                win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_KEYUP, 0)            
                time.sleep(.05)

def hydra():
    global controller
    while True:
        if win32api.GetKeyState(0xBD)<0: # "-" Key closes the autobuffer.
            break

        if win32api.GetKeyState(0x79)<0: # "F10" Key activate the autobuffer.
            controller = True

        if win32api.GetKeyState(0x78)<0: # "F9" Key deactivate the autobuffer.
            controller = False


        if controller:
            if win32api.GetKeyState(0x02)<0:
                win32api.keybd_event(0x58, 0, 0, 0)
                win32api.keybd_event(0x58, 0, win32con.KEYEVENTF_KEYUP, 0)           
                time.sleep(.4)

if __name__ == '__main__':
    multiprocessing.Process(target=hydra).start()
    multiprocessing.Process(target=other_skills).start()