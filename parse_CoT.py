from config_lists import LIST_OF_CONTRACTS, DATE, LIST_OF_COLUMNS

# YYMMDD
def date_greater_than(date_one, date_two):

    date_one = date_one.strip(f'"').strip(" ")
    date_two = date_two.strip(f'"').strip(" ")

    # parse dates
    date_one_year = int(date_one[:1])
    date_one_month = int(date_one[2:3])
    date_one_day = int(date_one[4:])

    date_two_year = int(date_two[:1])
    date_two_month = int(date_two[2:3])
    date_two_day = int(date_two[4:])

    # only works for year 2000 or greater
    if date_one_year > date_two_year:
        return True

    if date_one_year == date_two_year:
        if date_one_month > date_two_month:
            return True

        if date_one_month == date_two_month:
            if date_one_day > date_two_day:
                return True

    return False


list_of_important_rows = list()
sum_of_change_in_OI = 0
with open("c_year.txt", "r") as cot_file:
    for line in cot_file:
        # if date is greater than date we want AND
        # if contract is in our list of contracts AND
        # if contract is in standard form (2500 MMBtus)
        split_line = line.split(",")
        if split_line[0].strip(f'"') in LIST_OF_CONTRACTS:
            if date_greater_than(split_line[1], DATE):
                if split_line[185] == '"2500 MMBtus"':
                    list_of_important_rows.append(split_line)
                    sum_of_change_in_OI += abs(float(split_line[55]))

    print(f"contracts: {sum_of_change_in_OI}")
    print(f"mmbtus: {sum_of_change_in_OI*2500}")
