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
        self.giocatori = {}
        self.convocati = []
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

    def carica_giocatori ( self, filename ):
        f = open ( filename, "r" )
        lines = f.readlines ()
        f.close ()
        for line in lines:
            line = line.strip ()
            if len ( line ) > 0:
                self.giocatori [ line ] = giocatore ( line )

    def carica_convocati ( self, filename ):
        f = open ( filename, "r" )
        lines = f.readlines ()
        f.close ()
        for line in lines:
            line = line.strip ()
            if len ( line ) > 0:
                self.convocati.append ( line )

    def stampa_giocatori ( self ):
        for k, giocatore in self.giocatori.iteritems ():
            print "%s: %s" % ( k, giocatore.nome )

    def stampa_convocati ( self ):
        for convocato in self.convocati:
            print convocato

if __name__ == "__main__":
    print "+--------+"
    print "| baluba |"
    print "+--------+"
    baluba = baluba ()
    #baluba.print_furme ()
    baluba.carica_giocatori ( "giocatori.txt" )
    baluba.carica_convocati ( "convocati.txt" )
    #baluba.stampa_giocatori ()
    baluba.stampa_convocati ()

