
rem *** pre-start ***
rem power-on the I2C-to-CC (CSP) bridge
rem try the CSP bridge
rem try the CSP target (DUT)
rem ===============================================================================
rem python -mcynpy.aardv sw
rem python -mcynpy.isp   rev
rem python -mcynpy.isp   dump
rem python -mcynpy.csp   query
rem python -mcynpy.csp   rev
rem python -mcynpy.csp   dump
rem python -mcynpy.csp 1 dump b0 30
rem python -mcynpy.csp   stop
rem python -mcynpy.csp   nvm
rem python -mcynpy.csp   dnload otp.bin


rem prepare the bin file for temporary
rem ===============================================================================
rem python -B c:\Python27\Scripts\hex2bin.py ..\fw\cy2311r3\Objects\cy2311r3_x004.hex temp.bin
    python -B c:\Python27\Scripts\hex2bin.py z:\RD\Project\CAN1112\Ray\fw\cy2332r0_20180810_016.hex temp.bin


rem stop MCU
rem ===============================================================================
    python -mcynpy.csp stop


rem ES may be not fully trimmed but OSC. Complete the row of CP trim
rem ===============================================================================
rem python -mcynpy.csp prog_hex 1 940    ff 00 0a 00 00 ff
rem python -mcynpy.csp prog_hex 1 944 ff 4d 00 0a 00 00
rem python -mcynpy.csp prog_hex 1 94a    4d 00 0a 00 00 ff
    python -mcynpy.csp set_trim

rem upload FW
rem ===============================================================================
    python -mcynpy.csp upload temp.bin 1
rem python -mcynpy.csp upload ..\fw\cy2311r3\Objects\cy2311r3_20180606.2.memh 1
rem python -mcynpy.csp upload ..\fw\scp\phy20180605a_prl0605\scp\Objects\scp_20180613.2.memh 1


rem compare
rem ===============================================================================
    python -mcynpy.csp   comp temp.bin ^
                                       900=CAN1112A-000 ^
                                       910=AP4377-14L ^
                                       33=\90 34=\09 35=\40 36=\E4 37=\93 38=\F5 39=\A2 3A=\80 3B=\FE ^
                                       940=\00 941=\FF 942=\FF 943=\FF 944=\FF


rem FT information
rem writer information
rem option table
rem PDO table
rem mapping table
rem ===============================================================================
rem python -mcynpy.csp prog_asc 1 910 CAN1112A28L_BIN1
    python -mcynpy.csp prog_str 1 930 PY187_%DATE:~2,2%%DATE:~5,2%%DATE:~8,2%%TIME:~0,2%%TIME:~3,2%
rem python -mcynpy.csp prog_hex 1 960 02 08 00 00
rem python -mcynpy.csp prog_hex 1 960 06 08 08 00
    python -mcynpy.csp prog_hex 1 960 06 28 08 00

rem 2-PDO (5V/3A, 3.3-5.9V/3A, 15W/17.7W)
rem python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  3C 21 76 C0

rem 3-PDO (5V/3A, 9V/3A, 3.3-11V/3A, 27/33W)
rem python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  2C D1 02 00  3C 21 DC C0
rem python -mcynpy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE 13 E8 C1 F4 11 F4 B2 E4
rem python -mcynpy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE 13 E8 C1 F4 21 F4 12 E4

rem 4-PDO (5V/3A, 9V/2A, 3.3-5.9V/3A, 3.3-11V/2A, 18W/22W)
    python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  C8 D0 02 00  3C 21 76 C0  28 21 DC C0
rem python -mcynpy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE        13 E8 C1 F4 11 F4 22 E4
    python -mcynpy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE        13 E8 C1 F4 11 F4 62 E4

rem 6-PDO (5V/3A, 6V/3A, 7V/3A, 8V/2.75A, 9V/2.44A, 10V/2.2A, 22W)
rem python -mcynpy.csp   prog_hex 1 970 2C 91 01 0A  2C E1 01 00  2C 31 02 00  13 81 02 00  F4 D0 02 00  DC 20 03 00
rem python -mcynpy.csp   prog_hex 1 a20    10 FA        51 2C        01 5E        11 90        C1 C2        11 F4 62 E4


rem 3-PDO (5V/3A, 9V/2A, 3.3-21V/2A, ??W)
rem python -mcynpy.csp 1 prog_hex 1 98C 2C 91 01 0A  C8 D0 02 00  28 21 A4 C1



rem fine-tune table
rem ===============================================================================
rem python -mcynpy.csp   prog_hex 1 a58 80 20
    python -mcynpy.csp   prog_hex 1 a58 80 60


rem reset MCU
rem ===============================================================================
rem python -mcynpy.csp wrx F7 01 01 01
rem python -mcynpy.csp reset

    del temp.bin
