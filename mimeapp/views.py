from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
data="""<table><tr><th>Eid</th><th>Ename</th><th>Esal</th></tr>
         <tr><td>1001</td><td>Scott</td><td>2000</td></tr>
         <tr><td>1002</td><td>Blake</td><td>3000</td></tr>
         <tr><td>1003</td><td>Miller</td><td>4000</td></tr></table>"""
def csvview(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; ' \
                     'filename="myfile.csv"'
    writer=csv.writer(response)
    writer.writerow(['First row','Foo','Bar','Baz'])
    writer.writerow(['Second row','A','B','C',"Testing","Here's a quote"])
    return response
def pdfview(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= \
    'fvattachment; filename="myfile.pdf"'
    p=canvas.Canvas(response)
    p.drawString(100,100, "Hello World.")
    p.showPage()
    p.save()
    return response
def htmlview(request):
    return HttpResponse(data,content_type="text/html")
def xmlview(request):
    return HttpResponse(data,content_type="application/xml")



# Create your views here.
