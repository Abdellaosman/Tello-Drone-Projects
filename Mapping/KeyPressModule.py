import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))  # Create a window for capturing events

def getKey(keyName):
    ans = False
    for event in pygame.event.get(): pass  # Clear events to avoid build-up
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left Key Pressed")
    if getKey("RIGHT"):
        print("Right Key Pressed")

if __name__ == '__main__':
    init()
    while True:
        main()
