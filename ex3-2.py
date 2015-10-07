inp = raw_input("Enter Hours: ")
try:
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
except:
    print 'Error, please enter numeric input'
    quit()

if hours <= 40 :
    pay = hours * rate
elif hours > 40 :
    extra = (hours - 40) * 1.5 * rate
    basepay = 40 * rate
    pay = basepay + extra
print pay
