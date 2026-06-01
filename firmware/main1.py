from machine import Pin, SPI, I2C
import ili9341
import time
import os

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
spi = SPI(1, baudrate = 40000000, sck = Pin(12), mosi = Pin(11))
screen = ili9341.Display(spi, dc=Pin(10), cs=Pin(9), rst=Pin(8))



while True:

    def show(text):
        show("type a command/help: :")
        display.clear(ili9341)
        lines = text.split("\n")
        for i, line in enumerate(lines):
            display.draw_text(10, 10 + i * 20, line, ili9341)
        
            def get_input():
                typed = ""
                show(typed)
                while True:
                    k = i2c.readfrom(0x5F, 1).decode("uft-8")
                    if k == "\r":
                        return(typed)
                    elif k == "\x1b":
                        return "esc"
                    elif k == "\x08":
                        typed = typed[:-1]
                    elif k !="\x00":
                        typed += k
                    show(typed)
        
            show("terminal\ntype help")
            time.sleep(1)
        
            while True:
                show("type command")
                user = get_input().lower()
            
                if user == "uart":
                    import uart
                    uart.run(show, get_input)
            
                elif user == "repl":
                    import REPL
                    REPL.run(show, get_input)
                
                elif user == "calc":
                    import calc
                    calc.run(show, get_input)
                
                elif user.startswith("text "):
                    filename = user.split("")[1]
                    
                    try:
                        open(filename, 'r').close()
                        show(filename + "\n edit/delete/leave")
                        command = get_input()
                    
                        if command == "edit":
                            import text
                            text.run(show, get_input, filename)
                        elif command == "delete":
                            os.remove(filename)
                            show("deleted")
                        elif command == "leave":
                            pass
                        else:
                            show("command not valid")
                            pass
            
                    except:
                        show(filename + "\n create/leave")
                        command = get_input()
                        if command == "create":
                            import text
                            text.run(show, get_input, filename)
                        elif command == "leave":
                            pass
                        
        
                
                elif user == "help":
                    show("uart \n REPL \n calc \n text")
                    time.sleep(2)
                
                elif user == "esc":
                    pass
            
                else:
                    show("unknown command: " + user)
                
                
            
            