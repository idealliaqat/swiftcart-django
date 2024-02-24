from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "username", "last_login", "date_joined", "is_active")
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    #filter_horizontal = ()
    #list_filter = ()
    #fieldsets = ()


admin.site.register(Account, AccountAdmin)
'''
from django import forms
from django.contrib import admin
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Account
from django.forms import Media
from django.templatetags.static import static

class MyModelAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget = PhoneNumberPrefixWidget(attrs={'class': 'phone-prefix'})
        # You might need to adjust the CSS class and other attributes as needed.


class MyModelAdmin(admin.ModelAdmin):
    form = MyModelAdminForm

    class Media:
        css = {
            'all': (
                static('https://www.jqueryscript.net/demo/jQuery-International-Telephone-Input-With-Flags-Dial-Codes/build/css/intlTelInput.css?v2022'),
            )
        }
        js = (
            static('https://code.jquery.com/jquery-latest.min.js'),
            static('https://www.jqueryscript.net/demo/jQuery-International-Telephone-Input-With-Flags-Dial-Codes/build/js/intlTelInput-jquery.min.js?v2022'),

        )


admin.site.register(Account, MyModelAdmin)
'''
