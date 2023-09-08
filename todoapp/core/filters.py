from django_filters import FilterSet, DateFilter, NumberFilter, CharFilter
from django import forms
from .models import ToDo


class ToDoFilter(FilterSet):
    start_date = DateFilter('start_date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = DateFilter('end_date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    start_year__gt = NumberFilter(field_name='start_date', lookup_expr='year__gt')
    start_year__lt = NumberFilter(field_name='start_date', lookup_expr='year__lt')

    class Meta:
        model = ToDo
        exclude = ['user']
        # fields = ("todo_type", "title", "start_date_year", "end_date_year", "description")
