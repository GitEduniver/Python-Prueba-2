from  bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://listado.mercadolibre.com.ec/zapatos-deportivos")
soup = BeautifulSoup(url.content,"html.parser")


resultado = soup.find("span",{"class","andes-money-amount__fraction"})

print(resultado)

precioActual_text = resultado.text

print(precioActual_text)

precioActual = float(precioActual_text)

print(precioActual)

precioDeseado = 100

print(precioDeseado)

if precioDeseado >= precioActual:
    print("Hola hay una oferta interesante")
else:
    print("Por el momento no tenemos nada para ti")