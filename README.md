# RAM-machine-simulator
Simulator for a simple RAM machine code

Developed to check homework assignment for college course [Mathematical Logic and Computability](https://www.fer.unizg.hr/predmet/mli)

### Operations

* `INC x`   => increment value in register x by 1
* `DEC x m` => decrement value in register x by 1 if it's greater than 0, otherwise go to instruction m
* `GOTO m`  => go to instruction m
* `STOP`    => stop simulator

Commands are indexed from _1_

### Registers

All registers (that aren't filled with input args) are initially _0_.

Final result should be found in `R0`.

### Input file

First line must contain input arguments, or be empty if it has none.

First argument is placed into `R1`, second into `R2`, ...

Every other line must be an operation.
