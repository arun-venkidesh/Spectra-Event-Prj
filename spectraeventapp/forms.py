from django import forms # type: ignore
from spectraeventapp.models import Register, EventRegistration


class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['Name', 'Email', 'PhoneNumber', 'Password']
            
class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=EventRegistration
        fields=['Name', 'Email', 'PhoneNumber', 'Category','EventType', 'Date_and_Time', 'Message']
        widgets = {
            'Date_and_Time':forms.TextInput(attrs={'type':'datetime-local'}),
        }

        