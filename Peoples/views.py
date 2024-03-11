from django.shortcuts import render

def pupils_list(request):
    pupils = [
        {'id': 1, 'name': 'Inomjon Qurbonov', 'jami': 37},
        {'id': 2, 'name': 'Muhammadyusuf Abduvaliyev', 'jami': 36},
        {'id': 3, 'name': 'Shoxruhbek Turdaliyev', 'jami': 29},
        {'id': 4, 'name': 'Zafarbek Olimboyev', 'jami': 39},
        {'id': 5, 'name': 'Samariddin Baxtiyorov', 'jami': 37},
        {'id': 6, 'name': 'Ozodbek Axrorov', 'jami': 40},
        {'id': 7, 'name': 'Javohir Otaboyev', 'jami': 35},
        {'id': 8, 'name': 'Mubina Nusratullayeva', 'jami': 31},
        {'id': 9, 'name': 'Sunnatillo Sharipov', 'jami': 40},
        {'id': 10, 'name': 'Ruslan Mamatanov', 'jami': 35},
        {'id': 11, 'name': "Firdavs Jo'rayev", 'jami': 30},
        {'id': 12, 'name': "Javlonbek Jo'rayev", 'jami': 31},
        {'id': 13, 'name': 'Naziraxon Qodirova', 'jami': 31},
        {'id': 14, 'name': 'Arabboy Yunusov', 'jami': 36},
        {'id': 15, 'name': 'Fazilatxon Axmedova', 'jami': 36},
    ]
    return render(request, 'pupils/pupils_list.html', {'pupils': pupils})

def pupil_scores(request, id):
    scores = [
        {'id': 1, 'jami': 37},
        {'id': 2, 'jami': 36},
        {'id': 3, 'jami': 29},
        {'id': 4, 'jami': 39},
        {'id': 5, 'jami': 37},
        {'id': 6, 'jami': 40},
        {'id': 7, 'jami': 35},
        {'id': 8, 'jami': 31},
        {'id': 9, 'jami': 40},
        {'id': 10, 'jami': 35},
        {'id': 11, 'jami': 30},
        {'id': 12, 'jami': 31},
        {'id': 13, 'jami': 31},
        {'id': 14, 'jami': 36},
        {'id': 15, 'jami': 36},
    ]
    return render(request, 'pupils/pupil_scores.html', {'id': id, 'scores': scores})