from django.db import models

#Tabla Animal
class Animal(models.Model):
    ID = models.CharField(max_length=8, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=20)
    Sexo = models.CharField(max_length=20)
    Raza = models.CharField(max_length=50)
    Edad = models.CharField(max_length=20)
    Birth = models.DateTimeField(auto_now_add=True)
    Location = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Salud = models.TextField()
    Foto1 = models.ImageField()
    Foto2 = models.ImageField()
    Foto3 = models.ImageField()
    Foto4 = models.ImageField()
    Status = models.CharField(max_length=20)

#"str" se utiliza para devolver una representación en cadena del objeto.
# En este caso, estamos devolviendo el nombre del animal.

#"Self" es una variable que hace referencia al objeto actual en el que se 
# está trabajando dentro de una clase o método. 
def __str__(self):
    return self.Nombre # Devuelve el nombre del animal

class Form_Info_Animal(models.Model):
    ID_Animal = models.ForeignKey('Animal', to_field='ID', on_delete=models.PROTECT)
    Nombre_Animal = models.CharField(max_length=50)
    Nombre_Cliente = models.CharField(max_length=60)
    Apellido_Cliente = models.CharField(max_length=60)
    Email = models.CharField(max_length=60)
    Asunto = models.CharField(max_length=30)
    Mensaje = models.TextField()

    def __str__(self):
        return f"{self.Nombre_Cliente} {self.Apellido_Cliente}" # Devuelve el nombre completo del cliente

class Form_Contact(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=60)
    Apellido = models.CharField(max_length=60)
    Email = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=10)
    HorarioParaContactar = models.DateTimeField(blank=True, null=True)
    Mensaje = models.TextField()

    def __str__(self):
        return self.Nombre # Devuelve el nombre de la persona que contactó

class Form_Donacion(models.Model):
    ID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=100)
    Email2 = models.EmailField(max_length=60)
    Telefono2 = models.CharField(max_length=10)
    Monto =  models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
            return f'{self.FullName} - {self.Monto}'# Devuelve el nombre completo de la persona que realizó la donación

class Datos_Adoptante(models.Model):
    ID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=100)
    Cedula = models.CharField(max_length=11)
    Direccion = models.CharField(max_length=120)
    Sector = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    Email = models.EmailField(max_length=60)
    Telefono = models.CharField(max_length=10)
    Animal_Adoptado = models.ForeignKey('Animal', to_field='ID', on_delete=models.PROTECT)

    def __str__(self):
        return self.FullName # Devuelve el nombre completo del adoptante

class Info_Personal(models.Model):
    ID = models.AutoField(primary_key=True)
    Pregunta1 = models.CharField(max_length=150)
    Pregunta2Si_No = models.CharField(max_length=2)
    Pregunta2 = models.CharField(max_length=150)
    Pregunta3 = models.CharField(max_length=150)
    Pregunta4Si_No = models.CharField(max_length=2)
    Pregunta4 = models.CharField(max_length=150)
    Pregunta5 = models.CharField(max_length=150)

    def __str__(self):
        return f"ID:{self.ID}" # Devuelve el ID del registro de información personal

class Info_Hogar(models.Model):
    ID = models.AutoField(primary_key=True)
    Pregunta1 = models.IntegerField()
    Pregunta2Si_No = models.CharField(max_length=2)
    Pregunta3Si_No = models.CharField(max_length=2)
    Pregunta4Si_No = models.CharField(max_length=2)
    Pregunta4 = models.CharField(max_length=150)
    Pregunta5 = models.CharField(max_length=150)
    Pregunta6 = models.CharField(max_length=150)
    Pregunta7Si_No = models.CharField(max_length=2)
    Pregunta8 = models.CharField(max_length=150)
    Pregunta9 = models.CharField(max_length=150)
    Pregunta10Si_No = models.CharField(max_length=2)
    Pregunta10 = models.CharField(max_length=150)

    def __str__(self):
        return f"ID:{self.ID}" # Devuelve el ID del registro de información del hogar

class Exp_Mascotas(models.Model):
    ID = models.AutoField(primary_key=True)
    Pregunta1Si_No = models.CharField(max_length=2)
    Pregunta2 = models.CharField(max_length=150)
    Pregunta3 = models.DecimalField(max_digits=8, decimal_places=2)
    Pregunta4 = models.CharField(max_length=150)
    Pregunta5Si_No = models.CharField(max_length=2)
    Pregunta5 = models.DecimalField(max_digits=8, decimal_places=2)
    Pregunta6Si_No = models.CharField(max_length=2)
    Pregunta6VETERINARIO = models.CharField(max_length=150)
    Pregunta6VETERINARIO_TEL = models.CharField(max_length=11)
    Pregunta7Si_No = models.CharField(max_length=2)
    Pregunta7 = models.CharField(max_length=150)

    def __str__(self):
        return f"ID:{self.ID}" # Devuelve el ID del registro de experiencia con mascotas

class Futuro_Mascota(models.Model):
    ID = models.AutoField(primary_key=True)
    Pregunta1 = models.CharField(max_length=150)
    Pregunta2 = models.CharField(max_length=150)
    Pregunta3 = models.CharField(max_length=150)

    def __str__(self):
        return f"ID:{self.ID}" # Devuelve el ID del registro de información sobre el form anterior

class Form_Adop(models.Model):
    ID = models.AutoField(primary_key=True)
    ID_Adoptante = models.ForeignKey(Datos_Adoptante, on_delete=models.CASCADE, related_name='form_adop_id_adoptante')    
    ID_INFOPERSONAL = models.ForeignKey('Info_Personal',to_field='ID', on_delete=models.PROTECT)
    ID_INFOHOGAR = models.ForeignKey('Info_Hogar',to_field='ID', on_delete=models.PROTECT)
    ID_EXP = models.ForeignKey('Exp_Mascotas',to_field='ID', on_delete=models.PROTECT)
    ID_FUTUROMASCOTA = models.ForeignKey('Futuro_Mascota',to_field='ID', on_delete=models.PROTECT)

    def __str__(self):
        return f"ID:{self.ID}" # Devuelve el ID del registro de formulario de adopción