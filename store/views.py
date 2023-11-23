from django.db import models
from django.forms import fields
from django.http import request
from django.shortcuts import redirect, render, resolve_url
from django.urls.base import reverse_lazy
from django.views.generic import View,CreateView,UpdateView,DeleteView,TemplateView, ListView, DetailView
from .models import Debt, Booking
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class Home(TemplateView):
    template_name = 'store/home.html'

class DebtList(LoginRequiredMixin, ListView):
    model = Debt
    template_name = 'store/debt_list.html'
    context_object_name = 'debts'

class DebtDetail(LoginRequiredMixin, DetailView):
    model = Debt

class DebtCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Debt
    fields = ['name', 'game', 'amount', 'paid', 'balance']
    success_message = "New debt record has been successfully created"

    def form_valid(self, form):
        form.instance.keeper = self.request.user
        return super().form_valid(form)

class DebtUpdate(LoginRequiredMixin, UserPassesTestMixin ,SuccessMessageMixin, UpdateView):
     model = Debt
     fields = ['name', 'amount', 'paid', 'balance']
     success_message = "Debt record has been successfully updated"

     def form_valid(self, form):
        form.instance.keeper = self.request.user
        return super().form_valid(form)

     def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.keeper:
            return True
        return False

class DebtDelete(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin, DeleteView):
    model = Debt
    success_url = '/'
    success_message = "Debt record has been successfully deleted"

    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.keeper:
            return True
        return False

class BookList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'store/book_list.html'
    context_object_name = 'books'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        total = Booking.objects.filter(booker=self.request.user).count()
        context["bookings"] = total
        return context

class AdminList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'store/admin.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["counter"] = Booking.objects.count()
        return context

class BookCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Booking
    fields = ['name', 'number', 'console', 'description']
    success_message = "successfully created"
    

    def form_valid(self, form):
        form.instance.booker = self.request.user
        return super().form_valid(form)

class BookDetail(LoginRequiredMixin, DetailView):
    model = Booking

class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Booking
    fields = ['name', 'number', 'console', 'description']
    success_message = "updated successfully"

    def form_valid(self, form):
        form.instance.booker = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.booker:
            return True
        return False

class BookDelete(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin,DeleteView):
    model = Booking
    success_url = reverse_lazy('book_list')
    success_message = "successfully deleted"

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.booker:
            return True 
        return False

def contact(request):
    if request.method == "POST":
        name = request.POST.get("from")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name, '/n', subject, '/n' ,message)
    
        return redirect('/')
    return render(request, "store/contact.html")

