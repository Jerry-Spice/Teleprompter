import time
import pygame
import sys

def run_teleprompter():
    f = open("WordFives.txt","r")
    data = f.read().split("\n")
    f.close


    root = pygame.display.set_mode((1000,750))

    background = pygame.Surface((1000,750))
    background.fill((0,0,0))

    pygame.font.init()



    def create_text_elements_for_prompter(sampleSize):
        fontSize = sampleSize
        if fontSize > 64 :
            fontSize = 64
        font = pygame.font.SysFont('timesnewroman',  fontSize)
        texts = []
        for i in range(len(data)):
            tempText = font.render(data[i], True, (255,255,255))
            texts.append(tempText)
        return texts

    def display_texts_for_prompter(texts, scrollage):
        for i in range(len(texts)):
            textRect = texts[i].get_rect()
            textRect.center = (500,i*70 + 300 + scrollage)
            root.blit(texts[i], textRect)
        
    def display_init_message(screen, fontSize):
        font = pygame.font.SysFont('timesnewroman',  fontSize)
        tempText = font.render("Font Size: "+str(fontSize)+" | Press 'Enter' When ready", True, (255,255,255))
        textRect = tempText.get_rect()
        textRect.center = (500,750/2)
        screen.blit(tempText, textRect)




    # scrollSpeedInput = float(input("Enter the desired scroll speed (Tip! Try between 0.2 and 0.1) >>"))
    # if scrollSpeedInput > 0:
    #     scrollSpeedInput *= -1
    scrollSpeed = 30
    scrollage = 0

    texts = []

    sampleSize = 30
    screen = 0

    while True:
        root.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quitted"
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    screen = 1
            elif event.type == pygame.MOUSEWHEEL:
                # print(event)
                # print(event.x, event.y)
                # print(event.flipped)
                # print(event.which)
                if screen == 0:
                    sampleSize+= event.y
                elif screen >= 1:
                    scrollage += event.y * scrollSpeed
        if screen == 0:
            display_init_message(root, sampleSize)
        elif screen == 1:
            texts = create_text_elements_for_prompter(sampleSize)
            screen = 2
        elif screen == 2:
            display_texts_for_prompter(texts, scrollage)
        


        pygame.display.update()
    