
import serial
import subprocess
import ctypes
import sys

print("running")
def admin():
    try:
        print(ctypes.windll.shell32.IsUserAdmin)
        return ctypes.windll.shell32.IsUserAdmin
    except:
        return False
if not admin():
    ctypes.windll.shell32.ShellExecuteW(    None, "run as", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit

from serial.tools import list_ports

def find_pico():
    ports = list_ports()
    for port in ports:
        if "RP2040" in list_ports or "USB Serial" in list_ports:
            return port.device
    return None
port = find_pico()

if port is None:
    print("pico not found")
    sys.exit()
else:
    print("pico on: " + port)


pico = serial.Serial(port, 115200)
# rfc2217ServerPort = 4000

print("type command on pico")

while True:
    textplsc = pico.read() #raw
    textplsc = textplsc.decode().strip()
    print("picoinput: " + textplsc)

    if textplsc.startswith("cmd: "):
        cmd = textplsc[5:]
    if cmd.startswith("fech "):
        filename = cmd.slip(" ")[1]
        try:
            f = open(filename, "r")
            data = f.read
            f.close()
            pico.write((data).encode())
        except:
            pico.write((filename + " not found").encode())
    else:
        result = subprocess.run(cmd, shell = True, capture.output = True, text = True )
        if output == "":
            output = result.stderr
        pico.write((output).encode())
