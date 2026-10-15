import streamlit as st  
from calculos import *
from pdf_presupuesto import armar_pdf as pdf
from mi_negocio import *

nombres = []
cantidades = []
precios_unitarios=[]
subtotal=[]
total=0
iva=0
cantidad=0

st.title(NOMBRE_NEGOCIO)
st.write(f"Rubro: {RUBRO}")

nombre= st.text_input("Ingrese su nombre")
RENGLONES = st.number_input("Ingrese la cantidad de productos a presupuestar",min_value=1,max_value=3, step=1)

for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i+1}", PRODUCTOS, key=f"producto_{i}")
    cantidad = st.number_input(f"Cantidad {i+1}",min_value=0, step=1,)
    if cantidad>0:
        pos=buscar_posicion(PRODUCTOS,producto)
        precio=PRECIOS[pos]
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(precio)
        subtotal.append(calcular_subtotal(precio,cantidad))

pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])
cambiar_iva = st.selectbox("Cambiar IVA", ["excento", "10.5%", "21%"])
if cambiar_iva=="excento":
    cambiar_iva=0
elif cambiar_iva=="10.5%":
     cambiar_iva=0.105
else:
    cambiar_iva=0.21
fecha =st.date_input("Ingrese la fecha:")
numero=st.number_input("Ingrese su numero de presupuesto",min_value=0, step=1)


if pago=="Efectivo" and cantidad>0:
        descuento=aplicar_descuento(subtotal,DESCUENTO_EFECTIVO)[0]
        descontado= aplicar_descuento(subtotal,DESCUENTO_EFECTIVO)[1]
else:
    descuento=0
    descontado=sum(subtotal)

if cantidad>0:
        iva= aplicar_iva(descontado,cambiar_iva)[0]
        total= aplicar_iva(descontado,cambiar_iva)[1]
archivo = pdf(cliente=nombre, total=total,subtotal=subtotal,descuento=descuento,iva=iva,numero=numero,fecha=fecha,cantidad=cantidades,producto=nombres,precio=precios_unitarios)

st.write(f"Precios unitarios:")
for i in range(len(nombres)):
    st.write(f"{nombres[i]} ${precios_unitarios[i]}")
st.write(f"Subtotal:")
for i in range(len(nombres)):
    st.write(f"{cantidades[i]} x {nombres[i]} ${precios_unitarios[i]}")
st.metric(f"Descuento:",f"${descuento}")
st.metric(f"IVA:",f"${iva}")
st.metric(f"Subtotal con descuento:",f"${descontado}")
st.metric(f"Total:",f"${total}")

if nombre == "" :
    st.error("Ingrese su nombre para descargar el presupuesto")  
if len(cantidades)==0:
    st.error("Ingrese al menos un producto para descargar el presupuesto")
if nombre != "" and len(cantidades)>0:
    st.download_button("Descargar PDF", archivo, file_name="presupuesto.pdf", mime="application/pdf")