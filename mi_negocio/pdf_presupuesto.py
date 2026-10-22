from fpdf import FPDF

NOMBRE_KIOSCO = "Kiosco Carlos Paz"
LOGO = "logopdf.png"
 


def renglon(pdf, texto, valor):
    # un renglon con el texto a la izquierda y el valor a la derecha
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def renglon_productos(pdf, texto, valor):
    # un renglon con el texto a la izquierda y el valor a la derecha
    pdf.cell(120, 9, f"     {texto}")
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")


def armar_pdf(cliente,total,subtotal,descuento,iva,numero,fecha,cantidad,producto,precio):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(LOGO, x=10, y=10, w=60)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 12, NOMBRE_KIOSCO, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 7, f"Presupuesto N° {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)

    pdf.set_font("Arial", "", 12)
    renglon(pdf, "Cliente", cliente)
    for i in range(len(cantidad)):
        renglon_productos(pdf, f"{cantidad[i]} x {producto[i]}", f"${precio[i]:.2f} c/u")
    pdf.ln(4)


    pdf.cell(0, 9, "Subtotal:", new_x="LMARGIN", new_y="NEXT")
    for i in range(len(cantidad)):
        renglon_productos(pdf, f"{producto[i]}", f"${subtotal[i]:.2f}")
    renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, "IVA 21%", f"${iva:.2f}")
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(5, 178, 220)
    renglon(pdf, "TOTAL", f"${total:.2f}")
    pdf.set_text_color(0,0,0)

    pdf.ln(10)
    pdf.set_font("Arial", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.", new_x="LMARGIN", new_y="NEXT")


    return bytes(pdf.output())
