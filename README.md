# CLASE_21_PYTHON
Entregable1Leon_EntregableClase21
# En el proyecto tenemos tres models: Cliente, Vendedor y Producto.
Existe un template para models y para sus respectivos formularios, adicional se encuentran los template de busqueda y resultado.

Estas son las urls para realizar los llamados:
urlpatterns = [
    path('cliente/', crearCliente, name="cliente"),
    path('vendedor/', crearVendedor, name="vendedor"),
    path('producto/', crearProducto, name="producto"),
    path('', inicio, name="inicio"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('vendedorFormulario/', vendedorFormulario, name="vendedorFormulario"),
    path('productoFormulario/', productoFormulario, name="productoFormulario"),
    path('busquedaNombre/', busquedaNombre, name="busquedaNombre"),
    path('buscar/', buscar, name="buscar"),
    
    
