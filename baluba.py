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
    def __init__ ( self, parametri ):
        self.parametri = parametri

class baluba:
    def __init__ ( self ):
        self.giocatori = {}
        self.convocati = []
        self.nparametri = 5
        self.nconvocati = 10
        self.formazioni = []
        pass

    def zeri ( self, s ):
        z = 0

        for i in xrange ( 0, self.nconvocati ):
            if ( not ( s & ( 1 << i ) ) ):
                z+=1
        return z

    def to_binany ( self, s ):
        binary = ''

        for i in xrange ( 0, self.nconvocati ):
            if ( s & ( 1 << self.nconvocati - 1 - i ) ):
                c = '1'
            else:
                c = '0'

            binary = binary + c
        return binary

    def is_on_team ( self, formazione, igiocatore, team ):
        bit = ( formazione >> ( self.nconvocati - 1 - igiocatore ) ) & 1
        return bit == team

    def stampa_formazione ( self, formazione ):
        for i in xrange ( 0, self.nconvocati ):
            if self.is_on_team ( formazione, i, 0 ):
                print self.convocati [ i ],
        print "vs",
        for i in xrange ( 0, self.nconvocati ):
            if self.is_on_team ( formazione, i, 1 ):
                print self.convocati [ i ],
        print

    def stampa_formazioni ( self ):
        for form in self.formazioni:
            print form,
            print "%04X" % ( form ),
            print self.to_binany ( form ),
            baluba.stampa_formazione ( form )

    def genera_formazioni ( self ):
        for s in xrange ( 0, 512 ):
            z = self.zeri ( s )
            if ( z == 5 ):
                self.formazioni.append ( s )

    def carica_giocatori ( self, filename ):
        f = open ( filename, "r" )
        lines = f.readlines ()
        f.close ()
        nline = 1
        for line in lines:
            line = line.strip ()
            if len ( line ) > 0:
                l = line.split ()
                if ( len ( l ) == self.nparametri + 1 ):
                    self.giocatori [ l [ 0 ] ] = giocatore ( l [ 1: ] )
                else:
                    print "Errore alla riga %d, riconosciuti %d parametri" % ( nline, len ( l ) - 1 )
            nline += 1

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
            print "%s: %s" % ( k, giocatore.parametri )

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
    print "caricati %d giocatori" % ( len ( baluba.giocatori ) )
    #baluba.stampa_giocatori ()
    print "caricati %d convocati" % ( len ( baluba.convocati ) )
    #baluba.stampa_convocati ()
    print "genero le formazioni"
    baluba.genera_formazioni ()
    #baluba.stampa_formazioni ()

