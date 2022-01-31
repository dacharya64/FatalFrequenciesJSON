:- dynamic(scene/1).
:- dynamic(scene_name/2).
:- dynamic(scene_type/2).
:- dynamic(scene_visited/2).
:- dynamic(scene_lead_outs/2).
:- dynamic(scene_description/2).
:- dynamic(scene_clues/2).
:- dynamic(scene_characters/2).
:- dynamic(scene_challenges/2).

scene(sadies_sob_story).
scene_name(sadies_sob_story, "Sadie's Sob Story").
scene_type(sadies_sob_story, introduction).
scene_visited(sadies_sob_story, False).
scene_lead_outs(sadies_sob_story, what_the_cops_know).
scene_lead_outs(sadies_sob_story, fullers_electrical_repair).
scene_lead_outs(sadies_sob_story, the_peculiar_death_of_myron_fink).
scene_description(sadies_sob_story, "The scenario starts off for Vivian Sinclair on a Monday morning after she’s turned in her most recent story. Invite the player to describe it, if she likes. She may rest on her laurels and joke around with the guys in the Herald Tribune’s newsroom, or she may already be scouring a pile of newspaper clippings and notes for her next lead. Around 9 a.m., she gets a telephone call from downstairs.").
scene_description(sadies_sob_story, "Use this as an opportunity to establish Viv’s newsroom and how she meets with interested parties. Does she have the receptionist send them up to her desk in a smoky room full of (mostly) men bent over typewriters and paper-strewn desks? Or does she meet with her Sources and sometime- clients in another location, such as a restaurant across the street? Have the player take a moment to describe something important that Viv keeps at her desk in the newsroom, or her regular order at the restaurant.").
scene_clues(sadies_sob_story, someone_in_georges).
scene_clues(sadies_sob_story, george_works_as).
scene_characters(sadies_sob_story, sadie_cain).


:- dynamic(clue/1).
:- dynamic(clue_desc/2).
:- dynamic(clue_known/2).
:- dynamic(clue_leads_to/2).

clue(someone_in_georges).
clue_desc(someone_in_georges, "Someone in George’s apartment building was murdered the day before he disappeared. She gives an address and third-story apartment number near the Brooklyn Navy Yard.").
clue_known(someone_in_georges, False).
clue(george_works_as).
clue_desc(george_works_as, "(Core, 'Fuller’s Electrical Repair') George works as an electrical repairman at Fuller’s Electrical Repair, just a couple blocks north of Fulton Street in downtown Brooklyn.").
clue_known(george_works_as, False).
clue_leads_to(george_works_as, fullers_electrical_repair).


:- dynamic(source/1).
:- dynamic(source_name/2).
:- dynamic(source_profession/2).
:- dynamic(source_description/2).
:- dynamic(source_investigative_abilities/2).

source(annette_rice).
source_name(annette_rice, "Annette (Nettie) Rice").
source_profession(annette_rice, "Professor").
source_description(annette_rice, "If, during her time at Hunter College, someone had asked Viv which professor she’d be closest friends with in a decade, she’d never have named Nettie Rice.").
source_investigative_abilities(annette_rice, astronomy).
source_investigative_abilities(annette_rice, biology).
source_investigative_abilities(annette_rice, chemistry).
source_investigative_abilities(annette_rice, languages).
source_investigative_abilities(annette_rice, physics).


:- dynamic(problem/1).
:- dynamic(problem_name/2).
:- dynamic(problem_type/2).
:- dynamic(problem_descrption/2).
:- dynamic(problem_effect/2).

problem(sucker_for_a_pretty_face).
problem_name(sucker_for_a_pretty_face, "Sucker for a Pretty Face").
problem_type(sucker_for_a_pretty_face, continuity).
problem(wrenched_ankle).
problem_name(wrenched_ankle, "Wrenched Ankle").
problem_descrption(wrenched_ankle, "You pulled something in your foot.").
problem_effect(wrenched_ankle, "-2 on your next Athletics, Fighting, or other General/Physical test or Take Time and then discard this Problem").