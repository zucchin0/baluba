#!/usr/bin/python

import sys

#struct giocatore
#{
#    int attacco;
#    int difesa;
#    int velocita;
#    int tecnica;
#    int portiere;
#};

class Configs ( object ):
    nconvocati = 10
    nparametri = 5
    metodo = 'base'
    
class giocatore ( object ):
    def __init__ ( self, parametri ):
        self.parametri = [ eval ( par ) for par in parametri ]

class vincolo ( object ):
    def __init__ ( self, tipo, parametri ):
        self.tipo = tipo
        self.parametri = parametri

class formazione ( object ):
    def __init__ ( self, valore ):
        self.valore = valore
        self.valutazione = sys.maxint

    def __valutazione__ ( self ):
        return self.valutazione 

    def zeri ( self ):
        z = 0
        for i in xrange ( 0, Configs.nconvocati ):
            if ( not ( self.valore & ( 1 << i ) ) ):
                z += 1
        return z

    def to_binany ( self ):
        binary = ''
        for i in xrange ( 0, Configs.nconvocati ):
            if ( self.valore & ( 1 << Configs.nconvocati - 1 - i ) ):
                c = '1'
            else:
                c = '0'
            binary = binary + c
        return binary

    def is_on_team ( self, igiocatore ):
        return ( self.valore >> ( Configs.nconvocati - 1 - igiocatore ) ) & 1

    def squadra ( self, squadra ):
        s = []
        for i in xrange ( 0, Configs.nconvocati ):
            if self.is_on_team ( i ) == squadra:
                s.append ( i )
        return s

class baluba ( object ):
    def __init__ ( self ):
        self.giocatori = {}
        self.convocati = []
        self.formazioni = []
        self.vincoli = []
        pass

    def stampa_formazioni ( self ):
        for form in self.formazioni:
            print form.valore,
            print "%04X" % ( form.valore ),
            print form.to_binany ( ),
            for i in form.squadra ( 0 ):
                print self.convocati [ i ],
            print "vs",
            for i in form.squadra ( 1 ):
                print self.convocati [ i ],
            print form.valutazione,
            print

    def genera_formazioni ( self ):
        for val in xrange ( 0, ( 2 ** Configs.nconvocati ) / 2 ):
            f = formazione ( val )
            z = f.zeri ( )
            if ( z == Configs.nconvocati / 2 ):
                self.formazioni.append ( f )

    def carica_giocatori ( self, filename ):
        f = open ( filename, "r" )
        lines = f.readlines ()
        f.close ()
        nline = 1
        for line in lines:
            line = line.strip ()
            if len ( line ) > 0:
                l = line.split ()
                if ( len ( l ) == Configs.nparametri + 1 ):
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

    def carica_vincoli ( self, filename ):
        f = open ( filename, "r" )
        lines = f.readlines ()
        f.close ()
        for line in lines:
            line = line.strip ()
            if len ( line ) > 0:
                l = line.split ()
                self.vincoli.append ( vincolo ( l [ 0 ], l [ 1: ] ) )

    def stampa_vincoli ( self ):
        for vincolo in self.vincoli:
            print vincolo.valore

    def stampa_giocatori ( self ):
        for k, giocatore in self.giocatori.iteritems ():
            print "%s: %s" % ( k, giocatore.parametri )

    def stampa_convocati ( self ):
        for convocato in self.convocati:
            print convocato

    def valuta_formazioni ( self ):
        for form in self.formazioni:
            if Configs.metodo == 'base':
                sq0 = [ 0 for i in xrange ( 0, Configs.nparametri ) ]
                sq1 = [ 0 for i in xrange ( 0, Configs.nparametri ) ]
                for igiocatore in form.squadra ( 0 ):
                    g = self.giocatori [ self.convocati [ igiocatore ] ]
                    for par in xrange ( 0, Configs.nparametri ):
                        sq0 [ par ] += g.parametri [ par ]
                for igiocatore in form.squadra ( 1 ):
                    g = self.giocatori [ self.convocati [ igiocatore ] ]
                    for par in xrange ( 0, Configs.nparametri ):
                        sq1 [ par ] += g.parametri [ par ]
                val_sq0 = 0
                val_sq1 = 0
                for val in sq0:
                    val_sq0 += val
                for val in sq1:
                    val_sq1 += val
                form.valutazione = val_sq0 - val_sq1
                if form.valutazione < 0:
                    form.valutazione = -form.valutazione
            else:
                print "Metodo di valutazione '%s' sconosciuto" % ( Configs.metodo )
                break

    def ordina_formazioni ( self ):
        self.formazioni.sort ( key = formazione.__valutazione__ )

    def applica_vincoli ( self ):
        f = []
        for form in self.formazioni:
            for vincolo in self.vincoli:
                r = True
                if vincolo.tipo == 'vs':
                    g1 = self.convocati.index ( vincolo.parametri [ 0 ] )
                    g2 = self.convocati.index ( vincolo.parametri [ 1 ] )
                    r = form.is_on_team ( g1 ) != form.is_on_team ( g2 )
                elif vincolo.tipo == 'w':
                    g1 = self.convocati.index ( vincolo.parametri [ 0 ] )
                    g2 = self.convocati.index ( vincolo.parametri [ 1 ] )
                    r = form.is_on_team ( g1 ) == form.is_on_team ( g2 )
                if not r:
                    break
            else:
                f.append ( form )
        self.formazioni = f

if __name__ == "__main__":
    print "+--------+"
    print "| baluba |"
    print "+--------+"
    baluba = baluba ()
    baluba.carica_giocatori ( "giocatori.txt" )
    baluba.carica_convocati ( "convocati.txt" )
    baluba.carica_vincoli ( "vincoli.txt" )
    print "caricati %d giocatori" % ( len ( baluba.giocatori ) )
    #baluba.stampa_giocatori ()
    print "caricati %d convocati" % ( len ( baluba.convocati ) )
    #baluba.stampa_convocati ()
    print "caricati %d vincoli" % ( len ( baluba.vincoli ) )
    #baluba.stampa_vincoli ()
    print "genero le formazioni"
    baluba.genera_formazioni ()
    print "applico i vincoli"
    baluba.applica_vincoli ()
    print "valuto le formazioni"
    baluba.valuta_formazioni ()
    print "ordino le formazioni"
    baluba.ordina_formazioni ()
    print "stampo le formazioni"
    baluba.stampa_formazioni ()

