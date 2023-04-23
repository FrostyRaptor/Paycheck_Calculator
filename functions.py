def noraml_pay(hours, hourly_pay):
    return hours * hourly_pay

def overtime(hours, hourly_pay):
    return hours * (hourly_pay * 1.5)

def total_week_pay(hours, hourly_pay, overtime_hours=0):
    if overtime_hours == 0:
        # User didn't get overtime
        return noraml_pay(hours, hourly_pay)
    else:
        overtime_hours = overtime_qual(hours)
        return overtime(overtime_hours, hourly_pay) + noraml_pay(40, hourly_pay)

def overtime_qual(hours):
    num = hours - 40
    if num > 0:
        # User made overtime and returns those hours
        return num 
    else:
        # User didn't make overtime and returns a negative number
        return num

def oasdi(total_pay):
    return total_pay * .062

def medicare(total_pay):
    return total_pay * .0145

def state_tax(total_pay):
    return total_pay * .0495

def total_tax(total_pay):
    return oasdi(total_pay) + medicare(total_pay) + state_tax(total_pay)