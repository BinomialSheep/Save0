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
            if get_ground_type() != Grounds.Grassland:
                till()
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


def harvest_tree_and_carrot_glass_all():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if (i + j) % 2 == 0:
                if can_harvest():
                    harvest()
                plant(Entities.Tree)
            else:
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
                elif can_harvest():
                    pass
                else:
                    # まだ成長途中でどちらのパンプキンになるか分からない
                    if get_water() < 0.5:
                        use_item(Items.Water)
                    ok = False
                move(North)
            if ok:
                break
        move(East)
    if can_harvest():
        harvest()


def get_max_index(list):
    max_index = 0
    for i in range(len(list)):
        if list[i] > list[max_index]:
            max_index = i
    return max_index


# def plant_sunflower(num=20):
#     # 花びらの枚数
#     list = []
#     for j in range(10):
#         if get_ground_type() != Grounds.Soil:
#             till()
#         plant(Entities.Sunflower)
#         if get_water() < 0.8:
#             use_item(Items.Water)
#         list.append(measure())
#         move(North)
#     for i in range(num):
#         max_index = get_max_index(list)
#         go_to_xy(get_pos_x(), max_index)
#         while True:
#             if get_entity_type() != Entities.Sunflower:
#                 break
#             if can_harvest():
#                 break
#             if get_water() < 0.8:
#                 use_item(Items.Water)
#             pass
#         if can_harvest():
#             harvest()
#             plant(Entities.Sunflower)
#             list[max_index] = measure()
#     go_to_start()
#     for j in range(10):
#         while True:
#             if get_entity_type() != Entities.Sunflower:
#                 break
#             if can_harvest():
#                 break
#             if get_water() < 0.5:
#                 use_item(Items.Water)
#             pass
#         if can_harvest():
#             harvest()
#         move(North)
def plant_sunflower():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Sunflower)
            move(North)
        move(East)

    for k in range(9):
        vul = 15 - k
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if (
                    get_entity_type() == Entities.Sunflower
                    and measure() == vul
                    and can_harvest()
                ):
                    harvest()
                move(North)
            move(East)


def harvest_all():
    go_to_start()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            move(North)
        move(East)


def harvest_weird_substance_all():
    clear()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            while not can_harvest():
                pass
            if i % 2 == 0 and j % 2 == 0:
                use_item(Items.Weird_Substance)
            harvest()
            move(North)
        move(East)
    harvest_all()


# def exec_dinorsaur():
#     change_hat(Hats.Dinosaur_Hat)
#     set_world_size(5)
#     do_a_flip()
#     do_a_flip()

#     ok = True
#     for i in range(5):
#         for j in range(5):
#             ok = move(North)
#             if not ok:
#                 break
#         ok = move(East)
#         if not ok:
#             break


#     change_hat(Hats.Green_Hat)
#     set_world_size(32)
def exec_dinorsaur_naive():
    change_hat(Hats.Dinosaur_Hat)

    next_x, next_y = measure()
    ok = True
    count = 0
    target_count = 10000

    while count < target_count:
        while ok and get_pos_x() > next_x:
            ok = move(West)
        while ok and get_pos_x() < next_x:
            ok = move(East)
        while ok and get_pos_y() > next_y:
            ok = move(South)
        while ok and get_pos_y() < next_y:
            ok = move(North)
        if not ok:
            break
        next_x, next_y = measure()
        count += 1

    change_hat(Hats.Green_Hat)


# def exec_dinosaur():
#     change_hat(Hats.Dinosaur_Hat)


#     ok = True
#     while ok:
#         x, y = get_pos_x(), get_pos_y()
#         if x % 2 == 0:
#             if y < get_world_size() - 1:
#                 ok = move(North)
#             else:
#                 ok = move(East)
#         else:
#             if y > 0:
#                 ok = move(South)
#             else:
#                 ok = move(East)
#     change_hat(Hats.Green_Hat)


# FIXME：数手先で詰むケースを考慮できていない
def exec_dinosaur():
    change_hat(Hats.Dinosaur_Hat)

    tail_list = []
    next_x, next_y = measure()

    def dinorsaur_move(direction):
        global next_x
        global next_y
        ret = move(direction)
        tail_list.append((get_pos_x(), get_pos_y()))
        if next_x == get_pos_x() and next_y == get_pos_y():
            next_x, next_y = measure()
        else:
            if tail_list:
                tail_list.pop(0)
        return ret

    def valid_move(direction):
        nx = get_pos_x()
        ny = get_pos_y()
        ok = True
        if direction == West:
            nx -= 1
            ok = y == 0
        elif direction == East:
            nx += 1
            ok = y != 0
        elif direction == North:
            ny += 1
            ok = x % 2 == 0 and y < get_world_size() - 1
        elif direction == South:
            ny -= 1
            ok = y == 1 or (x % 2 == 1 and y != 0)
        # 自分の尻尾にぶつかる位置にはいけない（fixme 実際は先頭にはいける）
        if (nx, ny) in tail_list:
            ok = False
        return ok

    ok = True
    while ok:
        x, y = get_pos_x(), get_pos_y()
        if x > next_x:
            ds = [West, South, East, North]
        elif x == next_x:
            ds = [North, South, East, West]
        else:
            if next_y > y:
                ds = [North, East, South, West]
            elif next_y == y:
                ds = [East, North, South, West]
            else:
                ds = [South, East, North, West]
        for d in ds:
            if valid_move(d):
                ok = dinorsaur_move(d)
                break
    change_hat(Hats.Green_Hat)


def exec_treature_one():
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    visited = set()
    visited.add((get_pos_x(), get_pos_y()))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    d = [East, North, West, South]

    def dfs(parent_direction):
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True
        for i in range(4):
            nx = get_pos_x() + dx[i]
            ny = get_pos_y() + dy[i]
            if 0 <= nx < get_world_size() and 0 <= ny < get_world_size():
                if can_move(d[i]) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    move(d[i])
                    if dfs(i):
                        return True
        if parent_direction != -1:
            move(d[(parent_direction + 2) % 4])
        return False

    dfs(-1)


def exec_treature():
    # clear()
    # plant(Entities.Bush)
    # substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    # use_item(Items.Weird_Substance, substance)
    for i in range(4):
        do_a_flip()
    visited = set()
    visited.add((get_pos_x(), get_pos_y()))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    d = [East, North, West, South]

    def dfs(parent_direction):
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True
        for i in range(4):
            nx = get_pos_x() + dx[i]
            ny = get_pos_y() + dy[i]
            if nx < 0 or ny < 0 or nx >= get_world_size() or ny >= get_world_size():
                if can_move(d[i]):
                    # 外壁がない時はすでにゲームが終了している
                    return True
            else:
                if can_move(d[i]) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    move(d[i])
                    if dfs(i):
                        return True
        if parent_direction != -1:
            move(d[(parent_direction + 2) % 4])
        return False

    dfs(-1)
    # clear()


def exec_treature_parallel(drawn_num=32):
    clear()

    for _ in range(drawn_num):
        move(East)
        move(North)
        spawn_drone(exec_treature)

    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    exec_treature()


# 並列ヒマワリ＆カボチャ
def harvest_sunflower_and_pumpkin_parallel():

    drawn_num = 32
    wait_tic = 310 * drawn_num

    def func():
        for i in range(wait_tic):
            pass

        for i in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Sunflower)
            move(North)
        for k in range(9):
            vul = 15 - k
            for i in range(get_world_size()):
                if (
                    get_entity_type() == Entities.Sunflower
                    and measure() == vul
                    and can_harvest()
                ):
                    harvest()
                move(North)

    for _ in range(drawn_num):
        spawn_drone(func)
        move(East)
        wait_tic -= 310
    func()


def main():
    # harvest_all()
    loop_count = 0
    clear()

    harvest_sunflower_and_pumpkin_parallel()

    # exec_dinorsaur_naive()

    # while True:
    #     clear()
    #     if loop_count % 10 == 0:
    #         plant_sunflower()
    #     elif loop_count % 10 == 1:
    #         harvest_tree_all()
    #     elif loop_count % 10 == 2:
    #         plant_pumpkin()
    #     elif loop_count % 10 == 3:
    #         harvest_carrot_all()
    #     elif loop_count % 10 == 4:
    #         harvest_cactus_all()
    #     elif loop_count % 10 == 5:
    #         harvest_tree_all()
    #     elif loop_count % 10 == 6:
    #         plant_sunflower()
    #     elif loop_count % 10 == 7:
    #         harvest_glass()
    #     elif loop_count % 10 == 8:
    #         harvest_glass()
    #     elif loop_count % 10 == 9:
    #         harvest_glass()
    #     loop_count += 1


if __name__ == "__main__":
    main()
