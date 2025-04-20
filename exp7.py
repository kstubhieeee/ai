tab = []
result = []
goalList = ["a", "b", "c", "d", "e"]
problem = ["c", "a", "e", "d", "b"]

while problem:
    tab.append(problem.pop())

print("Initial tab :",tab)
count = 0
while tab and len(result) < len(goalList):
    count = count + 1 
    if tab[-1] == goalList[len(result)]:
        result.append(tab.pop())
        print("Step ",count," :")
        print(tab)
    else:
        tab.insert(0, tab.pop()) 
        print("Step ",count," :")
        print(tab)

print("Final Result:", result)
