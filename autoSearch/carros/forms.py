from django import forms

from .models import Car




class CarModelForm(forms.ModelForm):
    make = forms.CharField(label='',
                              widget=forms.Textarea(
                                        attrs={'placeholder':"Car",
                                               'class': "textarea"}
))
    class Meta:
        model = Car
        fields = [
            "make", "types", "year", "colour", "price"
]
