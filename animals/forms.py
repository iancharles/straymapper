from datetime import date

from django import forms


class AnimalSearchForm(forms.Form):
    animal_type_choices = (
        ('', 'All'),
        ('CAT', 'Cat'),
        ('DOG', 'Dog'),
    )
    animal_type = forms.ChoiceField(required=False,
        choices=animal_type_choices,
        widget=forms.Select(attrs={'class': 'span2'}))
    sex_choices = (
        ('', 'Any'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = forms.ChoiceField(required=False, choices=sex_choices,
        widget=forms.Select(attrs={'class': 'span2'}))
    intake_date = forms.DateField(required=False)
    intake_condition_choices = (
        ('', 'All'),
        ('NORMAL', 'Normal'),
        ('INJURED', 'Injured'),
        ('NURSING', 'Nursing'),
        ('FERAL', 'Feral'),
        ('AGED', 'Aged'),
        ('SICK', 'Sick'),
        ('PREGNANT', 'Pregnant'),
        ('OTHER', 'Other'),
    )
    intake_condition = forms.ChoiceField(required=False,
        choices=intake_condition_choices,
        widget=forms.Select(attrs={'class': 'span2'}))
