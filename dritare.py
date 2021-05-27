
import re
import tkinter as tk
from tkinter import *

# importimi i funksioneve korrigjuese nga modulet përkatëse
from korrigjo import *
from korrigjo_e import *
from korrigjo_c import *

## funksioni kryesor i korrigjimeve që thërret funksionet e tjera
def correction(field_in, field_out, field_message):
	# merret përmbajtja e kutizës së parë
	input_text = field_in.get("1.0", END) 
	t = input_text ; total_sub = 0
	
	# thirren zëvendësimet paraprake
	t, c = pre_replace(t) ; total_sub += c
		
	# thirren zëvendësimet e e-së
	t, c = replace_e(t) ; total_sub += c
	
	# thirren zëvendësimet e c-së
	t, c = replace_c(t) ; total_sub += c
	
	# thirren zëvendësimet dialektore
	t, c = replace_dial(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve
	t, c = replace_words(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve angleze
	t, c = replace_eng(t) ; total_sub += c
	
	# thirren zëvendësimet përfundimtare
	t, c = post_replace(t) ; total_sub += c

	output_text = t
	# shfaqet totali i zëvendësimeve të kryera
	output_message = str.format("{} zëvendësime. ", total_sub)
	
	# futet teksti i redaktuar te kutiza e dytë
	field_out.insert("1.0", output_text)
	# futet mesazhi i zëvendësimeve te kutiza e tretë
	field_message.insert("1.0", output_message)

## funksion që fshin tekstin nga kutizat
def clearAll(field1, field2, field3):
	## fshihet e gjithë përmbajtja e fushës së tekstit
	field1.delete("1.0", END)
	field2.delete("1.0", END)
	field3.delete("1.0", END)
	
## pikënisja e ekzekutimit
if __name__ == "__main__":

	# krijohet ndërfaqja grafike me disa specifikime
	root = Tk()
	root.configure(background = "red")		# ngjyra e sfondit
	root.geometry("1000x716")				# përmasat e dritares
	# titulli i dritares kryesore
	root.title("REDAKTOR TEKSTI PËR GJUHËN SHQIPE")		
	
	# etiketa për tekstin hyrës
	inlabel = Label(root, text = "Hyrje", fg = "black", bg = "light green") 
	# etiketa për tekstin dalës (të redaktuar)
	outlabel = Label(root, text = "Dalje", fg = "black", bg = "light green")

	inlabel.grid(row = 1, column = 0, padx = 7) 
	outlabel.grid(row = 17, column = 0, padx = 7) 
	
	# tre fushat e tekstit 
	text1_field = Text(height=14, width=80, fg="white", bg="black")
	text2_field = Text(height=14, width=80, fg="white", bg="black")
	text3_field = Text(height=1, width=17, fg="white", bg="black")
	
	# pozicionimi i tre fushave të tekstit te dritarja kryesore
	text1_field.grid(row = 1, column = 1, padx = 7, pady = 7)
	text2_field.grid(row = 17, column = 1, padx = 7, pady = 7)
	text3_field.place(x=756, y=668) 
	
	# butoni i korrigjimit lidhet me funksionin e korrigjimeve
	correct_button = Button(root, text = "Redakto", bg = "cyan", fg = "black", 
			command = lambda: correction(text1_field, text2_field, text3_field))
	correct_button.grid(row = 2, column = 1) # .place(x=790, y=300)
	
	# butoni i fshirjes lidhet me funksionin e fshirjes
	clear_button = Button(root, text = "Shuaj", bg = "cyan", fg = "black",
			command = lambda: clearAll(text1_field, text2_field, text3_field)) 
	clear_button.grid(row = 18, column = 1) # .place(x=800, y=590)  
	
	# aktivizimi i dritares grafike
	root.mainloop()
