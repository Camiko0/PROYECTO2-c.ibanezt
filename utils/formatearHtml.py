from flask import make_response

#Convertir de String a html para mostrar el front
def convertirStringToHtml(html_content: str) -> bool:
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response