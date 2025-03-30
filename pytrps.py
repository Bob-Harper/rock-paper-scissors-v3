in_game = False
hand = 0

def on_gesture_shake():
    global in_game, hand
    in_game = True
    basic.clear_screen()
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SCISSORS)
    basic.clear_screen()
    basic.pause(500)
    basic.show_number(1)
    basic.show_number(2)
    basic.show_number(3)
    basic.clear_screen()
    basic.pause(500)
    hand = randint(1, 3)
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(2000)
        basic.clear_screen()
        basic.show_string("ROCK")
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
        music.play(music.builtin_playable_sound_effect(soundExpression.spring),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(2000)
        basic.clear_screen()
        basic.show_string("PAPER")
    else:
        basic.show_icon(IconNames.SCISSORS)
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(2000)
        basic.clear_screen()
        basic.show_string("SCISSORS")
    basic.pause(1000)
    basic.show_string("AGAIN!")
    basic.pause(1000)
    basic.show_string("READY?")
    basic.pause(500)
    in_game = False
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if in_game:
        game.pause()
    else:
        if not (in_game):
            basic.show_leds("""
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                . . . . .
                """)
        else:
            game.pause()
        if not (in_game):
            basic.show_leds("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """)
        else:
            game.pause()
        if not (in_game):
            basic.show_leds("""
                . . . . .
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                """)
        else:
            game.pause()
        if not (in_game):
            basic.show_leds("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """)
        else:
            game.pause()
        if not (in_game):
            basic.show_string("S")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("H")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("A")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("K")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("E")
        else:
            game.pause()
        if not (in_game):
            basic.show_string(" ")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("M")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("E")
        else:
            game.pause()
        if not (in_game):
            basic.show_string("!")
        else:
            game.pause()
basic.forever(on_forever)
