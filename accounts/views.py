from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .decorators import unauthenticated_user, allowed_users, admin_only, admin_and_manager_only
from django.contrib.auth.models import Group


# Create your views here.
# def get_notifications(request):
#     message = Message.objects.filter(Q(seen=False, receiver=request.user))
#     return message

# @unauthenticated_user

@admin_only
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            us = form.save()
            if us.is_superuser and us.is_staff:
             group = Group.objects.get(name='medecins')
             us.groups.add(group)
             profile=Profile.objects.get(id=us.id)
             print(Profile)
             profile.manager=int(request.user.pk)
             profile.save()
            if us.is_staff and us.is_superuser == False:
             group = Group.objects.get(name='techniciens')
             us.groups.add(group)
             profile=Profile.objects.get(id=us.id)
             print(Profile)
             profile.manager=int(request.user.pk)
             profile.save()
            else:
             group = Group.objects.get(name='secretaires')
             us.groups.add(group)
             profile=Profile.objects.get(id=us.id)
             profile.manager=int(request.user.pk)
             profile.save()
            messages.success(
                request, f"Felicitation utilisateur bien ajoute f'{us.username}")

            return redirect('accounts:table_users')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
           


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})


def logoutUser(request):
    logout(request)
    return redirect('patient:home')


    
   
        



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

# @login_required(login_url='accounts/login')
# @admin_and_manager_only 
def tableuser(request):
    # message = get_notifications(request)
    profile = Profile.objects.all()
    user = User.objects.all()

    # n= Equipement.objects.all().count|sub-Installation.objects.all().count


    context={

        'profile': profile,
        'user': user,
        # 'message': message

    }
    return render(request,'accounts/table_user.html',context)