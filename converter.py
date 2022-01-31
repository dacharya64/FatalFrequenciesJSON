import json
import re

def check_in_item_tag(pred, item, item_type): 
	if pred in item:
		fWrite.write( item_type + "(" + str(item[pred]) + ").\n")
		return item[pred]

def check_in_item(pred, item): 
	if pred in item:
		fWrite.write( pred + "(" + tag + ", " + str(item[pred]) + ").\n")

def check_in_item_arr(pred, item): 
	if pred in item:
		array = item[pred]
		for subitem in array: 
			fWrite.write( pred + "(" + tag + ", " + str(subitem) + ").\n")
		

def check_in_item_quotes(pred, item): 
	if pred in item:
		fWrite.write( pred + "(" + tag + ", \"" + str(item[pred]) + "\").\n")

def check_in_item_arr_quotes(pred, item): 
	if pred in item:
		array = item[pred]
		for subitem in array: 
			fWrite.write( pred + "(" + tag + ", \"" + str(subitem) + "\").\n")


def convert_scenes():
	# opens the JSON file with the data and saves it to a JSON object
	with open('scenes.json') as data_file:
	    data = json.load(data_file)

	# add in the predicate definitions 
	fWrite.write(":- dynamic(scene/1).\n")
	fWrite.write(":- dynamic(scene_name/2).\n")
	fWrite.write(":- dynamic(scene_type/2).\n")
	fWrite.write(":- dynamic(scene_visited/2).\n")
	fWrite.write(":- dynamic(scene_lead_outs/2).\n")
	fWrite.write(":- dynamic(scene_description/2).\n")
	fWrite.write(":- dynamic(scene_clues/2).\n")
	fWrite.write(":- dynamic(scene_characters/2).\n")
	fWrite.write(":- dynamic(scene_challenges/2).\n")
	fWrite.write("\n")
	# runs through each element in JSON object and extracts the data, writing it to file
	for scene in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, scene, "scene")
		
		pred = "scene_name"
		check_in_item_quotes(pred, scene)

		pred = "scene_type"
		check_in_item(pred, scene)

		pred = "scene_visited"
		check_in_item(pred, scene)

		pred = "scene_lead_ins"
		check_in_item_arr(pred, scene)
		
		pred = "scene_lead_outs"
		check_in_item_arr(pred, scene)

		pred = "scene_description"
		check_in_item_arr_quotes(pred, scene)

		pred = "scene_clues"
		check_in_item_arr(pred, scene)

		pred = "scene_characters"
		check_in_item_arr(pred, scene)

		pred = "scene_challenges"
		check_in_item_arr(pred, scene)

def convert_clues():
	# opens the JSON file with the data and saves it to a JSON object
	with open('clues.json') as data_file:
	    data = json.load(data_file)

	# add in the predicate definitions 
	fWrite.write(":- dynamic(clue/1).\n")
	fWrite.write(":- dynamic(clue_desc/2).\n")
	fWrite.write(":- dynamic(clue_known/2).\n")
	fWrite.write(":- dynamic(clue_leads_to/2).\n")
	fWrite.write("\n")
	# runs through each element in JSON object and extracts the data, writing it to file
	for clue in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, clue, "clue")
		
		pred = "clue_desc"
		check_in_item_quotes(pred, clue)

		pred = "clue_known"
		check_in_item(pred, clue)

		pred = "clue_leads_to"
		check_in_item(pred, clue)

tag = ""
# file to which we will be writing 
fWrite = open('database.prolog', 'w')
convert_scenes()
fWrite.write("\n\n")
convert_clues()
fWrite.close()

