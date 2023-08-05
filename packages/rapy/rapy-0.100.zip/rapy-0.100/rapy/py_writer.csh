#!/bin/csh

### *** pre-start ***
### power-on the I2C-to-CC (CSP) bridge
### try the CSP bridge
### try the CSP target (DUT)
### ===============================================================================
### python -mrapy.aardv sw
### python -mrapy.isp   rev
### python -mrapy.isp   d[ump]
### python -mrapy.csp   q[uery]
### python -mrapy.csp   rev
### python -mrapy.csp   d[ump]
### python -mrapy.csp 1 d[ump] b0 30
### python -mrapy.csp   stop
### python -mrapy.csp   nvm


### prepare the bin file for temporary
### ===============================================================================
#   set hexfile = ../cy2332r0_20180810/Objects/cy2332r0_20180810_016.hex
    set hexfile = ~/Desktop/project/can1112/cy2332r0_20180810/Objects/cy2332r0_20180810_016.hex
    ls $hexfile
    if ! -e $hexfile exit -1
    hex2bin.py $hexfile temp.bin


### stop MCU
### ===============================================================================
    python -mrapy.csp stop
    echo $status
exit

### ES may be not fully trimmed but OSC. Complete the row of CP trim
### ===============================================================================
### python -mrapy.csp prog_hex 1 940    ff 00 0a 00 00 ff
### python -mrapy.csp prog_hex 1 944 ff 4d 00 0a 00 00
### python -mrapy.csp prog_hex 1 94a    4d 00 0a 00 00 ff
    python -mrapy.csp trim


### upload FW
### ===============================================================================
    python -mrapy.csp upload temp.bin 1
### python -mrapy.csp upload ..\fw\cy2311r3\Objects\cy2311r3_20180606.2.memh 1
### python -mrapy.csp upload ..\fw\scp\phy20180605a_prl0605\scp\Objects\scp_20180613.2.memh 1


### compare
### ===============================================================================
    python -mrapy.csp comp   temp.bin \
                                       900=CAN1112A-000 \
                                       910=AP4377-14L \
                                       33=\90 34=\09 35=\40 36=\E4 37=\93 38=\F5 39=\A2 3A=\80 3B=\FE \
                                       940=\00 941=\FF 942=\FF 943=\FF 944=\FF


### FT information
### writer information
### option table
### PDO table
### mapping table
### ===============================================================================
### python -mrapy.csp prog_asc 1 910 CAN1112A28L_BIN1
    python -mrapy.csp prog_str 1 930 PY188_`date +%y%m%d%H%M`
    python -mrapy.csp prog_hex 1 960 02 08 00 00

### 2-PDO (5V/3A, 3.3-5.9V/3A, 15W)
    python -mrapy.csp   prog_hex 1 970 2C 91 01 0A  3C 21 76 C0

### 4-PDO (5V/3A, 9V/2A, 3.3-5.9V/3A, 3.3-11V/2A, 18W)
### python -mrapy.csp   prog_hex 1 970 2C 91 01 0A  C8 D0 02 00  3C 21 76 C0  28 21 DC C0
### python -mrapy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE        13 E8 C1 F4 21 F4 12 E4

### 2-PDO (5V/3A, 9V/3A, 27W)
### python -mrapy.csp   prog_hex 1 970 2C 91 01 0A  2C D1 02 00

### 3-PDO (5V/3A, 9V/3A, 3.3-11V/3A, 27/33W)
### python -mrapy.csp   prog_hex 1 970 2C 91 01 0A  2C D1 02 00  3C 21 DC C0
### python -mrapy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE 13 E8 C1 F4 11 F4 B2 E4
### python -mrapy.csp   prog_hex 1 a20    10 FA        51 C2     01 EE 13 E8 C1 F4 21 F4 12 E4

### 5-PDO (3.5V/3A, 5V/3A, 6V/3A, 7.3V/3A, 10V/2.2A, 22W)
### python -mrapy.csp   prog_hex 1 970 2C 19 01 0A  2C 91 01 00  2C E1 01 00  2C 49 02 00  DC 20 03 00
### python -mrapy.csp   prog_hex 1 a20    10 AF        50 FA        01 2C        11 6D        C1 F4     11 F4 62 E4

### python -mrapy.csp 1 prog_hex 1 98c 2C 19 01 0A  2C 91 01 00  2C E1 01 00  2C 49 02 00  DC 20 03 00
### python -mrapy.csp 1 prog_hex 1 98c 2C 91 01 0A  2C 91 01 00  3C 21 76 C0
### python -mrapy.csp 1 prog_hex 1 9a8 2C 91 01 0A  3C 21 76 C0


### fine-tune table
### ===============================================================================
    python -mrapy.csp   prog_hex 1 a58 80 20


### reset MCU
### ===============================================================================
### python -mrapy.csp write F7 01 01 01
### python -mrapy.csp reset

    rm temp.bin

