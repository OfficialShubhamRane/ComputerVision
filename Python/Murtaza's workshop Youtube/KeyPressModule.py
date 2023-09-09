import pygame

def init():
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(keyName):
    res = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        res = True
    pygame.display.update()
    return res

def main():
    if getKey("w"):
        print("forward key pressed (W)")
    if getKey("a"):
        print("forward key pressed (A)")
    if getKey("s"):
        print("forward key pressed (S)")
    if getKey("d"):
        print("forward key pressed (D)")


if __name__ == "__main__":
    init()
    while True :
        main()

