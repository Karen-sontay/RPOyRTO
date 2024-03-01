from firebase import firebase

firebase = firebase.FirebaseApplication("https://virtual-ej-default-rtdb.firebaseio.com/",None)

datos ={
    'id': '14,',
    'primer sensor': '1024',
    'segundo sensor': '154'
}

#METODO POST
resultado=firebase.post('/ejerciciov/datos_post/', datos)