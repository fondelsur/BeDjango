from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notes
from .forms import NotesForm


def index(request):
    list_of_notes = Notes.objects.all()
    html_output = "<table border=true><tr><th>Title</th><th>Body</th></tr>"
    for note in list_of_notes:
        html_output += "<tr>"
        html_output += "<td>"+note.title+"</td><td>"+note.body+"</td>"
        html_output += "</tr>"
    html_output += "</table>"
    return HttpResponse(html_output)


def create(request):
    form = NotesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000')
        else:
            return HttpResponse('Error')
    context = {'form': form}
    return render(request, 'notes/creation_template.html', context)
