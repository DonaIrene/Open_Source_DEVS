import pygame
level_map =[
    '                                                 ', # 24 colunas
    '                       XXXXXX                    ', # 10 lines
    '                       RRRRRR                    ',
    '     X                 RRRRRR        XXX         ',
    '     RX    X           RRRRRRXX                  ',
    '      X      XXX     XXRRRR       XX        X    ',
    '                                                 ',
    '                                                 ',
    '                                                 ',
    '                                                 ',
    '        X    XX    X   XXXX    X   X         X   ',
    '      XXR    R     RR  RRRR  XX    X          X  ',
    '        R    R                                   ',
    'XP XX   RR                     X                f',
    'XXXRRXXXR    XXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXX',
]

title_size = 30
screen_width = 1200
screen_heigth = len(level_map)*title_size