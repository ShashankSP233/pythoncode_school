from random import randint
import pygame
from sys import exit  

def dis_score():
    cur_time=pygame.time.get_ticks()-str_time
    score_surf= test_font.render(str(cur_time//1000),False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return cur_time

def obs_move(obs_lis):
    if obs_lis:
        for obs_rect in obs_lis:
            obs_rect.x -=5
            if obs_rect.bottom == 301:      
                screen.blit(slime_sur,obs_rect)
            else:
                screen.blit(fly_sur,obs_rect)
                
        obs_lis=[obs for obs in obs_lis if obs.x >(-100)]    
        
        return obs_lis
    else:
        return []
            
def col_dect(player,obstacle):
    if obstacle:
        for obs_rect in obstacle:
            if player.colliderect(obs_rect):
                return(False)
    return True
def play_animation():
    global ply_index, ply_sur
    #display walk when on floor 
    if ply_rect.bottom< 300:
        ply_sur = ply_jump
    else:
        ply_index +=0.29
        if ply_index>=len(ply_walk):
            ply_index=0
        ply_sur= ply_walk[int(ply_index)]
       

#player selection
ply1_sur = pygame.image.load(r"platformerGraphicsDeluxe_Updated\Player\p1_stand.png")

ply2_sur = pygame.image.load(r"platformerGraphicsDeluxe_Updated\Player\p2_stand.png")
ply3_sur = pygame.image.load(r"platformerGraphicsDeluxe_Updated\Player\p3_stand.png")

ask_play= str(input('plese select player:'))
if ask_play == '1':
    ply_sur1= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk01.png")
    ply_sur2= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk02.png")
    ply_sur3= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk03.png")
    ply_sur4= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk04.png")
    ply_sur5= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk05.png")
    ply_sur6= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk06.png")
    ply_sur7= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk07.png")
    ply_sur8= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk08.png")
    ply_sur9= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk09.png")
    ply_sur10= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk10.png")
    ply_sur11= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_walk\PNG\p1_walk11.png")
    
    ply_jump=pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p1_jump.png")
elif ask_play == '2':
    ply_sur1= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk01.png")
    ply_sur2= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk02.png")
    ply_sur3= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk03.png")
    ply_sur4= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk04.png")
    ply_sur5= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk05.png")
    ply_sur6= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk06.png")
    ply_sur7= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk07.png")
    ply_sur8= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk08.png")
    ply_sur9= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk09.png")
    ply_sur10= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk10.png")
    ply_sur11= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_walk\PNG\p2_walk11.png")
    
    ply_jump=pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p2_jump.png")

elif ask_play == '3':    
    ply_sur1= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk01.png")
    ply_sur2= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk02.png")
    ply_sur3= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk03.png")
    ply_sur4= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk04.png")
    ply_sur5= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk05.png")
    ply_sur6= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk06.png")
    ply_sur7= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk07.png")
    ply_sur8= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk08.png")
    ply_sur9= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk09.png")
    ply_sur10= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk10.png")
    ply_sur11= pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_walk\PNG\p3_walk11.png")
    
    ply_jump=pygame.image.load(r"E:\py code\platformerGraphicsDeluxe_Updated\Player\p3_jump.png")
    



#screen

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('g@Me$')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()

grd_surface = pygame.image.load('graphics/ground.png').convert()


# obs

slime_frm1 = pygame.image.load("E:\py code\platformerGraphicsDeluxe_Updated\Enemies\slimeWalk1.png").convert_alpha()
slime_frm2 = pygame.image.load("E:\py code\platformerGraphicsDeluxe_Updated\Enemies\slimeWalk2.png").convert_alpha()
slime_idx=0
slime_frame=[slime_frm1,slime_frm2]
slime_sur = slime_frame[slime_idx]

fly_sur1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_sur2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fl_idx=0
fl_frame = [fly_sur1,fly_sur2]
fly_sur=fl_frame[fl_idx]


#obs timer
obs_timer= pygame.USEREVENT + 1
pygame.time.set_timer(obs_timer,1500)

slime_timer= pygame.USEREVENT + 2
pygame.time.set_timer(slime_timer,300)

fly_timer= pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer,100)

#player surface 
ply_sur1=ply_sur1.convert_alpha()
ply_sur2=ply_sur2.convert_alpha()
ply_sur3=ply_sur3.convert_alpha()
ply_sur4=ply_sur4.convert_alpha()
ply_sur5=ply_sur5.convert_alpha()
ply_sur6=ply_sur6.convert_alpha()
ply_sur7=ply_sur7.convert_alpha()
ply_sur8=ply_sur8.convert_alpha()
ply_sur9=ply_sur9.convert_alpha()
ply_sur10=ply_sur10.convert_alpha()

ply_walk = [ply_sur1,ply_sur2,ply_sur3,ply_sur4,ply_sur5,ply_sur6,ply_sur7,ply_sur8,ply_sur9,ply_sur10]
ply_index=0
ply_sur=ply_walk[int(ply_index)]
ply_rect = ply_sur.get_rect(midbottom=(50, 300))



#inttro screen

ply1_sur=ply1_sur.convert_alpha()
ply1_stand = pygame.transform.rotozoom(ply1_sur,0,3)
ply1_rect = ply1_sur.get_rect(midbottom=(200, 300))

ply2_sur=ply2_sur.convert_alpha()
ply2_stand = pygame.transform.rotozoom(ply2_sur,0,3)
ply2_rect = ply2_sur.get_rect(midbottom=(400, 300))

ply3_sur=ply3_sur.convert_alpha()
ply3_stand = pygame.transform.rotozoom(ply3_sur,0,3)
ply3_rect = ply3_sur.get_rect(midbottom=(600, 300))

g_name=test_font.render('rixser',False,(111,196,169))
g_name_rect=g_name.get_rect(center=(400,100))

game_mess = test_font.render('Press space to run',False,(111,196,169))
game_mess_rec= game_mess.get_rect(center=(400,320))

#sounds
jmp_sound= pygame.mixer.Sound('audio/jump.mp3')
jmp_sound.set_volume(0.04)

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.03)
bg_music.play(loops = -1)
 



#constants
player_grav =0
jump_count=0
game_update=False
str_time=0
score_val=0
obs_list=[]



while True:

    #eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_update:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump_count<=0:
                    player_grav=-22
                    jump_count+=1
                    jmp_sound.play()
            if event.type == obs_timer:
                if randint(0,2):
                    obs_list.append(slime_sur.get_rect(midbottom=(randint(900,1100), 301)))       
            
                else:
                    obs_list.append(fly_sur.get_rect(midbottom=(randint(900,1100), 200)))       
                
            if event.type == slime_timer:
                if slime_idx==0:
                    slime_idx=1
                else:
                    slime_idx=0
                slime_sur=slime_frame[slime_idx]
            if event.type == fly_timer:
                if fl_idx==0:
                    fl_idx=1
                else:
                    fl_idx=0
                fly_sur=fl_frame[fl_idx]

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_update=True

                    str_time= pygame.time.get_ticks()
        
            
    # game functions while active       
    if game_update:                

        screen.blit(sky_surface, (0, 0))
        screen.blit(grd_surface, (0, 300))

        score_val=dis_score()


        obs_move(obs_list)
    
    
        player_grav += 1
        ply_rect.y +=player_grav

        if ply_rect.bottom>=300:
            ply_rect.bottom=300
            jump_count=0
        
        play_animation()
        screen.blit(ply_sur, ply_rect)
        #colision
        game_update=col_dect(ply_rect,obs_list)
        
        
    # endscreen
    else:
        screen.fill('indigo')
        screen.blit(ply1_sur,ply1_rect)
        screen.blit(ply2_sur,ply2_rect)
        screen.blit(ply3_sur,ply3_rect)
        screen.blit(g_name,g_name_rect)  
        score_mess = test_font.render('yor score is {}'.format(score_val//1000),False,(111,196,169))
        score_mess_rec= score_mess.get_rect(center=(400,320))
        if score_val==0:
            screen.blit(game_mess,game_mess_rec)    
            
        else:              
            screen.blit(score_mess,score_mess_rec)

        obs_list.clear()
        ply_rect.midbottom= (80,300)
    pygame.display.update()
    clock.tick(60)
