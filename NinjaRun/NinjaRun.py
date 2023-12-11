import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((1042,576))
clock = pygame.time.Clock()
bg= pygame.image.load('images/BG.png').convert()
bg= pygame.transform.scale(bg, size=(1042,576))
running = True
ninjaa = pygame.transform.scale(pygame.image.load('images/ninjarund.png').convert_alpha(), size= (75,75))
ninjad = pygame.transform.scale(pygame.image.load('images/ninjaruna.png').convert_alpha(), size= (75,75))
ninja_rect = ninjad.get_rect(center = (0,500))
ninja = ninjad
ninja_movementx = 500
images1=pygame.image.load('images/1.png')
images2=pygame.image.load('images/2.png')
images3=pygame.image.load('images/3.png')
images4=pygame.image.load('images/4.png')
suriken_surface1 = pygame.transform.scale2x(images1.convert_alpha())
suriken_surface2 = pygame.transform.scale2x(images2.convert_alpha())
suriken_surface3 = pygame.transform.scale2x(images3.convert_alpha())
suriken_surface4 = pygame.transform.scale2x(images4.convert_alpha())
suriken_list = []
suriken_list1 = []
suriken_list2 = []
suriken_list3 = []
suriken_list4 = []
def create_suriken1():
    surikenx = random.randint(50,1000)
    surikeny = random.randint(-450,0)
    suriken1 = suriken_surface1.get_rect(center = (surikenx,surikeny))
    suriken_list.append(suriken1)
    return suriken1
def create_suriken2():
    surikenx = random.randint(50,1000)
    surikeny = random.randint(-450,0)
    suriken2 = suriken_surface2.get_rect(center = (surikenx,surikeny)) 
    suriken_list.append(suriken2) 
    return suriken2
def create_suriken3():
    surikenx = random.randint(50,1000)
    surikeny = random.randint(-450,0)
    suriken3 = suriken_surface3.get_rect(center = (surikenx,surikeny)) 
    suriken_list.append(suriken3)  
    return suriken3
def create_suriken4():
    surikenx = random.randint(50,1000)
    surikeny = random.randint(-450,0)
    suriken4 = suriken_surface4.get_rect(center = (surikenx,surikeny)) 
    suriken_list.append(suriken4)
    return suriken4
def move_suriken(surikens):
    for suriken in surikens:
        suriken.centery += 5  
          
    return surikens
do1 = 0
do2 =0
do3 = 0
do4 = 0
def draw_suriken1(surikens,do1):
    for suriken in surikens:    
        suriken_surface1 = pygame.transform.rotate(images1,do1)
        suriken_surface1 = pygame.transform.scale2x(suriken_surface1.convert_alpha())
        screen.blit(suriken_surface1,suriken)
    return surikens
def draw_suriken2(surikens,do2):
    for suriken in surikens:  
        suriken_surface2 = pygame.transform.rotate(images2,do2)
        suriken_surface2 = pygame.transform.scale2x(suriken_surface2.convert_alpha())      
        screen.blit(suriken_surface2,suriken)
    return surikens
def draw_suriken3(surikens,do3):
    for suriken in surikens:  
        suriken_surface3 = pygame.transform.rotate(images3,do3)
        suriken_surface3 = pygame.transform.scale2x(suriken_surface3.convert_alpha())      
        screen.blit(suriken_surface3,suriken)
    return surikens
def draw_suriken4(surikens,do4):
    for suriken in surikens:   
        suriken_surface4 = pygame.transform.rotate(images4,do4)
        suriken_surface4 = pygame.transform.scale2x(suriken_surface4.convert_alpha())     
        screen.blit(suriken_surface4,suriken)
    return surikens
def check_collision(surikens):
    for suriken in surikens:
        if ninja_rect.colliderect(suriken):            
            return False
    return True
spawnsuriken = pygame.USEREVENT
pygame.time.set_timer(spawnsuriken,1500)
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ninja = ninjad
        ninja_movementx -= 10
    if keys[pygame.K_RIGHT]:
        ninja = ninjaa
        ninja_movementx += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawnsuriken:
            suriken_list1.append(create_suriken1())
            suriken_list2.append(create_suriken2())
            suriken_list3.append(create_suriken3())
            suriken_list4.append(create_suriken4())
    screen.blit(bg,(0,0))
    ninja_rect.centerx = ninja_movementx
    ninja_rect.centery = 500
    suriken_list1 = move_suriken(suriken_list1)
    suriken_list2 = move_suriken(suriken_list2)
    suriken_list3 = move_suriken(suriken_list3)
    suriken_list4 = move_suriken(suriken_list4)
    do1+=5
    do2-=6
    do3+=7
    do4-=4
    draw_suriken1(suriken_list1,do1)
    draw_suriken2(suriken_list2,do2)
    draw_suriken3(suriken_list3,do3)
    draw_suriken4(suriken_list4,do4)
    running = check_collision(suriken_list)      
    screen.blit(ninja,ninja_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()