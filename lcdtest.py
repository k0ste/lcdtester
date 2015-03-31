#!/usr/bin/env python2
#coding=utf-8
#
#       lcdtest.py
#       
#       Copyright 2009 Matthew Brush <mbrush AT leftclick DOT ca>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os, sys, random
import pygame
from pygame.locals import *
        
def main():
   
    pygame.init()
    clock = pygame.time.Clock()
    
    inf = pygame.display.Info()
    
    win_size = (inf.current_w, inf.current_h)
    screen = pygame.display.set_mode(win_size)
    pygame.display.set_caption('Monitor Manager')
    pygame.mouse.set_visible(1)
    pygame.display.toggle_fullscreen()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))
    
    pygame.key.set_repeat(100,100)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    (r,g,b) = (0,0,0)
    incr = 1
    rgb_cnt = 0
    
    font = pygame.font.Font(None,24)
    font2 = pygame.font.Font(None, 32)
    
    text1 = font2.render('LCD Pixel Tester', True, (255,255,255))
    text2 = font.render(u'[R], [G] или [B] для включения этого цвета', True, (255,255,255))
    text3 = font.render(u'[SPACE] для генерации произвольного цвета', True, (255,255,255))
    text4 = font.render(u'[ENTER] для включения черного цвета', True, (255,255,255))
    text5 = font.render(u'[TAB]/[MOUSE1] для переключения между 100% R, G, B, белым и черным', True, (255,255,255))
    text6 = font.render(u'[H]/[MOUSE3] показать/скрыть это сообщение', True, (255,255,255))
    text7 = font.render(u'[ESCAPE]/[MOUSE2] чтобы выйти', True, (255,255,255))
    
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()
    textRect5 = text5.get_rect()
    textRect6 = text6.get_rect()
    textRect7 = text7.get_rect()
    
    textRect1.centerx = screen.get_rect().centerx
    textRect2.centerx = screen.get_rect().centerx
    textRect3.centerx = screen.get_rect().centerx
    textRect4.centerx = screen.get_rect().centerx
    textRect5.centerx = screen.get_rect().centerx
    textRect6.centerx = screen.get_rect().centerx
    textRect7.centerx = screen.get_rect().centerx
    
    textRect1.centery = screen.get_rect().centery - (textRect4.height * 4)
    textRect2.centery = screen.get_rect().centery - (textRect4.height * 2)
    textRect3.centery = screen.get_rect().centery - textRect4.height
    textRect4.centery = screen.get_rect().centery
    textRect5.centery = screen.get_rect().centery + textRect4.height
    textRect6.centery = screen.get_rect().centery + (textRect4.height * 2)
    textRect7.centery = screen.get_rect().centery + (textRect4.height * 3)
    
    help_enabled = True
    
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                return
            elif event.type == KEYDOWN and event.key == K_r:
                r = r + incr
            elif event.type == KEYDOWN and event.key == K_g:
                g = g + incr
            elif event.type == KEYDOWN and event.key == K_b:
                b = b + incr
            elif event.type == KEYDOWN and event.key == K_SPACE:
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
            elif event.type == KEYDOWN and event.key == K_RETURN:
                (r,g,b) = (0,0,0)
            elif event.type == KEYDOWN and event.key == K_TAB:
                if rgb_cnt == 0:
                    (r,g,b) = (255,0,0)
                elif rgb_cnt == 1:
                    (r,g,b) = (0,255,0)
                elif rgb_cnt == 2:
                    (r,g,b) = (0,0,255)
                elif rgb_cnt == 3:
                    (r,g,b) = (255,255,255)
                elif rgb_cnt == 4:
                    (r,g,b) = (0,0,0)
                rgb_cnt = rgb_cnt + 1
                if rgb_cnt > 4:
                    rgb_cnt = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rgb_cnt == 0:
                    (r,g,b) = (255,0,0)
                elif rgb_cnt == 1:
                    (r,g,b) = (0,255,0)
                elif rgb_cnt == 2:
                    (r,g,b) = (0,0,255)
                elif rgb_cnt == 3:
                    (r,g,b) = (255,255,255)
                elif rgb_cnt == 4:
                    (r,g,b) = (0,0,0)
                rgb_cnt = rgb_cnt + 1
                if rgb_cnt > 4:
                    rgb_cnt = 0
            elif event.type == KEYDOWN and event.key == K_h:
                if help_enabled:
                    help_enabled = False
                else:
                    help_enabled = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                if help_enabled:
                    help_enabled = False
                else:
                    help_enabled = True
                    
        if r > 255:
            r = 0
        if g > 255:
            g = 0
        if b > 255:
            b = 0
        
        c = (r,g,b)
        
        textColor = font.render('R: %03d, G: %03d, B: %03d' % c, True, (255,255,255))
        textColorRect = textColor.get_rect()
        textColorRect.centerx = screen.get_rect().centerx
        textColorRect.centery = screen.get_rect().centery + (textRect4.height * 5)
              
        background.fill(c)
        screen.blit(background, (0,0))
        
        if help_enabled:
            screen.blit(text1, textRect1)
            screen.blit(text2, textRect2)
            screen.blit(text3, textRect3)
            screen.blit(text4, textRect4)
            screen.blit(text5, textRect5)
            screen.blit(text6, textRect6)
            screen.blit(text7, textRect7)
            screen.blit(textColor, textColorRect)
        
        pygame.display.flip()
           
    return 0

if __name__ == '__main__': main()
