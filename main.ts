controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    projectile = sprites.createProjectileFromSprite(assets.image`ninjaStar`, mySprite, 0, -100)
    pause(500)
})
scene.onHitWall(SpriteKind.Enemy, function (sprite, location) {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.InBackground)
    info.changeScoreBy(1)
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.fire, 500)
})
let projectile2: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundImage(assets.image`dojo`)
tiles.setCurrentTilemap(tilemap`floor`)
mySprite = sprites.create(assets.image`Ninja`, SpriteKind.Player)
mySprite.setPosition(75, 100)
controller.moveSprite(mySprite, 75, 0)
info.setScore(0)
game.onUpdateInterval(1000, function () {
    projectile2 = sprites.createProjectileFromSide(assets.image`bug`, 0, 25)
    projectile2.setKind(SpriteKind.Enemy)
    projectile2.x = randint(10, 150)
})
