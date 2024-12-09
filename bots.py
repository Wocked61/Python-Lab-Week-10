import threading
import time
import json

with open("inventory.dat", "r") as f:
    inventory = json.load(f)

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    threads = []
    robot_fetchers = [[], [], []]
    for i, item in enumerate(items):
        item_index = i % 3
        robot_fetchers[item_index].append(item)


    for robot_list in robot_fetchers:
        if robot_list:
            thread = threading.Thread(target=bot_fetcher, args=(robot_list, cart, lock))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(item_list, cart, lock):
    for item in item_list:
        item_info = inventory[item]
        item_disc = item_info[0]
        item_time = item_info[1]
        time.sleep(item_time)

        with lock:
            cart.append([item, item_disc])