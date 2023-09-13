from django.shortcuts import render

def show_main(request):
    context = {
        'Name': 'Beginner Cue',
        'Force': 'very low',
        'Aim': 'very low',
        'Spin': 'very low',
        'Time': 'very low',
    }

    return render(request, 'main.html', context)