# Specs

16 bit machine
64k memory - \$0000 -> \$FFFF
5 registers - A (8bits), B (8bits), D (16bits -> holds concatenated value of A and B), X(16bits), Y(16bits)

# Bytecodes and Mnemonics

## Basic Mnemonics

For loading data into registers, storing data in memory and ending execution.

|Mnemonic| Description| Example| What will this example do?|
|---|---|---|----|
|LDA<br>\$01|Assigns a value to our A register |LDA&nbsp;#\$2A| Assigns the hex value \$2A to the A register|
|LDX<br>\$02|Assigns a value to our X register |LDX&nbsp;#16000 |Assigns the number 16,000 to the X register|
|STA<br>\$03|Stores the value of the A register to a memory location|STA&nbsp;,X| Stores the value of the A register to the memory location pointed to by the X register|
|END<br>\$04|Terminates the B32 program |END&nbsp;START|Terminate the program and tell our assembler that execution of our program should start at the START label |

# File Format of executables

|Data| Length| Description|
|---|---|---|
|“DDL”| 3 Bytes |Our magic header number|
|&lt;Starting Address&gt; |2 Bytes |This is a 16-bit integer that tells our virtual machine where, in memory, to place our program.|
|&lt;Execution Address&gt; |2 Bytes |This is a 16-bit integer that tells our virtual machine where to begin execution of our program.|
|&lt;ByteCode&gt; |?? Bytes |This will be the start of our bytecode, which can be any length.|

# Assembler

Our assembler expects input in the format:

```
[Optional Label:]
<white space><mnemonic><white space><operand>[Optional white space]<newline>
```