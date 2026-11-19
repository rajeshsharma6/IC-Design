# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")
    # Test all 8 full-adder input combinations
    test_cases = [
        (0, 0),
        (4, 1),
        (2, 1),
        (6, 2),
        (1, 1),
        (5, 2),
        (3, 2),
        (7, 3)
    ]

    for inputs, expected_output in test_cases:
        dut.ui_in.value = inputs

        await ClockCycles(dut.clk, 1)

        assert int(dut.uo_out.value) == expected_output, \
            f"Input {inputs}: expected {expected_output}, got {int(dut.uo_out.value)}"
