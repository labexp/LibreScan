#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
class libhOCR:
	def __init__(self):
		pass

	#Process a file to make a word per line and overwrites the new file
	def process(self, file):
		count_words_aux = 1
		hitbox = []
		tree = ET.ElementTree(file=file)
		html = tree.getroot()
		for line in html.findall(".//*[@class='ocr_line']"):
			aux_line = ""
			first = True
			for word in line.findall(".//*[@class='ocrx_word']"):
				if (word.text == None):
					inside_word = word.find('.//*')
					while(inside_word.text == None):
						new_inside_word = inside_word.find('.//*')
						if(new_inside_word == None):
							break

						inside_word = new_inside_word
					if(inside_word.text == None):
						inside_word.text = ""
					aux_line += inside_word.text+" "
				else:
					aux_line += word.text+" "

				hitbox = word.get("title").split(" ")

				if(first):
					count_words = count_words_aux
					first = False
				else:
					line.remove(word)

				count_words_aux += 1

			word = line.find(".//*[@id='word_1_"+str(count_words)+"']")
			if(word == None):
				return
			new_hit_box = word.get("title").split(" ")

			new_hit_box[3] = hitbox[3]
			new_hit_box[4] = hitbox[4]

			new_title = " ".join(str(x) for x in new_hit_box)

			word.set("title", new_title)

			word.text = aux_line

		tree.write(file)

	#Receives a file and a number of a line and returns the text in that line
	def get_line(self, file, line_number):
		output_line = ""
		tree = ET.ElementTree(file=file)
		html = tree.getroot()
		line = html.find(".//*[@id='line_1_"+str(line_number)+"']")
		if(line != None):
			word = line.find(".//*[@class='ocrx_word']")
			if (word.text == None):
				if (word[0].tag == '{http://www.w3.org/1999/xhtml}strong'):
					output_line += word[0].text+" "
			else:
				output_line += word.text+" "
		return output_line

	#Receives a file, number of a line and  line of text to put this text on the line
	def edit_line(self, file, line_number, text_line):
		tree = ET.ElementTree(file=file)
		html = tree.getroot()
		line = html.find(".//*[@id='line_1_"+str(line_number)+"']")
		if(line != None):
			word = line.find(".//*[@class='ocrx_word']")
			if (word.text == None):
				if (word[0].tag == '{http://www.w3.org/1999/xhtml}strong'):
					word[0].text = 	text_line
			else:
				word.text = text_line

		tree.write(file)
