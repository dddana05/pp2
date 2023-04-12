import pygame
pygame.init()
songs={
  "txt-tinnitus.mp3":"txtt.jpg",
  "SEVENTEEN Left & Right.mp3":"svt2.jpg"
}
screen=pygame.display.set_mode((600,600))
t=0
pz=False
while True:
     pygame.display.update()
     
     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            r=False
            pygame.quit()
        elif i.type==pygame.KEYDOWN:
           if i.key==pygame.K_SPACE:
             pz=not pz
             if pz:
                 pygame.mixer.music.pause()
             else:
              pygame.mixer.music.unpause()
           if i.key==pygame.K_RIGHT:
              if t==len(list(songs.keys()))-1:
               t=0
              else:  t+=1
           if i.key==pygame.K_LEFT:
             if t==0:
               t=len(list(songs.keys()))-1
             else: t-=1
           pygame.mixer.music.load(list(songs.keys())[t])
           pygame.mixer.music.play(-1)
          
    
           
           screen.blit(pygame.image.load(list(songs.values())[t]),(0,0))