def rental_car_cost(d):
    cost = d * 40

    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20

    return cost


# https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python