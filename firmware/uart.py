
import sys


def run(show, get_input):
    show("uart running")
    while True:
        live = select.select[0]

        data = sys.stdin.readline()
        
        if data:
            show(data)
        uinpt = get_input()
        if uinpt == "esc":
            return
