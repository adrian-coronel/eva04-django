from django.shortcuts import render

# Create your views here.
def showForm(request):
  return render(request, 'Form.html')

def calculate(request):
  hours = int(request.POST['hours'])
  pay = int(request.POST['pay'])
  childrens = int(request.POST['childrens'])
  
  hourly = 0
  if hours <= 48:
    hourly = pay * hours
  else:
    hourly = pay * 48 + pay * (hours - 48) * 2

  bonus = childrens * 50
  descuento = hourly * 8 / 100 

  context = {
    'hourly': hourly - descuento + bonus
  }
  return render(request, 'Resultado.html', context= context)