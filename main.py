import pygame

display = pygame.display.set_mode((300, 300))
pygame.init()
onclick = False


def drawcircle(pos):
    pygame.draw.circle(display, (255, 255, 0), (pos[0], pos[1]), 45, 8)


def drawX(pos):
    pygame.draw.line(display, (255, 0, 255), (pos[0] - 45, pos[1] - 45), (pos[0] + 45, pos[1] + 45))
    pygame.draw.line(display, (255, 0, 255), (pos[0] + 45, pos[1] - 45), (pos[0] - 45, pos[1] + 45))


def whereisclick(click):
    for x in range(0, 400, 100):
        for y in range(0, 400, 100):
            if x < click[0] < x + 100 and y < click[1] < y + 100:
                wheredraw = [x, y]
                return wheredraw


def drawboard():
    for linex in range(100, 300, 100):
        pygame.draw.line(display, (255, 255, 255), (linex, 0), (linex, 300))
    for liney in range(100, 300, 100):
        pygame.draw.line(display, (255, 255, 255), (0, liney), (300, liney))


kolej = "X"
pols = [[[0, 0, "1"], [0, 100, "2"], [0, 200, "3"]], [[100, 0, "4"], [100, 100, "5"], [100, 200, "6"]],
        [[200, 0, "7"], [200, 100, "8"], [200, 200, "9"]]]


def checkwin():
    # pion
    if pols[0][0][2] == pols[0][1][2] == pols[0][2][2]:
        print("win: " + str(pols[0][2][2]))
        pygame.draw.line(display, (255, 0, 0), (pols[0][0][0] + 50, pols[0][0][1]),
                         (pols[0][2][0] + 50, pols[0][2][1] + 100), 8)
    if pols[1][0][2] == pols[1][1][2] == pols[1][2][2]:
        print("win: " + str(pols[1][2][2]))
    if pols[2][0][2] == pols[2][1][2] == pols[2][2][2]:
        print("win: " + str(pols[2][2][2]))
    # poziom
    if pols[0][0][2] == pols[1][0][2] == pols[2][0][2]:
        print("win: " + str(pols[2][0][2]))
    if pols[0][1][2] == pols[1][1][2] == pols[2][1][2]:
        print("win: " + str(pols[2][1][2]))
    if pols[0][2][2] == pols[1][2][2] == pols[2][2][2]:
        print("win: " + str(pols[2][2][2]))
    # skos
    if pols[0][0][2] == pols[1][1][2] == pols[2][2][2]:
        print("win: " + str(pols[2][2][2]))
    if pols[0][2][2] == pols[1][1][2] == pols[2][0][2]:
        print("win: " + str(pols[2][0][2]))


def draw(click):
    global kolej
    for x in pols:
        for y in x:
            if y[2] != "0" and y[2] != "X" and y[0] == whereisclick(click)[0] and y[1] == whereisclick(click)[1]:
                if kolej == "O":
                    y[2] = "O"
                    kolej = "X"
                else:
                    y[2] = "X"
                    kolej = "O"


def redraw():
    global rond
    drawboard()
    for x in pols:
        for y in x:
            if y[2] == "O":
                pos = [y[0] + 50, y[1] + 50]
                drawcircle(pos)
            if y[2] == "X":
                pos = [y[0] + 50, y[1] + 50]
                drawX(pos)
            else:
                pass
    pygame.display.update()


print(pols)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            draw(click)
    redraw()
    checkwin()
