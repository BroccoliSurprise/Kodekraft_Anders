@namespace
class SpriteKind:
    kull = SpriteKind.create()

def on_overlap_tile(sprite, location):
    mySprite.set_image(img("""
        . f f f . f f f f . f f f . 
                f f f f f c c c c f f f f f 
                f f f f b c c c c b f f f f 
                f f f c 3 c c c c 3 c f f f 
                . f 3 3 c c c c c c 3 3 f . 
                . f c c c c 4 4 c c c c f . 
                . f f c c 4 4 4 4 c c f f . 
                . f f f b f 4 4 f b f f f . 
                . f f 4 1 f d d f 1 4 f f . 
                . . f f d d d d d d f f . . 
                . . e f e 4 4 4 4 e f e . . 
                . e 4 f b 3 3 3 3 b f 4 e . 
                . 4 d f 3 3 3 3 3 3 c d 4 . 
                . 4 4 f 6 6 6 6 6 6 f 4 4 . 
                . . . . f f f f f f . . . . 
                . . . . f f . . f f . . . .
    """))
    effects.clear_particles(mySprite)
scene.on_overlap_tile(SpriteKind.player, myTiles.transparency16, on_overlap_tile)

def on_countdown_end():
    if info.score() < 20:
        game.over(False)
    else:
        game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.halo, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_overlap_tile2(sprite, location):
    mySprite.say("blubb blubb", 500)
    mySprite.set_image(img("""
        . f f f . f f f f . f f f . 
                f f f f f c c c c f f f f f 
                f f f f b c c c c b f f f f 
                f f f c 3 c c c c 3 c f f f 
                . f 3 3 c c c c c c 3 3 f . 
                . f c c c c 4 4 c c c c f . 
                . f f c c 4 4 4 4 c c f f . 
                . f f f b f 4 4 f b f f f . 
                . f f 4 1 f d d f 1 4 f f . 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """))
    mySprite.start_effect(effects.bubbles)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile1, on_overlap_tile2)

def on_on_overlap2(sprite, otherSprite):
    global seismisk_aktivitet
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(10)
    scene.camera_shake(2, 500)
    if Math.percent_chance(seismisk_aktivitet * 2):
        game.splash("ÆÆÆÆ JORDSKJELV!")
        game.over(False, effects.melt)
    seismisk_aktivitet += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.kull, on_on_overlap2)

mySprite2: Sprite = None
energi: Sprite = None
mySprite: Sprite = None
seismisk_aktivitet = 0
seismisk_aktivitet = 0
tiles.set_tilemap(tilemap("""
    level
"""))
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
if Math.percent_chance(20):
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_path5)
else:
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass1)
mySprite3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
controller.player2.move_sprite(mySprite3)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
for index in range(100):
    energi = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . f f f f . . . . . 
                    . . . . . . f f 5 5 f . . . . . 
                    . . . . . . f 5 5 f f . . . . . 
                    . . . . . f f 5 f f . . . . . . 
                    . . . . f f 5 5 f f f . . . . . 
                    . . . . f 5 5 5 5 5 f . . . . . 
                    . . . . f f f f 5 5 f . . . . . 
                    . . . . . . f 5 5 f f . . . . . 
                    . . . . . f f 5 f f . . . . . . 
                    . . . . . f 5 f f . . . . . . . 
                    . . . . . f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    if Math.percent_chance(80):
        tiles.place_on_random_tile(energi, sprites.castle.tile_path5)
    else:
        tiles.place_on_random_tile(energi, sprites.castle.tile_grass1)
for index2 in range(25):
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . f f . . . . . . 
                    . . . . . . f f f f f f . . . . 
                    . . . . f f d d f d d f f f . . 
                    . . . . f d f f f d f f d f . . 
                    . . . f f f f f d f d f f f . . 
                    . . f f f f f f f f f d f d f . 
                    . . f f f f f f d f d d f d f . 
                    . f f f f d f d d f d f f f f . 
                    . f f d d f f f f f f f d d f . 
                    . f d d d d f f d f f d f d f . 
                    . f f d d d f f f f d f f f f . 
                    . . f f d f f d f f f f f f . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.kull)
    tiles.place_on_random_tile(mySprite2, sprites.castle.tile_path5)

def on_update_interval():
    global seismisk_aktivitet
    if seismisk_aktivitet > 0:
        seismisk_aktivitet += -1
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    scene.camera_shake(seismisk_aktivitet, 500)
game.on_update_interval(1000, on_update_interval2)
