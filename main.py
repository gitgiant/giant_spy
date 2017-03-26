import threading

# TODO implement threading
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
