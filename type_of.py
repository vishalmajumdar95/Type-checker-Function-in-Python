
def type_of(elem):
    try:
        elem+'h'
        print("< class - 'str' >")
        return 'str'
    except TypeError as err:
        z=str(err)
        if 'list' in z:
            print("< class - 'list' > ") 
            return 'list'
        elif 'tuple' in z:
            print("< class - 'tuple' > ") 
            return 'tuple'

        else:
            z=(z.split(':')[1]).split('and')[0]
            print(f"< class - {z} >")
            return z
d={"Name"}
x=type_of(d)
print(x)
