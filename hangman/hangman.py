import pygame
import math
import random
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

RADIUS = 20
GAP = 15
letters = [] 
# The formula used to calculate the starting position and space between circles which numbers had been put in -> (Width - (radius * 2 + gap) * 13) / 2 While we have got 2 separate rows and 13 buttons in each row
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65 #Letter A is equal to number 65 on our keyboard and as it goes on and we add 1 we would get the next letters alphabetically. chr() represents this relationship between letters and numbers 
for i in range(26):#what button we are on 
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)) #explaining two rows and the gap from edges
    y = starty + ((i // 13) * (GAP + RADIUS * 2)) # // removes remainders
    letters.append([x,y,chr(A + i),True])
    
#for writing numbers in circles we need fonts
font = pygame.font.SysFont('comicsans', 30)
wordFont = pygame.font.SysFont('comicsans', 50)
titleFont = pygame.font.SysFont('comicsans', 70)
    
    
pics = []
hangManStatus = 0 #Which pic is about to pop up
words = ["PYTHON","PROGRAMMER","WEB","IDE","PYGAME"]
word = random.choice(words)
guessed = []
for x in range(7):
    image = pygame.image.load("hangman" + str(x) + ".png")
    pics.append(image)


WHITE = (255,255,255) 
BLACK = (0,0,0)
FPS = 70 
clock = pygame.time.Clock()

def draw():
    window.fill(WHITE)
    text = titleFont.render("DEVELOPER HANGMAN", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    
    displayedWord = ""
    for letter in word:
        if letter in guessed:
            displayedWord += letter + " "
        else:
            displayedWord += "_ "
    text = wordFont.render(displayedWord, 1, BLACK)        
    window.blit(text, (350,200))        
    for letter in letters:
        x, y, fontLetter, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 2)
            text = font.render(fontLetter, 1, BLACK)
            window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    window.blit(pics[hangManStatus], (150,100))
    pygame.display.update()

def displayMessage(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = wordFont.render(message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    

run = True
while run:
    clock.tick(FPS)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, fontLetter, visible = letter
                if visible:
                    distance = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(fontLetter)
                        if fontLetter not in word:
                            hangManStatus += 1                  
    draw()                        
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        displayMessage("You WON!")
        break
    if hangManStatus == 6:
        displayMessage("You LOST!")
        break            
pygame.quit()