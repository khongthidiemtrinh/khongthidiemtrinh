# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:22:38 2024

@author: diemtrinh
"""
a=float(input("Số thứ nhất:"))
b=float(input("Số thứ hai:"))
c=float(input("Số thứ ba:"))
if a==b==c:
    print("Đây là tam giác đều") 
elif a==b or a==c or b==c:
    print("Đây là tam giác cân")
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("Đây là tam giác vuông")