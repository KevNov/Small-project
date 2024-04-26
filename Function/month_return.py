def return_month(num):
    month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if num > 0 and num < len(month):
        return month[num-1]
    return None

print(return_month(5))
print(return_month(2))
print(return_month(11))

