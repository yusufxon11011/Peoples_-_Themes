from django.shortcuts import render
import os

def themes_list(request):
    app_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(app_path, 'lessons.txt')
    themes = []
    with open(file_path, 'r') as file:
        for line in file:
            themes.append(line.strip())
    return render(request, 'themes/themes_list.html', {'themes': themes})
