from django.shortcuts import render, redirect
from .models import Do
# Create your views here.

def index(request):

    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        docs = request.POST.get('docs')
        status = request.POST.get('status')

        Do.objects.create(title=title, time=time, docs=docs, status=status)

        return redirect('/')

    data = {
        'does': Do.objects.all()
    }

    return render(request, 'todo.html',data)


def delete(request, id):

    Do.objects.get(id=id).delete()

    return redirect('/')

def edit(request, id):
    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        docs = request.POST.get('docs')
        status = request.POST.get('status')
        Do.objects.filter(id=id).update(title=title, time=time, docs=docs, status=status)

        return redirect('/')

    data = {
            'todo': Do.objects.get(id=id)
        }

    return render(request, 'edit.html', data)
