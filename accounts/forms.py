from django import forms
from accounts.models import Member


class MemberForm(forms.ModelForm):
    """For CRUDing Users"""

    class Meta:
        model = Member
        fields = ('username', 'password', 'repeat_password', 'email')
