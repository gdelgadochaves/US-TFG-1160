def priceRange(x):
    if x < 20.0:
        price_range = 0.0
    elif x >= 20.0 and x < 50.0:
        price_range = 1.0
    elif x >= 50.0 and x < 100.0:
        price_range = 2.0
    elif x >= 100.0 and x < 150.0:
        price_range = 3.0
    elif x >= 150.0 and x < 200.0:
        price_range = 4.0
    elif x >= 200.0 and x < 250.0:
        price_range = 5.0
    elif x >= 250.0 and x < 300.0:
        price_range = 6.0
    elif x >= 300.0 and x < 350.0:
        price_range = 7.0
    elif x >= 350.0 and x < 400.0:
        price_range = 8.0
    elif x >= 400.0 and x < 450.0:
        price_range = 9.0
    elif x >= 450.0 and x < 500.0:
        price_range = 10.0
    elif x >= 500.0:
        price_range = 11.0
    else:
        price_range = -1.0
    return price_range
