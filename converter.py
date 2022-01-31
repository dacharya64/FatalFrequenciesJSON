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
	for item in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, item, "scene")
		
		pred = "scene_name"
		check_in_item_quotes(pred, item)

		pred = "scene_type"
		check_in_item(pred, item)

		pred = "scene_visited"
		check_in_item(pred, item)

		pred = "scene_lead_ins"
		check_in_item_arr(pred, item)
		
		pred = "scene_lead_outs"
		check_in_item_arr(pred, item)

		pred = "scene_description"
		check_in_item_arr_quotes(pred, item)

		pred = "scene_clues"
		check_in_item_arr(pred, item)

		pred = "scene_characters"
		check_in_item_arr(pred, item)

		pred = "scene_challenges"
		check_in_item_arr(pred, item)

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
	for item in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, item, "clue")
		
		pred = "clue_desc"
		check_in_item_quotes(pred, item)

		pred = "clue_known"
		check_in_item(pred, item)

		pred = "clue_leads_to"
		check_in_item(pred, item)

def convert_sources():
	# opens the JSON file with the data and saves it to a JSON object
	with open('sources.json') as data_file:
	    data = json.load(data_file)

	# add in the predicate definitions 
	fWrite.write(":- dynamic(source/1).\n")
	fWrite.write(":- dynamic(source_name/2).\n")
	fWrite.write(":- dynamic(source_profession/2).\n")
	fWrite.write(":- dynamic(source_description/2).\n")
	fWrite.write(":- dynamic(source_investigative_abilities/2).\n")
	fWrite.write("\n")
	# runs through each element in JSON object and extracts the data, writing it to file
	for item in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, item, "source")
		
		pred = "source_name"
		check_in_item_quotes(pred, item)

		pred = "source_profession"
		check_in_item_quotes(pred, item)

		pred = "source_description"
		check_in_item_quotes(pred, item)

		pred = "source_investigative_abilities"
		check_in_item_arr(pred, item)

def convert_problems():
	# opens the JSON file with the data and saves it to a JSON object
	with open('problems.json') as data_file:
	    data = json.load(data_file)

	# add in the predicate definitions 
	fWrite.write(":- dynamic(problem/1).\n")
	fWrite.write(":- dynamic(problem_name/2).\n")
	fWrite.write(":- dynamic(problem_type/2).\n")
	fWrite.write(":- dynamic(problem_description/2).\n")
	fWrite.write(":- dynamic(problem_effect/2).\n")
	fWrite.write("\n")
	# runs through each element in JSON object and extracts the data, writing it to file
	for item in data:
		pred = "tag" 
		global tag 
		tag = check_in_item_tag(pred, item, "problem")
		
		pred = "problem_name"
		check_in_item_quotes(pred, item)

		pred = "problem_type"
		check_in_item(pred, item)

		pred = "problem_description"
		check_in_item_quotes(pred, item)

		pred = "problem_effect"
		check_in_item_quotes(pred, item)

tag = ""
# file to which we will be writing 
fWrite = open('database.prolog', 'w')
convert_scenes()
fWrite.write("\n\n")
convert_clues()
fWrite.write("\n\n")
convert_sources()
fWrite.write("\n\n")
convert_problems()
fWrite.write("\n\n")

fWrite.close()

