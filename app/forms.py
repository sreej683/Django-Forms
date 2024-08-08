from django import forms

c=[('MALE','male'),('FEMALE','female')]
j=[('PYTHON','python'),('DJANGO','django')]
class StudentForm(forms.Form):
    sid=forms.IntegerField(max_value=1)
    sname=forms.CharField(max_length=100)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    dob=forms.DateTimeField()
    surl=forms.URLField()
    gender=forms.ChoiceField(choices=c)
    #gender=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    subjects=forms.MultipleChoiceField(choices=j)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':5}))
