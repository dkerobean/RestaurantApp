from django.forms import ModelForm
from .models import Food, FoodType, Category
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FoodForm(ModelForm):
    class Meta:
        model = Food 
        fields = '__all__'
        exclude =  ['created_at']
        
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control '})

            self.fields["name"].widget.attrs.update(
                {'class': 'form-control'})
            
            
            
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
           
            
class FoodTypeForm(ModelForm):
    class Meta:
        model = FoodType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
            
            
class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control' 
            
class createUserForm(ModelForm):
    class Meta:
        model = User 
        fields = 'username', 'first_name','last_name', 'email', 'password', 'groups'
        #exclude = ['last_login', 'is_superuser', 'user_permissions', 'is_active', 'is_staff', 'date_joined']
        labels = {
            "groups": "User Permission"
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    
    
    
