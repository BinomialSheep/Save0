def go_to_start():
    while get_pos_x() > 0:
        move(West)
    while get_pos_y() > 0:
        move(South)


# todo: はみ出してワープした方が早い場合がある
def go_to_xy(x, y):
    while get_pos_x() > x:
        move(West)
    while get_pos_x() < x:
        move(East)
    while get_pos_y() > y:
        move(South)
    while get_pos_y() < y:
        move(North)


def harvest_glass(num=6):
    for i in range(num):
        for j in range(get_world_size()):
            while not can_harvest():
                pass
            harvest()
            move(North)
    clear()


def harvest_bush_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            plant(Entities.Bush)
            move(North)
        move(East)
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            while not can_harvest():
                pass
            harvest()
            move(North)
        move(East)


def harvest_tree_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if (i + j) % 2 == 0:
                plant(Entities.Tree)
            else:
                plant(Entities.Bush)
            move(North)
        move(East)
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            while not can_harvest():
                pass
            harvest()
            move(North)
        move(East)


def harvest_carrot_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Carrot)
            move(North)
        move(East)
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            while not can_harvest():
                pass
            harvest()
            move(North)
        move(East)


# サボテン
def harvest_cactus_all():
    size = get_world_size()
    for i in range(size):
        for j in range(size):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)
    # 列のソートをする
    for i in range(size):
        for j in range(size):
            prev = -1
            ok = True
            for k in range(size):
                cur = measure()
                if prev > cur:
                    ok = False
                    swap(South)
                prev = cur
                move(North)
            if ok:
                break
        move(East)
    # 行のソートをする
    for i in range(size):
        for j in range(size):
            prev = -1
            ok = True
            for k in range(size):
                cur = measure()
                if prev > cur:
                    ok = False
                    swap(West)
                prev = cur
                move(East)
            if ok:
                break
        move(North)
    # 収穫
    go_to_start()
    if can_harvest():
        harvest()


def watering_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            use_item(Items.Water)
            move(North)
        move(East)


def plant_pumpkin():
    # 最初の埋め
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Pumpkin)
            move(North)
        move(East)
    for i in range(get_world_size()):
        while True:
            ok = True
            for j in range(get_world_size()):
                if get_entity_type() == Entities.Dead_Pumpkin:
                    plant(Entities.Pumpkin)
                    if get_water() < 0.5:
                        use_item(Items.Water)
                    ok = False
                move(North)
            if ok:
                break
        move(East)
    if can_harvest():
        harvest()


def harvest_all():
    go_to_start()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            move(North)
        move(East)


# go_to_start()
# harvest_all()
def main():
    loop_count = 0
    if can_harvest():
        harvest()
    # watering_all()
    clear()
    # harvest_cactus_all()
    while True:
        clear()
        harvest_glass()
        if loop_count % 10 == 0:
            plant_pumpkin()
        elif loop_count % 4 == 0:
            harvest_carrot_all()
        else:
            harvest_tree_all()
        loop_count += 1


if __name__ == "__main__":
    main()
