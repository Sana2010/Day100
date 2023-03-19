ground_y = 300
dinosaur_y = ground_y
jumping = False
jump_vel = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                jump_vel = -10
                jump_sound.play()

    if jumping:
        dinosaur_y += jump_vel
        jump_vel += 1
        if dinosaur_y >= ground_y:
            jumping = False
            dinosaur_y = ground_y

    screen.blit(background, (0, 0))
    screen.blit(ground, (0, ground_y))
    screen.blit(cactus, (600, 250))
    dinosaur_rect = pygame.Rect(50, dinosaur_y, 64, 64)
    pygame.draw.rect(screen, (255, 0, 0), dinosaur_rect)

    pygame.display.update()
