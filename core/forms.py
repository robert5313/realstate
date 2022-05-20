from django import forms

class CustomerRequestForm(forms.Form):
    phone_number = forms.CharField(max_length=50, label='Phone Number',  required=True, widget=forms.TextInput(attrs={
            "class": "w-full p-3 text-sm border-gray-200 rounded-lg",
            "placeholder": "Phone Number",
            "id":"phone_number"
    }))
    request = forms.CharField(max_length=300, label='Provide more information', required=True, widget=forms.Textarea(attrs={
            "class": "w-full p-3 text-sm border-gray-200 rounded-lg",
            "placeholder": "Provide more information",
            "rows": 6,
            "id":"request"
    }))
    email = forms.CharField(max_length=50, label='Email Address',  required=True, widget=forms.TextInput(attrs={
            "class": "w-full p-3 text-sm border-gray-200 rounded-lg",
            "placeholder": "Email",
            "id":"email"
    }))
    first_name = forms.CharField(max_length=50, label='First Name',  required=True, widget=forms.TextInput(attrs={
            "class": "w-full p-3 text-sm border-gray-200 rounded-lg",
            "placeholder": "First Name",
            "id":"first_name"
    }))
    last_name = forms.CharField(max_length=50, label='Last Name',  required=True, widget=forms.TextInput(attrs={
            "class": "w-full p-3 text-sm border-gray-200 rounded-lg",
            "placeholder": "Last Name",
            "id":"last_name"
    }))