from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from harddrives.models import File, Harddrive, Owner, History
from django import forms
from myform import FileForm, HarddriveForm, CheckoutForm
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import datetime
import pdb

def homepage(request, template_name):
    return render(request, template_name)

def findfile(request):
    if ( request.method == 'POST' ):
        form = FileForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_name = cd['name']
            return HttpResponseRedirect(reverse('testsite_detailfile',
                    kwargs = {'new_name':new_name}))
        else:
            form = FileForm()
            return render(request, 'harddrives/findfile.html',{
                'form':form,
                'error_message':"File not found"})
    else:
        form = FileForm()
    return render(request, 'harddrives/findfile.html', {'form':form})


def detailfile(request, new_name, template_name):
    file = File.objects.get(name=new_name)
    return render(request, template_name, {'file': file})

def historyfile(request, name, template_name):
    file = File.objects.get(name = name)
    return render(request, template_name, {'file': file})

def detailowner(request, name, template_name):
    owner = Owner.objects.get(name = name) 
    return render(request, template_name, {'owner': owner})

def historyowner(request, name, template_name):
    owner = Owner.objects.get(name = name)
    return render(request, template_name, {'owner': owner})

def detailharddrive(request, serial_num, template_name):
    harddrive = Harddrive.objects.get(serial_number=serial_num)
    return render(request, template_name, {'harddrive': harddrive})

def historyharddrive(request, serial_num, template_name):
    harddrive = Harddrive.objects.get(serial_number=serial_num)
    return render(request, template_name, {'harddrive': harddrive})

def addfile( request):
    if ( request.method == 'POST' ):
        form = FileForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            try:
                f = File.objects.get(name=new_name)
            except ObjectDoesNotExist:
                f = File(name=new_name)
                f.save()
            return HttpResponseRedirect(reverse('testsite_addharddrive',
                   kwargs = {'file_name' : new_name}))
        else:
            return HttpResponseRedirect(reverse('testsite_homepage'))
    else:
        form = FileForm()
        return render(request, 'harddrives/addfile.html', {'form':form})

def addharddrive( request , file_name ):
    if ( request.method == 'POST' ):
        form = HarddriveForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            harddrive_num = cd['serial_number']
            if ( cd['box'] is not None ):
                newowner = cd['box']
            elif ( cd['person'] is not None ):
                newowner = cd['person']
            try:
                h = Harddrive.objects.get(serial_number=harddrive_num)
            except ObjectDoesNotExist:
                h = Harddrive(serial_number=cd['serial_number'],
                              startup_date = datetime.datetime.now(),
                              owner = newowner,
                              file = File.objects.get(name = file_name))
                h.save()
            return HttpResponseRedirect(reverse('testsite_detailfile', 
                kwargs = { 'new_name' : file_name }))
        else:
            return HttpResponseRedirect(reverse('testsite_addharddrive',
                kwargs = { 'file_name' : file_name }))
    else:
        form = HarddriveForm()
        return render(request, 'harddrives/addharddrive.html', {
            'form':form,
            'file_name':file_name})

def checkout(request, template_name):
    if ( request.method == 'POST' ):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if ( cd['box'] is not None ):
                owner = cd['box']
            elif ( cd['person'] is not None ):
                owner = cd['person']
            hd = Harddrive.objects.get(serial_number=cd['serial_number'])
            h = History(
                        date = datetime.datetime.now(),
                        newowner = owner,
                        oldowner = hd.owner,
                        harddrive = hd)
            h.save()
            hd.owner=owner
            hd.save()
            return HttpResponseRedirect(reverse('testsite_detailfile',
                kwargs = { 'new_name' : hd.file.name }))
        else:
            form = CheckoutForm()
            return render(request, template_name,{
                'form':form,
                'error_message':"Either checkout or checkin"});
    else:
        form = CheckoutForm()
        return render(request, template_name, {'form' : form})
