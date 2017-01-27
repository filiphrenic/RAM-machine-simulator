# RAM-machine-simulator
Simulator for a simple RAM and Macro machine

Developed to check homework assignment for college course [Mathematical Logic and Computability](https://www.fer.unizg.hr/predmet/mli)

## Usage

`python simulator.py path/to/file`

> for examples run:

`python simulator.py examples/example*.ram`

## Registers

All registers (that aren't filled with input args) are initially _0_.

Final result should be found in `R0`.

## Input file

First line must contain input arguments, or be empty if it has none.

First argument is placed into `R1`, second into `R2`, ...

Every other line must be an operation.

Operations are indexed from _1_


## Operations

### RAM machine

* `INC x`   => increment value in `R[x]` by _1_
* `DEC x m` => decrement value in `R[x]` by _1_ if it's greater than _0_, otherwise go to instruction _m_
* `GOTO m`  => go to instruction _m_
* `STOP`    => stop simulator

### Macro machine

* all operations from _RAM machine_
* `ZERO x`   => set `R[x]` to _0_
* `MOVE x y` => set `R[y] = R[x]`
* `f(x,y,z,...)` => start _RAM function f_ using registers _x,y,z,..._ and write result to `R[0]`

These can be written entirely by using operations for the RAM machine

#### `ZERO x`
```
(m+0) DEC x (m+2)
(m+1) GOTO (m+0)
(m+2) _next operation_
```

#### `MOVE x y`
> Let z be some register that wasn't used up until now

```
(m+0) ZERO y
(m+1) ZERO z
(m+2) DEC x 6
(m+3) INC y
(m+4) INC z
(m+5) GOTO 2
(m+6) DEC z 9
(m+7) INC x
(m+8) GOTO 6
(m+9) ZERO z
```

#### `f(x,y,z,...)`

> Lets assume that _m_ is the biggest register index being used

```
Move registers [1,m] -> [m+1,2m]
Zero out registers [1,m]
Start RAM machine which calculates _f_
Move registers [m+1,2m] -> [1,m]
```

## TODO

Implement macros
