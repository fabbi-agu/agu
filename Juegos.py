import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import os
def ingresar_datos():
	ok=True
	columna  = [
	    [sg.Text('elige con que juego quiere jugar')],
	    [sg.Text('1- Ahorcado')],
	    [sg.Text('2- Ta - Te - Ti')],
	    [sg.Text('3- Otello')],
	    [sg.Text('4- Salir')],
	    [sg.Button('Enviar'),sg.Button('Cancelar')]
	]
	columna1 = [
	    [sg.Text('nombre')],[sg.Input(key='nom')],
	    [sg.Text('apellido')],[sg.Input(key='ape')],
		[sg.Text('Numero')],[sg.Input(key='num')],
	]
	layout = [
	    [
	     sg.Column(columna1,background_color='black'), sg.Column(columna, background_color='lightblue')
	     ]
	]
	window = sg.Window("Ventana").Layout(layout)
	events,values = window.read()
	if( events== None or events== 'Cancelar'):
		ok=False
	window.close()
	return values['num'],values['nom'],values['ape'],ok

def sigue_jugando():
	ok=False
	columna  = [
	    [sg.Text('elige con que juego quiere jugar')],
	    [sg.Text('1- Ahorcado')],
	    [sg.Text('2- Ta - Te - Ti')],
	    [sg.Text('3- Otello')],
	    [sg.Text('4- Salir')],
		[sg.Input(key='num')],
	    [sg.Button('Enviar'),sg.Button('Cancelar')]
	]

	layout = [
	    [
		sg.Frame('SEGUIS JUGANDO',[[
	     sg.Column(columna, background_color='lightblue')]])
	     ]
	]

	window = sg.Window("Ventana").Layout(layout)
	events,values = window.read()
	if events==None or events== 'Cancelar':
		ok=True
	window.close()
	return values['num'],ok

def where_json(file_name):
	return os.path.exists(file_name)

dataa=[]
datos={}
tupla = ingresar_datos()
sigo_jugando=tupla[3]
pre=tupla[3]
if(sigo_jugando):
	keyy=tupla[2]+' '+tupla[1]
	if where_json('jugadores.json'):
		archivo=open('jugadores.json','r')
		datos=json.load(archivo)
	else:
	    datos[keyy] =[]
	    with open('data.json', 'w') as outfile:
	        json.dump(datos, outfile)
	if keyy in datos:
		dataa=datos[keyy]
	else:
		datos[keyy]=[]
while sigo_jugando:
	if tupla[0] == '1':
		hangman.main()
		dataa.append('Jugo al ahorcado')
	elif tupla[0] == '2':
		tictactoeModificado.main()
		dataa.append('Jugo al TaTeTi')
	elif tupla[0] == '3':
		reversegam.main()
		dataa.append('Jugo al Reversegam')
	elif tupla[0]  == '4' or tupla[1]==True :
		break
	if tupla[0] != '4' :
		tupla = sigue_jugando()
if(pre):
	datos[keyy]=dataa
	archivo= open('jugadores.json', 'w')
	json.dump(datos, archivo, indent=4)
	archivo.close()
