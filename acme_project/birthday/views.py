from django.shortcuts import render

from .forms import BirthdayForm


def birthday(request):
    print(request.GET)
    form = BirthdayForm()
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)
