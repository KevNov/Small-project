# loop a days using generator

def week():
    days = ["monday","tuesday","wednsday","thursday","friday","saturday","sunday"]
    for day in days:
        yield day

days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
print(next(days)) # 'Wednesday'
print(next(days)) # 
print(next(days)) # 
print(next(days)) # 
print(next(days)) # 
print(next(days)) # 