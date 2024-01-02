'''Write a program using functions that counts the area and perimeter of circle and rectangle.'''

#Solution:

#defining function for area of circle
def area_circle(r):
    return 3.14 * (r**2)

#defining function for perimeter of circle
def perimeter_circle(r):
    return 2 * 3.14 * r

#defining function for area of rectangle
def area_rect(l,b):
    return (l * b)

#defining function for perimeter of rectangle
def perimeter_rect(l,b):
    return (2 * (l + b))

#taking inputs through input menu from users
polygon=''
while (polygon!='exit'):
    print('\nPOLYGONS:\ncircle\nrectangle\nexit')
    polygon=input('\nchoose the polygon or exit: ')
    property=''
    if (polygon=='exit'):
        break
    elif (polygon=='circle'):
        radius=float(input(('Enter the radius of cicle: ')))
        while (property==''):
            print('\nPROPERTY:\narea\nperimeter\nexit')
            property=input('\nchoose the property of circle or go back: ')
            if (property=='area'):
                r=area_circle(radius)
                print('Area of circle is',r,'sq.units')
                property=''
            elif (property=='perimeter'):
                p=perimeter_circle(radius)
                print('Perimeter of circle is',p,'sq.units')
                property=''
            elif (property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property=''
    elif (polygon=='rectangle'):
        l=float(input(('Enter the length of rectangle: ')))
        b=float(input(('Enter the breadth of rectangle: ')))
        while (property==''):
            print('\nPROPERTY:\narea\nperimeter\nexit')
            property=input('\nchoose the property of rectangle or go back: ')
            if (property=='area'):
                ar=area_rect(l,b)
                print('Area of rectangle is',ar,'units')
                property=''
            elif (property=='perimeter'):
                pr=perimeter_rect(l,b)
                print('Perimeter of rectangle is',pr,'units')
                property=''
            elif (property=='back'):
                break
            else:
                print('Please select the correct polygon property')
                property=''
    else:
        print('Choose the correct polygon type or exit')

#-------------------------------------------------------------------------------------------#
