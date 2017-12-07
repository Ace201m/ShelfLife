from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login


class FormView(View):
    form_class = UserForm
    template_name = 'form-login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('basic:index')
        else:
            return render(request, 'form-login.html', {'message': "Either username or password is not valid"})


class SignUp(View):
    form_class = UserForm
    template_name = 'form-register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        again = request.POST['again']

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if again != password:
                return render(request, 'form-register.html', {'message': "password fields don't match"})

            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('basic:adddetails')
                else:
                    return render(request, 'form-register.html', {'message': "user not active"})
            else:
                return render(request, 'form-register.html', {'message': "user is not authenticated"})
        else:
            return render(request, 'form-register.html', {'message': "username already exist"})
