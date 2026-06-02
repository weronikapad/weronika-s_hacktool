## Weronika's Hacktool

A raspberry pi Pico based hardware tool that can be pluged via USB-A or or a connecting wire betwen raspberry's pi pico and a device that you're connecting it to.

## Specifics
Raspberry pi pico is powered by a LiPo battery, that is charged through USB-A and the voltage that pico recives is controled by the power managment. 
1. specifics to connecting hardware parts
   a) battery
       - connect it with a male to male wire to a connector pin socket 01x02
   b) keyboard (look at connector pins on conn_01x04 from KiCad view), (use female to female wires)
     - Pin1 -> wrire -> the pin in the keyboard port that the black wire from the picture goes into
     - Pin2 -> wrire -> the pin in the keyboard port that the red wire from the picture goes into
     - Pin3 -> wrire -> the pin in the keyboard port that the white wire from the picture goes into
     - Pin4 -> wrire -> the pin in the keyboard port that the yellow wire from the picture goes into
<img src="images/keyboardspecifics.png" alt="keyboardspecifics" width="800"/>

    c) screen (use female to female wires)(look at connector pins on conn_01x09 from KiCad view)
      - Pin1 -> wire -> vcc on the screen
      - Pin2 -> wire -> GND on the screen
      - Pin3 -> wire -> CS on the screen
      - Pin4 -> wire -> SDO(MISO) on the screen
      - Pin5 -> wire -> SCK on the screen
      - Pin6 -> wire -> SDI(MOSI) on the screen
      - Pin7 -> wire -> DC on the screen
      - Pin8 -> wire -> LED on the screen

  <img src="images/backofscreen.png" alt="backofscreen" width="800"/>


## Features

-Raspberry pi Pico
-SD card port (microSD_HC_Molex_104031-0811)
-USB-A (USB_A_CNCTech_1001-011-01101_Horizontal)
-2000 Ohm resistor
-Power manager (TP4057)
-LCD display 
-Keyboard
-LiPo Battry
-Connectors on PCB for screen, keyboard and battery conection

## PCB 
Designed in KiCad, through pico's USB using REPL, pico can send commands to pluged pc and recive and print output, and through UART it can monitor trafic. Independently it can serve as a calculator or a text editor.

**PCB's front copper layer view in KiCad**

<img src="images/pcbfcu.png" alt="pcbfcu" width="800"/>

**PCB's back copper layer view in KiCad**

<img src="images/pcbbcu.png" alt="pcbbcu" width="800"/>

**PCB's 3D model, with exact location of specific connectors**

<img src="images/3dpcd.pdf.jpg" alt="3dpcb" width="800"/>

## Schematic

<img src="images/Screenshot 2026-06-01 204912.png" alt="Screenshot 2026-06-01 204912" width="800"/>

## detailed description on how to use

1. dowloand firmware for pico, and pc
2. dowloand tonny
3. works best with an sd card connected
4. before asebeling everything in the box:
   - plug raspberry pico via wire to your pc
   - push firmware files onto pico
5. to stop any program at any time press esc
6. in order to use the REPL program, or UART:
   - connect pico to at least the screen, and and keyboard
   a) for REPL:
      - in the terminal type "repl"
      - then type the command that you wish to run in your pluged device
     - pico is programed to always run in administrator mode in your pc's cmd so, in order for the rogram to run as inteded you must allow it on your pc
    b) for UART:
      -in the terminal type "uart"
7. to use the hacktool independently:
   - connect the pcb to keyboard, screen, and battery
   - charge the battery via USB-A
   a) to use the text editor:
      - type in the termianl "text" + your filename (it can be alredy saved on sd card or can be created by this command)
        if the file exists:
          - to edit the file type "edit"
          - to delete type "delete"
          - if you change your mind and you no longer wish to engange with the text editor type "leave"
        if it doesn't:
          - type "create" to create it and open it
          - type "leave" if you don't wish to create
8. if you forgot any of those commands type "help" in the main terminal
        



