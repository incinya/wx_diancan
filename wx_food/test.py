list01 = [{'id': 1}, {'id': 4}, {'id': 2}, {'id': 3}]


def take_id(elem):
    return elem['id']


list01.sort(key=take_id)
print(list01)
