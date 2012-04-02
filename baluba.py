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
    z = 0;

    for i in xrange ( 0, 10 ):
        if ( not ( s & ( 1 << i ) ) ):
            z+=1
    return z

if __name__ == "__main__":
    print "balula"

    for s in xrange ( 0, 512 ):
        z = zeri ( s )
        if ( z == 5 ):
            print s,
            #cout << " " << z << " " << 10 - z
            print

