from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import SubstackUserCreation, SubstackAuthenticationForm, SubstackUpdateForm

# Create your views here.
def login_screen(request):
    user = request.user
    if user.is_authenticated:
        return redirect("articles:create")

    if request.method == "POST":
        form = SubstackAuthenticationForm(request.POST)
        print(form)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect("homepage")
    else:
        form = SubstackAuthenticationForm()
    return render(request, 'accounts/login_webpage.html', context = { 'form':form } )

def create_account(request):
    if request.method == 'POST':
        form = SubstackUserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:create')
    else:
        form = SubstackUserCreation()
    return render(request, 'accounts/create_account.html', context = { 'form': form } )

def account_management(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
   
    context = {}

    if request.POST:
        form = SubstackUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = SubstackUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['form'] = form
    return render(request, 'accounts/account.html', context=context)

def logout_view(request):
    if request.user:
        print('passed')
        logout(request)
        return redirect('accounts:login')
    else:
        print('failed')
        return
        

def send_to_login(request):
    return redirect('accounts:login')