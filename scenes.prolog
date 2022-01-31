:- dynamic(scene/1).
:- dynamic(scene_name/2).
:- dynamic(scene_type/2).
:- dynamic(scene_visited/2).
:- dynamic(lead_outs/2).
:- dynamic(scene_description/2).
:- dynamic(scene_clues/2).
:- dynamic(scene_characters/2).

tag(sadies_sob_story).
name(sadies_sob_story, "Sadie's Sob Story").
type(sadies_sob_story, introduction).
player_visited(sadies_sob_story, False).
lead-outs(sadies_sob_story, what_the_cops_know).
lead-outs(sadies_sob_story, fullers_electrical_repair).
lead-outs(sadies_sob_story, the_peculiar_death_of_myron_fink).
description(sadies_sob_story, "The scenario starts off for Vivian Sinclair on a Monday morning after she’s turned in her most recent story. Invite the player to describe it, if she likes. She may rest on her laurels and joke around with the guys in the Herald Tribune’s newsroom, or she may already be scouring a pile of newspaper clippings and notes for her next lead. Around 9 a.m., she gets a telephone call from downstairs.").
description(sadies_sob_story, "Use this as an opportunity to establish Viv’s newsroom and how she meets with interested parties. Does she have the receptionist send them up to her desk in a smoky room full of (mostly) men bent over typewriters and paper-strewn desks? Or does she meet with her Sources and sometime- clients in another location, such as a restaurant across the street? Have the player take a moment to describe something important that Viv keeps at her desk in the newsroom, or her regular order at the restaurant.").
clues(sadies_sob_story, someone_in_georges).
clues(sadies_sob_story, george_works_as).
characters(sadies_sob_story, sadie_cain).
