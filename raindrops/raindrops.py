from collections import namedtuple
def convert(number):
    Item = namedtuple('Item', ['number', 'value'])
    values = [
        Item(number=3, value="Pling"),
        Item(number=5, value="Plang"),
        Item(number=7, value="Plong")
    ]

    response = []
    for item in values:
        if number % item.number == 0:
            response.append(item.value)

    if not response:
        response.append(str(number))

    return "".join(response)
