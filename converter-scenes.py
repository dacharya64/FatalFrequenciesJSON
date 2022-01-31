import json
import re

def check_in_scene_tag(pred, scene): 
	if pred in scene:
		fWrite.write( pred + "(" + str(scene[pred]) + ").\n")
		return scene[pred]

def check_in_scene(pred, scene): 
	if pred in scene:
		fWrite.write( pred + "(" + tag + ", " + str(scene[pred]) + ").\n")

def check_in_scene_arr(pred, scene): 
	if pred in scene:
		array = scene[pred]
		for item in array: 
			fWrite.write( pred + "(" + tag + ", " + str(item) + ").\n")
		

def check_in_scene_quotes(pred, scene): 
	if pred in scene:
		fWrite.write( pred + "(" + tag + ", \"" + str(scene[pred]) + "\").\n")

def check_in_scene_arr_quotes(pred, scene): 
	if pred in scene:
		array = scene[pred]
		for item in array: 
			fWrite.write( pred + "(" + tag + ", \"" + str(item) + "\").\n")

# file to which we will be writing 
fWrite = open('scenes.prolog', 'w')

# opens the JSON file with the data and saves it to a JSON object
with open('scenes.json') as data_file:
    data = json.load(data_file)

# add in the predicate definitions 
fWrite.write(":- dynamic(scene/1).\n")
fWrite.write(":- dynamic(scene_name/2).\n")
fWrite.write(":- dynamic(scene_type/2).\n")
fWrite.write(":- dynamic(scene_visited/2).\n")
fWrite.write(":- dynamic(lead_outs/2).\n")
fWrite.write(":- dynamic(scene_description/2).\n")
fWrite.write(":- dynamic(scene_clues/2).\n")
fWrite.write(":- dynamic(scene_characters/2).\n")
fWrite.write("\n")
# runs through each element in JSON object and extracts the data, writing it to file
for scene in data:
	pred = "tag" 
	tag = check_in_scene_tag(pred, scene)
	
	pred = "name"
	check_in_scene_quotes(pred, scene)

	pred = "type"
	check_in_scene(pred, scene)

	pred = "player_visited"
	check_in_scene(pred, scene)

	pred = "lead-ins"
	check_in_scene_arr(pred, scene)
	
	pred = "lead-outs"
	check_in_scene_arr(pred, scene)

	pred = "description"
	check_in_scene_arr_quotes(pred, scene)

	pred = "clues"
	check_in_scene_arr(pred, scene)

	pred = "characters"
	check_in_scene_arr(pred, scene)

	pred = "challenges"
	check_in_scene_arr(pred, scene)

fWrite.close()