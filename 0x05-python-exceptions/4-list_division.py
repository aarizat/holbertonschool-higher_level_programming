def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            d = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            d = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            d = 0
            continue
        except IndexError:
            print("out of range")
            d = 0
            continue
        finally:
            new_list.append(d)
    return new_list
