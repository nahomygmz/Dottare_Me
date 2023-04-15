from django.contrib import admin
from .models import Animal
from .models import Form_Info_Animal
from .models import Form_Contact
from .models import Form_Donacion
from .models import Datos_Adoptante
from .models import Info_Personal
from .models import Info_Hogar
from .models import Exp_Mascotas
from .models import Futuro_Mascota
from .models import Form_Adop

admin.site.register(Animal)
admin.site.register(Form_Info_Animal)
admin.site.register(Form_Contact)
admin.site.register(Form_Donacion)

#Formulario de adopción
admin.site.register(Datos_Adoptante)
admin.site.register(Info_Personal)
admin.site.register(Info_Hogar)
admin.site.register(Exp_Mascotas)
admin.site.register(Futuro_Mascota)
admin.site.register(Form_Adop)