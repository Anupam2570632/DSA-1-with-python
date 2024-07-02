
def hanoi(disc, source, spare, target):
    global count
    if disc > 0:
        hanoi(disc - 1, source, target, spare)
        print(f"move disc {disc} from {source} to {target}")
        target.append(source.pop())
        count += 1
        hanoi(disc - 1, spare, source, target)
        

source = [3, 2, 1]  # Initial source tower with discs
spare = []          # Initial spare tower (empty)
target = []         # Initial target tower (empty)
count = 0

print('-------------------')
hanoi(len(source), source, spare, target)
print("Moves:", count)
print("Source:", source)
print("Spare:", spare)
print("Target:", target)
