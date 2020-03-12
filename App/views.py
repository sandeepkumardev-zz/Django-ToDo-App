from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from App.models import ToDo

# Create your views here.


def home(request):
    all_items = ToDo.objects.all().order_by('-added_date')
    return render(request, 'App/index.html', {'todo_items': all_items})


@csrf_exempt
def add_item(request):
    added_date = timezone.now()
    content = request.POST["text"]
    print(added_date, content)
    todo = ToDo(added_date=added_date, text=content)
    todo.save()
    return redirect('/')


@csrf_exempt
def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect('/')
