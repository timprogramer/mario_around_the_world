import wrap ,time
wrap.world.create_world(1920,1080,1000,340)
player=wrap.sprite.add("mario-1-big",960,540,"walk3")
wrap.world.set_back_image('/Users/Tim GF63/Desktop/program progkids/2022-04-06_23.23.21.png')

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    if wrap.sprite.get_reverse_y(player)==True:
        wrap.sprite.set_reverse_y(player,False)
    wrap.sprite.set_reverse_x(player,False)
    wrap.sprite.move(player,10,0)
    wrap.sprite.set_costume(player,"walk1")

@wrap.on_key_always(wrap.K_LEFT)
def left():
    if wrap.sprite.get_reverse_y(player)==True:
        wrap.sprite.set_reverse_y(player,False)
    wrap.sprite.set_reverse_x(player,True)
    wrap.sprite.move(player, -10, 0)
    wrap.sprite.set_costume(player, "walk1")

@wrap.on_key_always(wrap.K_UP)
def up():
    wrap.sprite.set_costume(player,"swim3")
    wrap.sprite.set_reverse_y(player,False)
    wrap.sprite.move(player, 0, -10)

@wrap.on_key_always(wrap.K_DOWN)
def down():
    wrap.sprite.set_reverse_y(player,True)
    wrap.sprite.move(player, 0, 10)






















