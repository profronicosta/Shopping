from django import forms
from Site.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'class':'cpf'}),
            'cep': forms.TextInput(attrs={'class':'cep'}),
            'data_nascimento': forms.TextInput(attrs={'class':'date'})
        }

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField()

    class Meta:
        widgets = {
            'telefone': forms.TextInput(attrs=
                                {'class':'phone_with_ddd'}),
            'mensagem': forms.Textarea
        }