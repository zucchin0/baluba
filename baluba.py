#!/usr/bin/python

#struct giocatore
#{
#    int attacco;
#    int difesa;
#    int velocita;
#    int tecnica;
#    int portiere;
#};

def zeri ( s ):
    z = 0

    for i in xrange ( 0, 10 ):
        if ( not ( s & ( 1 << i ) ) ):
            z+=1
    return z

def to_binany ( s ):
    binary = ''

    for i in xrange ( 0, 10 ):
        if ( s & ( 1 << 9 - i ) ):
            c = '1'
        else:
            c = '0'

        binary = binary + c
    return binary

if __name__ == "__main__":
    print "balula"

    for s in xrange ( 0, 512 ):
        z = zeri ( s )
        if ( z == 5 ):
            print s,
            print "%04X" % ( s ),
            print to_binany ( s ),
            print

