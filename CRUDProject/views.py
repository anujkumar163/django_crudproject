from django.shortcuts import render, redirect
from .models import Customer

def customers(request):
	if request.method == "POST":
		name = request.POST['nm']
		age = request.POST['age']
		add = request.POST['addr']
		pin = request.POST['pin']
		mob = request.POST['mob']

		c = Customer(name=name, age=age, address=add, pincode=pin, mobile=mob)
		c.save()
		return redirect('/customers/')
	else:
		cobjs = Customer.objects.all()
		return render(request, "index.html", {'cobjs': cobjs})

def delcustomer(request, id):
	cobj = Customer.objects.get(id=id)
	cobj.delete()
	return redirect('/customers/')

def updatecust(request, id):
	if request.method == 'POST':
		nm = request.POST['nm']
		age = request.POST['age']
		a = request.POST['addr']
		p = request.POST['pin']
		m = request.POST['mob']

		cobj = Customer.objects.filter(id=id)#QuerySet
		cobj.update(name=nm, age=age, address=a, pincode=p, mobile=m)

		return redirect('/customers/')

	else:	
		c = Customer.objects.get(id=id)
		return render(request, "updatecustomer.html",{'data': c})

	