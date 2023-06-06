from Site.models import Departamento

def listar_departamentos(request):
    departamentos = Departamento.objects.all()

    context = {
        'departamentos': departamentos
    }

    return context