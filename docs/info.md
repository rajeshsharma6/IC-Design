## How it works

This project implements a 1-bit full adder using VHDL and the Tiny Tapeout SKY130 template.

The full adder is a combinational digital circuit that adds three 1-bit inputs: A, B, and Cin (carry-in). It produces two outputs: Sum and Cout (carry-out).

The Boolean expressions are:

- Sum = A XOR B XOR Cin
- Cout = (A AND B) OR (Cin AND (A XOR B))

The design uses an intermediate XOR signal, X = A XOR B, which is shared between the Sum and Carry-out logic.

### Pin assignments

| Signal | Tiny Tapeout pin | Description |
|---|---|---|
| A | ui_in[0] | First input bit |
| B | ui_in[1] | Second input bit |
| Cin | ui_in[2] | Carry-in |
| Sum | uo_out[0] | Sum output |
| Cout | uo_out[1] | Carry-out |

The remaining dedicated output pins are held at logic 0. All bidirectional output drivers are disabled.

The circuit is combinational and does not require a clock for normal operation.

## How to test

The full adder can be verified by applying all eight possible combinations of its three input bits and comparing the outputs with the expected truth table.

| A | B | Cin | Sum | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

The project includes a Python testbench using Cocotb, located in `test/test.py`. The testbench applies each input combination, waits for the simulation to update, and checks the output using assertions.

The tests can be executed using the Tiny Tapeout simulation workflow.

## External hardware

No external hardware is required for simulation.

For physical hardware testing, the design can be used with a compatible Tiny Tapeout development board. Input signals can be supplied through the board's input pins, and the Sum and Carry-out signals can be observed through its output pins.
