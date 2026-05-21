# 1. MATRIZ DEL MENU ( 6 productos de diversas categorias)
# Estructura: [Nombre del producto, categoria, Precio Base]
menu_restaurante = [
    ["Hamburguesa Gourmet", "Comidas Rapidas", 25000],
    ["Papas Nativas", "Entradas", 8000],
    ["Pizza Familiar", "Comidas Rapidas", 35000],
    ["Limonada de coco", "Bebidas", 7000],
    ["Lasaña de Pollo", "Platos Fuertes", 16000],
    ["Copa de Helado", "Postres", 6000]
]

# 2. Modulo funcion para calcular el precio final
def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    if categoria_producto == categoria_objetivo and precio_base > umbral_precio:
        return precio_base * 0.85  # Retorna directamente el 85% del valor original
    else:
        return precio_base

# 3. Configuracion de la promocion (logica de negocio)
# Definimos la categoria a la que queremos aplicar la promo y desde que valor
CATEGORIA_PROMO = "Comidas Rapidas"
UMBRAL_PROMO = 20000

# 4. Salida y procesamiento de datos
print("="* 65)
print(f"  REPORTE DE PRECIOS - PROMOCION PARA: {CATEGORIA_PROMO.upper()}")
print(f"  (descuento del 15% para productos con precio mayor a ${UMBRAL_PROMO:,})")
print("="* 65)
print(f"{'Producto':<22} | {'Categoria':<15} | {'Precio Base':<11} | {'Precio Final':<11}")
print("="* 65)

# Recorremos la matriz fila por fila
for producto in menu_restaurante:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    #llamamos al modulo para calcular el precio final de cada producto
    precio_final = calcular_precio_final(categoria, precio_base, CATEGORIA_PROMO, UMBRAL_PROMO)

    #mostramos los resultados alineados y con formato de miles
    print(f"{nombre:<22} | {categoria:<15} | ${precio_base:<10,} | ${precio_final:<10,.9f}")

print("=" *65)
    
