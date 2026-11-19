library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tt_um_Rajesh_full_adder is
    port (
        ui_in   : in  std_logic_vector(7 downto 0);
        uo_out  : out std_logic_vector(7 downto 0);
        uio_in  : in  std_logic_vector(7 downto 0);
        uio_out : out std_logic_vector(7 downto 0);
        uio_oe  : out std_logic_vector(7 downto 0);
        ena     : in  std_logic;
        clk     : in  std_logic;
        rst_n   : in  std_logic
    );
end tt_um_Rajesh_full_adder;

architecture Behavioral of tt_um_Rajesh_full_adder is

  signal X : std_logic;

begin

    X <= ui_in(0) xor ui_in(1);

    uo_out(0) <= X xor ui_in(2);

    uo_out(1) <= (ui_in(0) and ui_in(1)) or
                 (ui_in(2) and X);

    uo_out(7 downto 2) <= (others => '0');

    uio_out <= (others => '0');
    uio_oe  <= (others => '0');

end Behavioral;
