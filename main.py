def on_a_pressed():
    global projectile
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        ninjaStar
    """), mySprite, 0, -100)
    pause(500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_hit_wall(sprite, location):
    game.game_over(False)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

def on_on_overlap(sprite2, otherSprite):
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
    sprites.destroy(sprite2)
    sprites.destroy(otherSprite, effects.fire, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

projectile2: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    dojo
"""))
tiles.set_current_tilemap(tilemap("""
    floor
"""))
mySprite = sprites.create(assets.image("""
    Ninja
"""), SpriteKind.player)
mySprite.set_position(75, 100)
controller.move_sprite(mySprite, 75, 0)
info.set_score(0)

def on_update_interval():
    global projectile2
    projectile2 = sprites.create_projectile_from_side(assets.image("""
        bug
    """), 0, 25)
    projectile2.set_kind(SpriteKind.enemy)
    projectile2.x = randint(10, 150)
game.on_update_interval(1000, on_update_interval)
