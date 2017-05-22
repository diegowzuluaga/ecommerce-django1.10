from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db import connection
from products.models import *
from orders.models import *
from cart.models import *
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors 
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Table
from reportlab.graphics.shapes import Rect
from reportlab.pdfgen import canvas



def my_sql(request, consulta):
    #sql = consulta
    cursor = connection.cursor()
    cursor.execute(consulta)
    row = cursor.fetchall()
    cursor.close()
    return row


def ReporteProductos(request):
	#sql = ("SELECT A.TITLE, B.TITLE FROM PRODUCTS_PRODUCT A, PRODUCTS_VARIATION B WHERE A.ID = B.PRODUCT_ID")
	sql = "select a.title as categoria,b.title as producto from products_category a, products_product b, products_product_categories c where c.category_id = a.id and c.product_id=b.id group by a.id, b.id"
	reporte1 = Product.objects.all()
	reporte= my_sql(request, sql)
	print(reporte)
	#contexto = {'lista' : reporte}
	#return render_to_response('products/reporte.html',reporte)
	return render_to_response('products/reporte.html', locals(), context_instance = RequestContext(request))

def VentasDia(request):
	sql = "select date(timestamp) as fecha, b.title as productos, sum(quantity) as cantidad, round(sum(line_item_total),2) as valor  from cart_cart a,  products_variation b, cart_cartitem c  where a.id=c.cart_id and c.item_id=b.id group by 1,2 order by 1,2 "
	reporte= my_sql(request, sql)
	paginator = Paginator(reporte, 15)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	print(contacts, paginator)
	return render_to_response('products/ventasdia.html', locals(), context_instance = RequestContext(request))
	#return render_to_response('products/ejemplo.rml', locals(), context_instance = RequestContext(request))


def csrf_rejected(request, reason = ''):
	contexto = {'reason' : reason}
	return render_to_response('home/csrf.html', contexto)

def practicas(request):
	response = HttpResponse(content_type='application/pdf')
	buff = BytesIO()
	styles = getSampleStyleSheet()
	styleN = styles['Normal']
	styleH = styles['Heading1']
	story = []
	#add some flowables
	story.append(Paragraph("This is a Heading",styleH))
	story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
	styleN))
	pdf_name = "clientes.pdf"
	doc = SimpleDocTemplate(buff ,pagesize = letter)
	doc.build(story)
	response.write(buff.getvalue())
	buff.close()
		
	return response


def imprimir_ventas(request):
    print ("Genero el PDF")
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    sql =''' select date(timestamp) as fecha,
              b.title as productos,sum(quantity) as cantidad,
              round(sum(line_item_total)) as valor
                from cart_cart a,  products_variation b, cart_cartitem c
                  where a.id=c.cart_id and c.item_id=b.id 
                  group by 1,2 order by 1,2 '''
    reporte= my_sql(request, sql)
    ventas = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Ventas por Items", styles['Title'])
    #linea = drawString("hola")
    #header = Paragraph("Listado de Ventas por Items", styles['RightAlign'])
    #ventas.append(linea)
    ventas.append(header)
    headings = ('Fecha', 'Producto', 'Cantidad', 'Valor')
    #allventas = [(p.fecha, p.producto, p.cantidad, p.valor) for p in item(for item in reporte)]
    #print (allventas)

    t = Table([headings] + reporte)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 3, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
            ('ALIGN', (2,1), (-1,-1), 'RIGHT'),
            ('ALIGN', (0,0), (-1,0), 'CENTER'),


        ]
    ))
    #t.setStyle(TableStyle(
    #    (TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    #                                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))


    ventas.append(t)
    doc.build(ventas)
    response.write(buff.getvalue())
    buff.close()
    return response



"""
def imprimir_ventas(request):
	buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)
 
        # Our container for 'Flowable' objects
        elements = []
 
        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RightAlign', fontName='Arial' alignment=TA_RIGHT))
 
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        users = User.objects.all()
        elements.append(Paragraph('My User Names', styles['RightAlign']))
 
        # Need a place to store our table rows
        table_data = []
        for i, user in enumerate(users):
            # Add a row to the table
            table_data.append([user.get_full_name(), user.username, user.last_login]))
        # Create the table
        user_table = Table(table_data, colWidths=[doc.width/3.0]*3)
        user_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
        elements.append(user_table)
        doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)
 
        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
        """