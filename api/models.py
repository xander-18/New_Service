from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100 , unique=True)
    password = models.CharField(max_length=100) 
    active = models.BooleanField(default=True)
    
class Empresa(models.Model):
    nombre  = models.CharField(max_length=100)
    ruc = models.CharField(max_length=15 , unique=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    actividad = models.CharField(max_length=200)
    
class Empledo(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    dni  = models.CharField(max_length=15 , unique=True)
    sueldo = models.DecimalField(max_digits=10 , decimal_places=2)
    avatar = models.ImageField(null=True , upload_to='foto_employe')
    id_empresa = models.ForeignKey(Empresa , on_delete=models.CASCADE)

class Mesa(models.Model):
    qrcode = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=[
        ('ocupado', 'Ocupado'),
        ('Disponible', 'Disponible'),
    ])

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)            
              
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    id_mesa = models.ForeignKey(Mesa , on_delete=models.CASCADE)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    imagen = models.ImageField(null=True , upload_to='product')
    descripcion = models.TextField()
    id_categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    
class Caja(models.Model):
    id_producto = models.ForeignKey(Producto , on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10 , decimal_places=2)
    estado = models.BooleanField(max_length=50  , default='pendiente')
    fecha = models.DateTimeField()
    metodo_pago = models.CharField(max_length=50, choices=[
        ('efectivo', 'Efectivo'), 
        ('tarjeta', 'Tarjeta'), 
        ('QR', 'QR')
    ])

class Pedido(models.Model):
    id_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('preparando', 'Preparando'),
        ('servido', 'Servido'),
        ('pagado', 'Pagado')
    ])
    total = models.DecimalField(max_digits=8, decimal_places=2)
    pagado = models.BooleanField(default=False)
    
class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(max_digits=8 , decimal_places=2)

class HistorialPedido(models.Model):	
    id_pedido = models.ForeignKey(Pedido , on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado_anterior =models.CharField(max_length=100)
    estado_nuevo =models.CharField(max_length=100)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)