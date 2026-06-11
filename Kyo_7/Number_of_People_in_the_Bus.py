def number(bus_stops):
    on_bus = 0
    for i in bus_stops:
        on_bus = on_bus + i[0] - i[1]
        
    return on_bus

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python