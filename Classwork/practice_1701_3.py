'''
def test(a=33,b=55,c=45,d=56):
    print("A = ",a,"B = ",b,"C = ",c,"D = ",d)

test(b=768,d=748448)
'''
def test(a,b,c,*d,**e):
    print("A = ",a,"B = ",b,"C = ",c,"D = ",list(d),"E = ",e)

test(10,20,30,40,50,60,70,80,x=65,y=625,z=87)

