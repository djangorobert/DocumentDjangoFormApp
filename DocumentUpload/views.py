# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from DocumentUpload.forms import DocumentForm
from DocumentUpload.models import Document
from django.shortcuts import render, redirect

# Create your views here.
def upload(request):
    all_files = Document.objects.all()
    total_files = Document.objects.count()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'DocumentUpload/upload.html', {
        'form': form,
        'all_files': all_files,
        'total_files': total_files,
    })

def home(request):
    templates = 'DocumentUpload/home.html'
    context = {}
    return render(request, templates, context)