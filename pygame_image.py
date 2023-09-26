import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    img = pg.image.load("ex01/fig/3.png")
    img = pg.transform.flip(img,True,False)
    imgs = [img, pg.transform.rotozoom(img,10,1.0)]
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img,[1600-tmr,0])
        screen.blit(imgs[tmr%2], [300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()