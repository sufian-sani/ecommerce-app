from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponseForbidden,Http404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView, TemplateView, View, RedirectView
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

# Create your views here.
# class Signup(CreateView):
#     model = Customerprofile
#     # form_class = YourModelForm  # You can specify a form class if needed
#     fields = ["first_name"]
#     template_name = 'accounts/signup.html'
#     # success_url = reverse_lazy('success_url_name')
#     def form_valid(self, form):
#         import pdb;pdb.set_trace()
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)

# class Signup(FormView):
#     template_name = 'accounts/signup.html'
#     form_class = SignupForm
#     import pdb;pdb.set_trace()
#     print(form_class)
#     import pdb;pdb.set_trace()
    # fields = '__all__'
    # def post(self, request, *args, **kwargs):
    #     import pdb;pdb.set_trace()
    #     # if not request.user.is_authenticated:
    #     #     return HttpResponseForbidden()
    #     # self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)

class Signup(View):
    template_name = 'accounts/signup.html'
    # model = Customerprofile
    # # import pdb;pdb.set_trace()
    # fields = ['first_name',]
    def get(self, request):
        # print('get')
        # Render the form for a GET request
        return render(request, self.template_name)
    
    def post(self, request):
        # Process the form data for a POST request
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        city = request.POST.get('city')
        division = request.POST.get('division')
        zip = request.POST.get('zip')

        if password1 == password2:
            if email is not None or phone is not None:
                existing_user_email = User.objects.filter(email=email)
                existing_customerprofile_phone = Customerprofile.objects.filter(phone=phone)
                if existing_user_email.exists() or existing_customerprofile_phone.exists():
                    return HttpResponseForbidden('phone or email already saved')
                else:
                    username = '-'.join((phone if phone else '', email if email else '')).lstrip('-').rstrip('-')
                    user = User(username=username,first_name=first_name,last_name=last_name,email=email)
                    user.set_password(password1)
                    user.save()
                    user_profile = Customerprofile(user=user,phone=phone, address=address, city=city, division=division, zip=zip)
                    # user_profile.user.set_password(password1)
                    # user.save()
                    # import pdb;pdb.set_trace()
                    user_profile.save()
            else:
                return HttpResponseForbidden('phone or email missing')
        else:
            return HttpResponseForbidden('password not same')

        return redirect('home:home')
    


class Signin(View):
    template_name = 'accounts/signin.html'

    def get(self, request):
        # print('get')
        # Render the form for a GET request
        return render(request, self.template_name)
    
    def post(self, request):
        email_phone = request.POST.get('email_phone')
        password = request.POST.get('password')
        # import pdb;pdb.set_trace()
        # username = User.objects.filter(Q(email=email_phone) | Q(phone=email_phone) | Q(username=email_phone)).values_list('username', flat=True).first()
        # email = User.objects.get(email=email_phone)
        # phone = Customerprofile.objects.get(phone=email_phone)
        # if username:
        #     user = authenticate(username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('home:home')
        # else:
        #     return HttpResponseForbidden('Something Wrong')
        try:
            # print('try')
            # import pdb;pdb.set_trace()
            try:
                email = get_object_or_404(User, email=email_phone)
                user_profile_phone = get_object_or_404(Customerprofile, **dict(user=email.id)).phone
                email_address=email.email
                if user_profile_phone and email_address:
                    username=email.username
                    user = authenticate(username=username, password=password)
                    if user and user.is_active:
                        print('user',user)
                        login(self.request, user)
                        return redirect('home:home')
                    else:
                        return HttpResponseForbidden('pair doesn\'t match')
                # username = '-'.join((phone if phone else '', email if email else '')).lstrip('-').rstrip('-')
                # import pdb;pdb.set_trace()
                # email.Customerprofile
                # phone = Customerprofile.objects.get(phone=User.email)
            except Http404:
                # print('except')
                # import pdb;pdb.set_trace()
                phone = get_object_or_404(Customerprofile, phone=email_phone)
                user=get_object_or_404(User, username=phone.user)
                if phone.phone and user.email:
                    username=user.username
                    user = authenticate(username=username, password=password)
                    if user and user.is_active:
                        login(self.request, user)
                        return redirect('home:home')
                    else:
                        return HttpResponseForbidden('pair doesn\'t match')
                # import pdb;pdb.set_trace()
        except Http404:
            return HttpResponseForbidden('pair doesn\'t match')

class SignOutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/signin/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)




