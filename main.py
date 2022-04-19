# Cycle Thru Alphabet

def on_button_pressed_a():
    global inString, cArrayChar, iArrayLocation, LastCharSet, MsgSent
    if MsgSent == 1:
        inString = ""
    basic.show_string("" + (text_list[iArrayLocation]))
    cArrayChar = text_list[iArrayLocation]
    iArrayLocation += 1
    if iArrayLocation >= len(text_list):
        iArrayLocation = 0
    LastCharSet = 0
    MsgSent = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

# Build Morse Alphabet
def fnMorseAlphabet(inChar: str):
    if inChar == "A":
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "B":
        fnDash()
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "C":
        fnDash()
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "D":
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "E":
        fnDot()
        fnPipe()
    elif inChar == "F":
        fnDot()
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "G":
        fnDash()
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "H":
        fnDot()
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "I":
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "J":
        fnDot()
        fnDash()
        fnDash()
        fnDash()
        fnPipe()
    elif inChar == "K":
        fnDash()
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "L":
        fnDot()
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "M":
        fnDash()
        fnDash()
        fnPipe()
    elif inChar == "N":
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "O":
        fnDash()
        fnDash()
        fnDash()
        fnPipe()
    elif inChar == "P":
        fnDot()
        fnDash()
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "Q":
        fnDash()
        fnDash()
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "R":
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    elif inChar == "S":
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    elif inChar == "T":
        fnDash()
        fnPipe()
    elif inChar == "U":
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "V":
        fnDot()
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "W":
        fnDot()
        fnDash()
        fnDash()
        fnPipe()
    elif inChar == "X":
        fnDash()
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    elif inChar == "Y":
        fnDash()
        fnDot()
        fnDash()
        fnDash()
        fnPipe()
    elif inChar == "Z":
        fnDash()
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
# Display Pipe
def fnPipe():
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
# Send/Display Msg

def on_button_pressed_ab():
    global inString, LastCharSet, MsgSent
    if LastCharSet == 0:
        inString = "" + inString + cArrayChar
        LastCharSet = 1
    radio.send_string(inString)
    MsgSent = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Receive Msg

def on_received_string(receivedString):
    global iArrayLocation, durPause, currChar, lenString
    iArrayLocation = 0
    durPause = 1000
    currChar = 0
    lenString = len(receivedString)
    while currChar < lenString:
        fnMorseAlphabet(receivedString.char_at(currChar))
        currChar += 1
radio.on_received_string(on_received_string)

# Append Letter to Msg

def on_button_pressed_b():
    global inString, iArrayLocation, LastCharSet, MsgSent
    inString = "" + inString + cArrayChar
    iArrayLocation = 0
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    LastCharSet = 1
    MsgSent = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# Display Dash
def fnDash():
    hummingbird.set_led(ThreePort.ONE, 100)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    hummingbird.set_led(ThreePort.ONE, 0)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
# Display Dot
def fnDot():
    hummingbird.set_led(ThreePort.ONE, 100)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    basic.pause(10)
    hummingbird.set_led(ThreePort.ONE, 0)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
lenString = 0
currChar = 0
durPause = 0
LastCharSet = 0
cArrayChar = ""
MsgSent = 0
inString = ""
iArrayLocation = 0
text_list: List[str] = []
radio.set_group(138)
text_list = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "_"]
iArrayLocation = 0
inString = ""
MsgSent = 0