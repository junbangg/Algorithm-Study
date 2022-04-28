from collections import deque
def solution(record):
    lifo = []
    soldAmount = 0
    for data in record:
        _type, value, amount = data.split()
        if _type == 'P':
            lifo.append(list(map(int, [value, amount])))
        if _type == 'S':
            soldAmount += int(amount)
    lifoSoldAmount = soldAmount
    fifo = deque(lifo)
    # fifo
    fifo_value = 0
    while fifo and fifo[0][1] <= soldAmount:
        value, amount = fifo.popleft()
        fifo_value += value * amount
        soldAmount -= amount
    if fifo and soldAmount > 0:
        value, amount = fifo.popleft()
        fifo_value += value * min(amount, soldAmount)
    # lifo
    lifo_value = 0
    while lifo and lifo[-1][1] <= lifoSoldAmount:
        value, amount = lifo.pop()
        lifo_value += value * amount
        lifoSoldAmount -= amount
        print(lifoSoldAmount)
    if lifo and lifoSoldAmount > 0:
        value, amount = lifo.pop()
        lifo_value += value * min(amount, lifoSoldAmount)
    return fifo_value, lifo_value

print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]))
