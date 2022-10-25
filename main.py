from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)
  
    def setup():
        p.createCanvas(700, 410)
        p.background(255)
        p.rectMode(p.CENTER)
        # die >fill< Methode gibt an ,welche fabe fortan zum zeichen verwendet wirt .
      # Als parameter werden RGB-werte übergeben oder 1 Parameter für den garton
        #RGB-WERTE sind auf >farb-tabelle.de< zu finden.
        p.fill(70, 700, 500)
        p.circle(300,150,300);

        p.fill(328, 35, 8)
        p.circle(300,150,200);

        p.fill(311, 42, 93)
        p.circle(300,150,150);

        p.fill(548, 74, 327)
        p.circle(300,150,50);

        p.fill(437, 378,67)
        p.rect(39,43,97,67)
      
    p.setup = setup    

myp5 = window.p5.new(sketch)