
TRUE  = 1 # ACK, YES
FALSE = 0 # NAK, NO

class i2c:
    '''
    i2c class hierarchy
    -------------------

               ftdi_i2c
             /
         i2c
             \
               aardvark_i2c
             / (aardv.py)
    aardvark
    
    '''
    def enum (me): raise NotImplementedError()
    def baud (me, ask): raise NotImplementedError()
    def i2cw (me, wdat): raise NotImplementedError()
    def read (me, dev, adr, rcnt, rpt=FALSE): raise NotImplementedError()

    def write (me, dev, adr, wdat): # SMB write
        return me.i2cw ([dev,adr]+wdat)

    def probe (me):
        print 'Searching I2C slave.....'
        hit = []
        for dev in range(0x80):
            if me.i2cw ([dev]):
                print 'device 0x%02x found' % (dev)
                hit += [dev]
        return hit



CHOOSE_FTDI_FIRST = 1
CHOOSE_AARDVARK_FIRST = 2

def choose_i2cmst (order=CHOOSE_FTDI_FIRST, rpt=TRUE):
    from rapy.ftdi_i2c import ftdi_i2c
    from cynpy.aardv   import aardvark_i2c
    i2cmst = 0
    if order == CHOOSE_FTDI_FIRST:
        if ftdi_i2c().enum (rpt) > 0:
            i2cmst = ftdi_i2c(0)
        if not i2cmst and \
           aardvark_i2c().enum (rpt) > 0:
            i2cmst = aardvark_i2c(0)
    elif order == CHOOSE_AARDVARK_FIRST:
        if aardvark_i2c().enum (rpt) > 0:
            i2cmst = aardvark_i2c(0)
        if not i2cmst and \
           ftdi_i2c().enum (rpt) > 0:
            i2cmst = ftdi_i2c(0)

    return i2cmst



if __name__ == '__main__':

    i2cmst = choose_i2cmst ()

    from cynpy.basic import *
    if not no_argument ():
        if i2cmst!=0:
            if   sys.argv[1]=='probe' : print i2cmst.probe ()
            elif sys.argv[1]=='baud'  : print i2cmst.baud (argv_dec[2])
            elif sys.argv[1]=='write' : print i2cmst.i2cw (argv_hex[2:])
            elif sys.argv[1]=='rdx'   : print ['0x%02X' % xx for xx in i2cmst.i2crdx (argv_hex[2], argv_hex[3], argv_hex[4], FALSE)] # FTDI-only
            elif sys.argv[1]=='rdi'   : print ['0x%02X' % xx for xx in i2cmst.i2crdx (argv_hex[2], argv_hex[3], argv_hex[4])] # FTDI-only
            elif sys.argv[1]=='read'  : print ['0x%02X' % xx for xx in i2cmst.read   (argv_hex[2], argv_hex[3], argv_hex[4])]
            else: print "command not recognized"
        else: print "I2C master not found"
