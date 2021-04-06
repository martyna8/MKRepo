def setup():
    size(400,400)
    textSize(70)
def draw():
    clear()
    background(204,204,204)
    fill(0,255,255)
    rect(50,50,50,150,50)
    
    ksztalt = createShape()
    ksztalt.beginShape()
    ksztalt.fill(255,255,255)
    ksztalt.vertex(100, height/4*2)
    ksztalt.vertex(150, height/2*2+30)
    ksztalt.vertex(width/2, height/3*2)
    ksztalt.vertex(width-150, height/3*2+20)
    ksztalt.vertex(width-100, height/5*2)
    ksztalt.endShape(CLOSE)
    shape(ksztalt, 55,-25)
    
    fill(0,255,0)
    text("MK",195,230)
    if hex(get(mouseX,mouseY)) == 'FF00FFFF':
        fill(255,0,255)
        text("MK",195,230) # żeby był w wybranym koleore trzeba napisać go ponownie, gdy aktywny jest ten kolor
    else:
        fill(0,0,0)
        text("MK",195,230)
        
    if keyPressed:
        if key == 'm' or key == 'k' or key == 'M' or key == 'K' :
            fill(255,0,255)
            text("MK",195,230)

#1,25pkt
