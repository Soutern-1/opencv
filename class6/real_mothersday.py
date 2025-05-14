import pygame

pygame.init()

import time

display = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("My dearest mom!")


font1 = pygame.font.SysFont("Times New Roman",30)


photo = pygame.image.load("images/photo.jpeg")
selfie = pygame.image.load("images/selfie.jpeg")
parthenon = pygame.image.load("images/flight.jpeg")
flight = pygame.image.load("images/parthenon.jpeg")
introduction = pygame.image.load("images/introduction.jpeg")

 
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

# --------------
    display.fill('BLACK')
    
    text = font1.render("To my dearest mother....",True,(0,0,255))

    display.blit(photo,(0,0))
    display.blit(text,(30,30))

    pygame.display.update()
    time.sleep(2)


# --------------
    display.fill('BLACK')

    text = font1.render("Thank you for everything no matter where we go...",True,(255,0,0))


    display.blit(flight,(0,0))
    display.blit(text,(30,30))


    pygame.display.update()
    time.sleep(2)

    display.fill('BLACK')


# --------------

    text = font1.render("Even while traveling in Greece or just at home",True,(0,255,0))

    display.blit(parthenon,(180,90))
    display.blit(text,(30,30))


    pygame.display.update()
    time.sleep(2)

    display.fill('BLACK')

# --------------


    text = font1.render("You will always be my mom!!",True,(0,255,0))

    display.blit(selfie,(0,0))
    display.blit(text,(30,30))


    pygame.display.update()
    time.sleep(2)

    display.fill('BLACK')

# --------------




    text = font1.render("Happy Mother's Day!",True,(0,255,0))

    display.blit(introduction,(400,400))
    display.blit(text,(30,30))


    pygame.display.update()
    time.sleep(2)

# --------------