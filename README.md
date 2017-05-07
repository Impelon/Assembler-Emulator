# Assembler-Emulator
An Emulator for a simplified assembly language.

Currently a very simple prototype using Python. Sourcecode is written in German. 

The assembler (`main.py`) loads up a program written in a file `input.txt` and outputs the result in `output.txt` in the same folder.
It currently supports a language following this format: 
`(line number) (command|number)`, e.g. 
```
00 lda 4
01 add 5
02 sta 6
03 stp
04 1
05 3
```

This is a list of the supported commands and their effects on the components:
```
LDA #x    accumulator := x
LDA x     accumulator := RAM[x]
LDA (x)   accumulator := RAM[RAM[x]]

STA x     RAM[x] := accumulator
STA (x)   RAM[RAM[x]] := accumulator

ADD x     accumulator := accumulator + RAM[x]
SUB x     accumulator := accumulator - RAM[x]
MUL x     accumulator := accumulator * RAM[x]
DIV x     accumulator := accumulator / RAM[x]

JMP x     PC := x
JMP (x)   PC := RAM[x]

JNZ x     PC := x, if accumulator is not 0
JNZ (x)   PC := RAM[x], if accumulator is not 0

JZE x     PC := x, if accumulator = 0
JZE (x)   PC := RAM[x], if accumulator = 0

JLE x     PC := x, if accumulator <= 0
JLE (x)   PC := RAM[x], if accumulator <= 0

STP       end program
```
