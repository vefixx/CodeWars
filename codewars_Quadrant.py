#Первый квадрант, квадрант в правом верхнем углу, содержит все точки с положительными X и Y.
#Второй квадрант, квадрант в верхнем левом углу, содержит все точки с отрицательным X, но положительным Y.
#Третий квадрант, квадрант в нижнем левом углу, содержит все точки с отрицательными значениями X и Y.
#Четвертый квадрант, квадрант в правом нижнем углу, содержит все точки с положительным X, но отрицательным Y.

#1. + +
#2 - +
#3 - -
#4 + -

def Quadrant(x,y):
    x = x
    y = y
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
