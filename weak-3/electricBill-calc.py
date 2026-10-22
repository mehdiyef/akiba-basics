print("================== Date-Free Electricity Bill Calculator===============")

def validate_units(unit):
    if type(unit) != str or unit < 0 or unit == "":
        return True


def calculate_charge(units):
    low_coast=0
    medium_coast=0
    high_coast=0
    total_charge = 0

    low_coast = 50 * 0.5
    units-=50
    if units > 0:
        medium_coast = 100 * 0.75
        units-=100

    if units > 0:
        high_coast = units * 1.20

    return low_coast, medium_coast, high_coast

def calculate_total_charge(units, service_fee=18.20):
    if not validate_units(units):
        print(type(units))
        return units


    values = calculate_charge(units)
    total_charge =0
    for value in values:
        total_charge += value
    return total_charge+service_fee

def generate_bill_summary():
    unit= int(input("Enter the unit number: "))

    value = calculate_total_charge(unit)

    if type(value)!=str:
        print("Unit used:", "service fee", "coast", sep="              ")
        print(unit, "18.20", value, sep="                       ")

    else:
        print(value, "is a string uitn")

    print("--------------------------------------------------------------------")
generate_bill_summary()
# print(calculate_total_charge(123))