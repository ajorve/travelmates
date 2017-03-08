from django.shortcuts import render
from accounts.forms import MemberForm

# Create your views here.


def register(request):

    if request.method == 'GET':

        form = MemberForm()

    elif request.method == 'POST':

        form = MemberForm(data=request.POST)

        if form.is_valid():
            register = form.save(commit=False)
            register.save()

    context = {'form': form}

    return render(request, 'login_page.html', context)