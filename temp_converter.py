x = raw_input("Enter a temperature in celsius: ")
try: 
    tc = float(x)
    tf = (tc * 9 / 5) + 32
    tf = str(tf)
    tc = str(tc)
except:
    print 'Enter a numeric value'
    quit()
z = " degrees Celsius is "
y = " degrees Fahrenheit"
print tc + z + tf + y
