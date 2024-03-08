from django.shortcuts import render

def weekdays_list(request):
    weekdays1 = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
    weekdays2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays3 = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return render(request, 'weekdays/weekdays_list.html', {'weekdays1': weekdays1, 'weekdays2': weekdays2, 'weekdays3': weekdays3})

def weekdays_uz_list(request):
    weekdays = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
    return render(request, 'weekdays/uz_weekdays_list.html', {'weekdays': weekdays})

def weekdays_en_list(request):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render(request, 'weekdays/en_weekdays_list.html', {'weekdays': weekdays})

def weekdays_ru_list(request):
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return render(request, 'weekdays/ru_weekdays_list.html', {'weekdays': weekdays})