import wrap ,time
wrap.world.create_world(1920,1080,910,50)
player=wrap.sprite.add("mario-1-big",960,540,"walk3")
wrap.sprite.set_size_percent(player,150,150)
wrap.world.set_back_color(255,255,255)
wrap.add_sprite_dir("My sprite gens")
menu=wrap.sprite.add("backimages",960,540,"menu")

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.set_reverse_x(player,False)
        wrap.sprite.move(player,10,0)
        wrap.sprite.set_costume(player,"walk1")
    elif wrap.sprite.is_collide_sprite(player,menu) == True:
        wrap.sprite.move_to(player,960,540)

@wrap.on_key_always(wrap.K_LEFT)
def left():
    if wrap.sprite.is_collide_sprite(player,menu)==False and wrap.sprite.is_visible(menu) == True:
        wrap.sprite.set_reverse_x(player,True)
        wrap.sprite.move(player, -10, 0)
        wrap.sprite.set_costume(player, "walk1")
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)
    if wrap.sprite.get_left(player) <= 0 :
        wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/imgonline-com-ua-Resize-dc6B9AZEgPA3.jpg')
        wrap.sprite.move_to(player,1880,540)
        wrap.sprite.add("battle_city_items", 1910, 540,"effect_appearance4")
        wrap.sprite.hide(menu)
    elif wrap.sprite.is_visible(menu) == False:

@wrap.on_key_always(wrap.K_UP)
def up():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.set_costume(player,"walk1")
        wrap.sprite.move(player, 0, -10)
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)

@wrap.on_key_always(wrap.K_DOWN)
def down():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.move(player, 0, 10)
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)






















