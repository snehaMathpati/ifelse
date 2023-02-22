

ch=input("enter the cheractor:")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print("its alphabet")
elif ch=='@' or ch=='#' or ch=='&' or ch=='_':
    print("its special ch")
else:
    print("its digit")