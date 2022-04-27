import wrap ,time
wrap.world.create_world(1920,1000,0,0)
player=wrap.sprite.add("mario-1-big",960,540,"walk3")
star=wrap.sprite.add("battle_city_items", 1910, 0, "effect_appearance4",visible=False)
wrap.sprite.set_size_percent(player,150,150)
wrap.world.set_back_color(255,255,255)
wrap.add_sprite_dir("My sprite gens")
menu=wrap.sprite.add("backimages",960,540,"menu")
def perehod1 ():
    wrap.sprite.move_to(player, 960, 540)
    wrap.world.clear_back_image()
    wrap.sprite.hide(star)
    wrap.sprite.show(menu)
    wrap.sprite.move_to(menu, 960, 540)
@wrap.on_key_always(wrap.K_RIGHT)
def right():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.set_reverse_x(player,False)
        wrap.sprite.move(player,10,0)
        wrap.sprite.set_costume(player,"walk1")
    elif wrap.sprite.is_collide_sprite(player,menu) == True:
        wrap.sprite.move_to(player,960,540)
    if wrap.sprite.get_right(player) >= 1910 and wrap.sprite.is_visible(star) == False:
        wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/imgonline-com-ua-Resize-YKrnuQo4CRYhakZ.jpg')
        wrap.sprite.move_to(player,160,540)
        wrap.sprite.add("battle_city_items",30, 540,"effect_appearance4")
        wrap.sprite.hide(menu)
        perehod1()
@wrap.on_key_always(wrap.K_LEFT)
def left():
    wrap.sprite.move(player, -10, 0)
    if wrap.sprite.is_collide_sprite(player,menu)==False and wrap.sprite.is_visible(menu) == True:
        wrap.sprite.set_reverse_x(player,True)
        wrap.sprite.set_costume(player, "walk1")
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)
    if wrap.sprite.get_left(player) <= 0 and wrap.sprite.is_visible(menu) == True:
        wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/imgonline-com-ua-Resize-M8DyfAYKJj1NI.jpg')
        wrap.sprite.show(star)
        wrap.sprite.move_to(player,1860,540)
        wrap.sprite.hide(menu)
    elif wrap.sprite.is_collide_sprite(player,star) and wrap.sprite.is_visible(menu) == False:
        perehod1()
    elif wrap.sprite.is_visible(menu) == False:
        wrap.sprite.move_to(menu,4000,5000)
        wrap.sprite.set_reverse_x(player,True)
    # elif wrap.sprite.is_collide_sprite(player, star) == True:
    #     wrap.sprite.move_to(player,1900,540)
    #     wrap.world.clear_back_image()
    #     wrap.sprite.hide(star)
    #     wrap.sprite.show(menu)
    #     wrap.sprite.move_to(menu, 960, 540)

@wrap.on_key_always(wrap.K_UP)
def up():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.set_costume(player,"walk1")
        wrap.sprite.move(player, 0, -10)
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)
    if wrap.sprite.get_top(player) <= 0 :
        wrap.world.set_back_image('C:/Users/Tim GF63/Downloads/imgonline-com-ua-Resize-QeU1UQJytzj0Nf.jpg')
        wrap.sprite.move_to(player,960,900)
        wrap.sprite.add("battle_city_items",960,970,"effect_appearance4")
        wrap.sprite.hide(menu)
@wrap.on_key_always(wrap.K_DOWN)
def down():
    if wrap.sprite.is_collide_sprite(player,menu)==False:
        wrap.sprite.move(player, 0, 10)
    elif wrap.sprite.is_collide_sprite(player, menu) == True:
        wrap.sprite.move_to(player, 960, 540)






















