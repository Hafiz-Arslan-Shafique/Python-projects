##   ATM machines allow 4 or 6 digit PIN codes and
##   PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
##   If the function is passed a valid PIN string, return true, else return false.


##   "1234"   -->  true
##   "12345"  -->  false
##   "a234"   -->  false





passw="12#441"
if len(passw)!=4 and len(passw)!=6:
    print("false")
else:
    if passw.isdigit():
        print("true")
    else:
        print("false")
        

