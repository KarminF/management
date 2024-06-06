from django.shortcuts import render, redirect

from app1 import models


def departments_list(request):
    return render(request, "departments_list.html", {'departments': models.Department.objects.all()})


def departments_add(request):
    if request.method == "GET":
        return render(request, "departments_add.html")

    depart = request.POST.get("depart")
    models.Department.objects.create(name=depart)
    return render(request, "departments_add.html", {'message': 'successfully added'})


def departments_delete(request):
    id = request.GET.get("id")
    models.Department.objects.filter(id=id).delete()
    return redirect(departments_list)


def departments_edit(request, id):
    if request.method == "GET":
        obj = models.Department.objects.filter(id=id).first()
        return render(request, "departments_edit.html", {'name': obj.name})

    depart = request.POST.get("depart")
    models.Department.objects.filter(id=id).update(name=depart)
    return redirect(departments_list)


