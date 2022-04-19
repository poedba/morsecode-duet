// Cycle Thru Alphabet
input.onButtonPressed(Button.A, function () {
    if (MsgSent == 1) {
        inString = ""
    }
    basic.showString("" + (text_list[iArrayLocation]))
    cArrayChar = text_list[iArrayLocation]
    iArrayLocation += 1
    if (iArrayLocation >= text_list.length) {
        iArrayLocation = 0
    }
    LastCharSet = 0
    MsgSent = 0
})
// Build Morse Alphabet
function fnMorseAlphabet (inChar: string) {
    if (inChar == "A") {
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "B") {
        fnDash()
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "C") {
        fnDash()
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "D") {
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "E") {
        fnDot()
        fnPipe()
    } else if (inChar == "F") {
        fnDot()
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "G") {
        fnDash()
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "H") {
        fnDot()
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "I") {
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "J") {
        fnDot()
        fnDash()
        fnDash()
        fnDash()
        fnPipe()
    } else if (inChar == "K") {
        fnDash()
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "L") {
        fnDot()
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "M") {
        fnDash()
        fnDash()
        fnPipe()
    } else if (inChar == "N") {
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "O") {
        fnDash()
        fnDash()
        fnDash()
        fnPipe()
    } else if (inChar == "P") {
        fnDot()
        fnDash()
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "Q") {
        fnDash()
        fnDash()
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "R") {
        fnDot()
        fnDash()
        fnDot()
        fnPipe()
    } else if (inChar == "S") {
        fnDot()
        fnDot()
        fnDot()
        fnPipe()
    } else if (inChar == "T") {
        fnDash()
        fnPipe()
    } else if (inChar == "U") {
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "V") {
        fnDot()
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "W") {
        fnDot()
        fnDash()
        fnDash()
        fnPipe()
    } else if (inChar == "X") {
        fnDash()
        fnDot()
        fnDot()
        fnDash()
        fnPipe()
    } else if (inChar == "Y") {
        fnDash()
        fnDot()
        fnDash()
        fnDash()
        fnPipe()
    } else if (inChar == "Z") {
        fnDash()
        fnDash()
        fnDot()
        fnDot()
        fnPipe()
    }
}
// Display Pipe
function fnPipe () {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
// Send/Display Msg
input.onButtonPressed(Button.AB, function () {
    if (LastCharSet == 0) {
        inString = "" + inString + cArrayChar
        LastCharSet = 1
    }
    radio.sendString(inString)
    MsgSent = 1
})
// Receive Msg
radio.onReceivedString(function (receivedString) {
    iArrayLocation = 0
    durPause = 1000
    currChar = 0
    lenString = receivedString.length
    while (currChar < lenString) {
        fnMorseAlphabet(receivedString.charAt(currChar))
        currChar += 1
    }
})
// Append Letter to Msg
input.onButtonPressed(Button.B, function () {
    inString = "" + inString + cArrayChar
    iArrayLocation = 0
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    LastCharSet = 1
    MsgSent = 0
})
// Display Dash
function fnDash () {
    hummingbird.setLED(ThreePort.One, 100)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    hummingbird.setLED(ThreePort.One, 0)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
// Display Dot
function fnDot () {
    hummingbird.setLED(ThreePort.One, 100)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.pause(10)
    hummingbird.setLED(ThreePort.One, 0)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
let lenString = 0
let currChar = 0
let durPause = 0
let LastCharSet = 0
let cArrayChar = ""
let MsgSent = 0
let inString = ""
let iArrayLocation = 0
let text_list: string[] = []
radio.setGroup(138)
text_list = [
"A",
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
"_"
]
iArrayLocation = 0
inString = ""
MsgSent = 0
