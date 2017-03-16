from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import reverse
from rest_framework import viewsets
from accounts.serializers import GroupSerializer, MemberSerializer
from accounts.models import Member
from accounts.forms import MemberRegistration
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == 'GET':
        form = MemberRegistration()
        context = {'form': form}
        return render(request, 'site.html', context)

    elif request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            authlogin(request, user)
            return redirect('/app')  # entrance door to app - redirect
            # Redirect to a success page.

        else:
            return redirect('/')

            # Return an 'invalid login' error message.


def registration(request):
    if request.method == 'POST':
        #TODO; handle errors

        form = MemberRegistration(data=request.POST)

        if form.is_valid():

            # import pdb; pdb.set_trace()
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone = request.POST['phone']

            member = Member.objects.create_user('username', 'password1')

            messages.success(request, message="Account Created Successfully, Please Login!")
            return redirect(reverse('login'))

        else:
            context = {'form': form}
            return render(request, 'site.html', context)

        # Return an 'invalid login' error message.


def forgot_password(request):
    if request.method == 'GET':

        form = MemberForgotPassword()

    elif request.method == 'POST':

        form = MemberForgotPassword(data=request.POST)

        if form.is_valid():
            change_password = form.save(commit=False)
            change_password.save()

    context = {'form': form}

    return render(request, 'forgot_page.html', context)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
