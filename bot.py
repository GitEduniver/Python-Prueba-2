import requests
from webscraping import  precioActual
from webscraping import  precioDeseado
def telegram_bot_sendtext(bot_message):
    bot_token  = '6692627648:AAGvFwCE-p6zT6U7EsDAki05A22YZnhn94k'
    bot_chatID = '6692627648'
    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(enviar_text)
    return response.json()
if precioDeseado < precioActual:
    test = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioActual)}\nEnlace: https://listado.mercadolibre.com.ec/zapatos-deportivos")
else:
    test = telegram_bot_sendtext(f" ¡El precio sigue muy alto! Esta en:  {'$'+str(precioActual)}")