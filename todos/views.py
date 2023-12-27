from django.shortcuts import render

def todo_list(request):
    #nome = "Tomás"
    #alunos= ["Ariel", "João", "Maria"]
    return render(request, "todos/todo_list.html")
