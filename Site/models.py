from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    AVALIACAO = [
        (0, '0'), 
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5')
    ]
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(max_length=8000)
    imagem = models.ImageField(upload_to='images/')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    avaliacao = models.IntegerField(choices=AVALIACAO)
    lancamento = models.BooleanField()
    destaque = models.BooleanField()

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    ESTADO_CIVIL = [
        ('SOL','Solteiro'),
        ('CAS','Casado'),
        ('DIV','Divorciado'),
        ('VIU','Viúvo')
    ]
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=120)
    endereco = models.CharField(max_length=250, verbose_name="Endereço")
    nro = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    estado_civil = models.CharField(max_length=3, choices=ESTADO_CIVIL)

    def __str__(self):
        return self.nome