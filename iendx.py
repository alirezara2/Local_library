import p1.Local_library.FuFile as FuFile

# من از درون فایل دیگری فانکشن ها رو صدا زدم و در اینجا به کار گرفتم


a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))
c = input("emaliat mord nazar vard konid , * - + / :")

if c == "*":
    x = FuFile.zarb(a,b)
elif c == "/":
    x = FuFile.taghsem(a,b)
elif c == "+":
    x = FuFile.jam(a,b)
elif c == "-":
    x = FuFile.maines(a,b)

print(x)