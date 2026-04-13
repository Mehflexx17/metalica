mySprite = sprites.create(assets.image("""myImage"""), SpriteKind.player)
music.play(music.create_song(assets.song("""mySong""")),
    music.PlaybackMode.UNTIL_DONE)