import sys
def run(show, get_input):
    while True:
    
        
        show("type comand: ")
        cmd = get_input()
        
        if cmd == "esc":
            return
        
        cmd().lower()
    
        sys.stdout.write("cmd: " + cmd)
        
        data = sys.stdin.readline()
        show(data)
       
       
    
        