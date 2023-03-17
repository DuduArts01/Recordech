import pygame

class Outset(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, image_x, image_y, width, height, resize_x, resize_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_outset = []
        for i in range(1): 
            img = sprite_sheet.subsurface((i * image_x, 0 * image_y), (width, height))
            img = pygame.transform.scale(img, (resize_x, resize_y))
            self.image_outset.append(img)

        self.image = self.image_outset[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):                       
        self.image = self.image_outset[int(0)]
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        pass