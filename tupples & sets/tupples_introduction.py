month = ("jan", "feb", "mar", "apr", "may", "june", "july", "aug", "sep", "oct" ,"nov", "dec")
print(month[3])

# Tuples can be used as a key in dictionaries
locations = {
    (35.6873, 39.6173) : "Tokyo office",
    (32.8717, 69.6382) : "New york office",
    (45.9272, 102.0282) : "San francisco office",
    (65.9181, 87.8595) : "Singapore office",
    (24.9101, 75.9101) : "Jakarta office"
}
print(locations[(65.9181, 87.8595)])