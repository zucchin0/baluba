#!/usr/bin/python

#struct giocatore
#{
#    int attacco;
#    int difesa;
#    int velocita;
#    int tecnica;
#    int portiere;
#};

class giocatore:
    def __init__ ( self, nome ):
        self.nome = nome

class baluba:
    def __init__ ( self ):
        pass

    def zeri ( self, s ):
        z = 0

        for i in xrange ( 0, 10 ):
            if ( not ( s & ( 1 << i ) ) ):
                z+=1
        return z

    def to_binany ( self, s ):
        binary = ''

        for i in xrange ( 0, 10 ):
            if ( s & ( 1 << 9 - i ) ):
                c = '1'
            else:
                c = '0'

            binary = binary + c
        return binary

    def print_furme ( self ):
        for s in xrange ( 0, 512 ):
            z = self.zeri ( s )
            if ( z == 5 ):
                print s,
                print "%04X" % ( s ),
                print self.to_binany ( s ),
                print

if __name__ == "__main__":
    print "balula"
    baluba = baluba ()
    baluba.print_furme ()

