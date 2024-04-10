from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


from .models import Employer, JobSeeker


class EmployerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Employer
        fields = ('phone_number', 'username', 'email', 'is_active')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmployerChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employer
        fields = ('password', 'is_admin', 'is_active')


class EmployerAdmin(BaseUserAdmin):
    form = EmployerChangeForm
    add_form = EmployerCreationForm
    list_display = ('username', 'email', 'phone_number', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': (
            'password',
            'username',
            'phone_number',
            'email',
            )}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'phone_number',
                'password1',
                'password2'),
        }),
    )
    search_fields = ('phone_number', 'username', 'email')
    ordering = ('phone_number', )
    filter_horizontal = ()


class JobSeekerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = JobSeeker
        fields = ('phone_number', 'username', 'email', 'is_active')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class JobSeekerChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = JobSeeker
        fields = ('password', 'is_admin', 'is_active')


class JobSeekerAdmin(BaseUserAdmin):
    form = JobSeekerChangeForm
    add_form = JobSeekerCreationForm
    list_display = ('username', 'email', 'phone_number', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': (
            'password',
            'username',
            'phone_number',
            'email',
            )}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'phone_number',
                'password1',
                'password2'),
        }),
    )
    search_fields = ('phone_number', 'username', 'email')
    ordering = ('phone_number', )
    filter_horizontal = ()


admin.site.register(Employer, EmployerAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)
