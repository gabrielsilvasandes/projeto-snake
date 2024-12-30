import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preta = (30, 30, 30)
verde = (50, 205, 50)
verde_escuro = (34, 139, 34)
vermelha = (255, 70, 70)
vermelha_escuro = (139, 0, 0)
tamanho_quadrado = 20
velocidade_jogo = 10
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y
def desenhar_comida(tamanho, comida_x, comida_y):
    sombra_offset = 4
    pygame.draw.rect(tela, vermelha_escuro, [comida_x + sombra_offset, comida_y + sombra_offset, tamanho, tamanho], border_radius=5)
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho], border_radius=5)
def desenhar_cobra(pixels):
    sombra_offset = 4
    for pixel in pixels:
        pygame.draw.rect(tela, verde_escuro, [pixel[0] + sombra_offset, pixel[1] + sombra_offset, tamanho_quadrado, tamanho_quadrado], border_radius=5)
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado], border_radius=5)
def rodar_jogo():
    fim_jogo = False
    x = largura // 2
    y = altura // 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -tamanho_quadrado
                    velocidade_y = 0
                if evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = tamanho_quadrado
                    velocidade_y = 0
                if evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_x = 0
                    velocidade_y = -tamanho_quadrado
                if evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_x = 0
                    velocidade_y = tamanho_quadrado

        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        pixels.append((x, y))
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        for segmento in pixels[:-1]:
            if segmento == (x, y):
                fim_jogo = True
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        desenhar_cobra(pixels)
        pygame.display.update()
        relogio.tick(20)
    pygame.quit()
rodar_jogo()
