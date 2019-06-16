from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from my_contacts.models import *

def all_contacts(request):
    contacts = Person.objects.all().order_by("last_name")
    return render(request,"allcontacts.html",{
        'contacts': contacts
    })

def del_contact(request,to_delete):
    Person.objects.get(pk=to_delete).delete()
    return redirect('/')

def del_adress(request,id,to_delete):
    Adress.objects.get(pk=to_delete).delete()
    return redirect(f'../../show/{id}')

def del_email(request,id,to_delete):
    Email.objects.get(pk=to_delete).delete()
    return redirect(f'../../show/{id}')

def del_phone(request,id,to_delete):
    PhoneNumber.objects.get(pk=to_delete).delete()
    return redirect(f'../../show/{id}')

@csrf_exempt
def add_contact(request):
    if request.method == "POST":
        new_person = Person.objects.create(first_name=request.POST.get("first_name"),
                                           last_name=request.POST.get("last_name"),
                                           description=request.POST.get("description"))

        return redirect(f'../show/{new_person.id}')

    else:
        return render(request,"addcontact.html")

def show_by_id(request,id):
    person = Person.objects.get(pk=id)
    adress = Adress.objects.filter(person=id)
    email = Email.objects.filter(person=id)
    phone = PhoneNumber.objects.filter(person=id)

    return render(request, "contact.html", {
        'contact': person,
        'adress': adress,
        'email': email,
        'phone':phone
    })

@csrf_exempt
def modify_contact(request,id):
    if request.method == "POST":
        person = Person.objects.get(pk=id)
        person.first_name = request.POST.get("first_name")
        person.last_name = request.POST.get("last_name")
        person.description = request.POST.get("description")
        person.save()

        return redirect(f'../show/{id}')

    else:
        person = Person.objects.get(pk=id)
        return render(request,"modify.html",{
            'contact': person
        })

@csrf_exempt
def add_adress(request, id):
    person = Person.objects.get(pk=id)
    Adress.objects.create(city=request.POST.get("city"), street=request.POST.get("street"), street_no=request.POST.get("street_no"),
                          apartament_no=request.POST.get("apartament"), person=person)
    return redirect(f'../show/{id}')

@csrf_exempt
def add_email(request, id):
    person = Person.objects.get(pk=id)
    Email.objects.create(email=request.POST.get("email"), email_type=request.POST.get("email_type"), person=person)

    return redirect(f'../show/{id}')

@csrf_exempt
def add_phone(request, id):
    person = Person.objects.get(pk=id)
    PhoneNumber.objects.create(number=request.POST.get("number"), number_type=request.POST.get("number_type"), person=person)

    return redirect(f'../show/{id}')

def all_groups(request):
    groups = Group.objects.all().order_by("name")
    return render(request,"allgroups.html",{
        'groups': groups
    })

def del_group(request,to_delete):
    Group.objects.get(pk=to_delete).delete()
    return redirect('/groups')

@csrf_exempt
def add_group(request):
    if request.method == "POST":
        new_group = Group.objects.create(name=request.POST.get("group_name"))

        return redirect(f'../groups/show/{new_group.id}')

    else:
        return render(request,"addgroup.html")

def group_by_id(request,id):
    members = Person.objects.filter(group=id)
    group = Group.objects.get(pk=id)

    return render(request, "group.html", {
        'members': members,
        'group_id': id,
        'group': group
    })

def delete_from_group(request, group_id, person_id):
    group = Group.objects.get(pk=group_id)
    person = Person.objects.get(pk=person_id)
    person.group.remove(group)
    person.save()

    return redirect(f'../../../groups/show/{group_id}')

def add_members(request,group_id):
    if request.method == "GET":
        contacts = Person.objects.all().order_by("last_name")
        return render(request,"addmembers.html", {
            'group_id': group_id,
            'contacts': contacts,
        })
def add_member_to_group(request,person_id,group_id):
    person = Person.objects.get(pk=person_id)
    group = Group.objects.get(pk=group_id)
    person.group.add(group)
    person.save()

    return redirect(f'../../../groups/show/{group_id}')

