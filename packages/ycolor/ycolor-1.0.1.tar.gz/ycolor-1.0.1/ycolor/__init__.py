'''A convenient color text printing tool'''
import ctypes, sys
try:
    from ycolor import Back, Fore
except:
    import Back,Fore

handle = ctypes.windll.kernel32.GetStdHandle(-11)

class ColorError(Exception):
    pass

def printcolor(mess,end='\n',fore=Fore.WHITE,back=Back.BLACK):
    '''Print colored text'''
    try:
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, fore|back)
        sys.stdout.write(mess+end)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, Fore.WHITE)
    except:
        pass

def printcolor_text(mess,end='\n',color='WHITE+BLACK'):
    '''Print colored text in the format of "Fore+Back"
You can also choose not to enter Fore or (and) Back'''
    place = color.find('+')
    if place == -1:
        raise ColorError("You should type'Fore+Back")
    fore = color[:place]
    back = color[place+1:]
    fore = _printcolor_text_help(fore,'Fore',Fore.WHITE)
    back = _printcolor_text_help(back,'Back',Back.BLACK)
    printcolor(mess,end=end,fore=fore,back=back)

def _printcolor_text_help(what,whattext,whatelse):
    error = ()
    if what == '':
        whatreturn = whatelse
    else:
        try:
            whatreturn = eval(whattext + '.' + what)
        except:
            error = (whattext,what)
    if error != ():
        raise ColorError(error[0]+" don't have color "+error[1])
    else:
        return whatreturn

if __name__ == '__main__':
    printcolor('hello')
    printcolor_text('hello',color='+')
