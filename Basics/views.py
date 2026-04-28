from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method == "POST":
        a = int(request.POST.get("txt_num1"))
        b = int(request.POST.get("txt_num2"))
        c = a + b
        return render(request,'Basics/Sum.html',{"result":c})
    else:
        return render(request,'Basics/Sum.html')



def Calculator(request):
    if request.method == "POST":
        num1 = int(request.POST.get("txt_num1"))
        num2= int(request.POST.get("txt_num2"))
        btn= request.POST.get("btn_submit")
        if btn == "+":
            sum= num1 + num2
        elif btn == "-":
            sum= num1 - num2
        elif btn == "*":
            sum= num1 * num2
        elif btn == "/":
            sum= num1 / num2
        return render(request,'Basics/Calculator.html',{"result":sum})
    else:
        return render(request,'Basics/Calculator.html')

def Largest(request):
    if request.method == "POST":
        num1 = int(request.POST.get("txt_num1"))
        num2 = int(request.POST.get("txt_num2"))
        num3 = int(request.POST.get("txt_num3"))
        if num1 > num2 and num1 > num3:
            result = num1
        elif num2>num1 and num2 > num3:
            result = num2
        else:
            result = num3
        return render(request, 'Basics/Largest.html', {"result": result})
    else:
        return render(request, 'Basics/Largest.html',)


