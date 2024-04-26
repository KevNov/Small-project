# donation list (in rupiah)

donations = dict(irham=40, ihram=30, faiz=75, dion=60, kevin=50, fredo=55, rayhan=45, ryo=80)

#total_donations = 0

#for donations in donations.values():
    #print(f"the amount of donation we get is {total_donations}")
    #total_donations += donations

total_donation = sum(donations for donations in donations.values())
print(total_donation)

