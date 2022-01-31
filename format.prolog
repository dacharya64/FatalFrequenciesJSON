%%% Format of prolog representation should be the following: 

%%%%%%%%%%%% SCENE INFO %%%%%%%%%%%%%

:- dynamic(scene/1).
scene(sadies_sob_story).
scene(fullers_electrical_repair).

:- dynamic(scene_name/2).
scene_name(sadies_sob_story, "Sadie’s Sob Story").
scene_name(fullers_electrical_repair, "Fuller’s Electrical Repair").

:- dynamic(scene_type/2).
scene_type(sadies_sob_story, introduction).

:- dynamic(scene_visited/2).
scene_vistied(sadies_sob_story, false).

:- dynamic(lead_outs/2).
lead_outs(sadies_sob_story, what_the_cops_know).
lead_outs(sadies_sob_story, fullers_electrical_repair).
lead_outs(sadies_sob_story, the_peculiar_death_of_myron_fink).

:- dynamic(scene_description/2).
scene_description(sadies_sob_story, "The scenario starts off for Vivian Sinclair on a Monday morning after she’s turned in her most recent story. Invite the player to describe it, if she likes. She may rest on her laurels and joke around with the guys in the Herald Tribune’s newsroom, or she may already be scouring a pile of newspaper clippings and notes for her next lead. Around 9 a.m., she gets a telephone call from downstairs.").
scene_description(sadies_sob_story, "Use this as an opportunity to establish Viv’s newsroom and how she meets with interested parties. Does she have the receptionist send them up to her desk in a smoky room full of (mostly) men bent over typewriters and paper-strewn desks? Or does she meet with her Sources and sometime- clients in another location, such as a restaurant across the street? Have the player take a moment to describe something important that Viv keeps at her desk in the newsroom, or her regular order at the restaurant.").

:- dynamic(scene_clues/2).
scene_clues(sadies_sob_story, someone_in_georges).
scene_clues(sadies_sob_story, george_went_to).

:- dynamic(scene_characters/2).
scene_characters(sadies_sob_story, sadie_cain).

%%%%%%%%%%%% CLUE INFO %%%%%%%%%%%%%%%

:- dynamic(clue/1).
clue(someone_in_georges) 

:- dynamic(clue_desc/2).
clue_desc(someone_in_georges, "Someone in George’s apartment building was murdered the day before he disappeared. She gives an address and third-story apartment number near the Brooklyn Navy Yard.").
clue(george_went_to, "George went to work the next day, but no one’s seen him since. That was Thursday. He didn’t come to work Friday and wasn’t in his building.").

:- dynamic(clue_known/2).
clue_known(someone_in_georges, false).
clue_known(george_went_to, false).

:- dynamic(clue_leads_to/2).
clue_leads_to(george_works_as, fullers_electrical_repair).