-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/JuEPVM
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- This comes from the variables listed in Mushroom_Data.csv.

CREATE TABLE "Mushroom_Attributes" (
    "Poisonous_or_Edible" string   NOT NULL,
    "Cap_Shape" string   NOT NULL,
    "Cap_Surface" string   NOT NULL,
    "Cap_Color" string   NOT NULL,
    "Bruises" string   NOT NULL,
    "Odor" string   NOT NULL,
    "Gill_attachment" string   NOT NULL,
    "Gll_spacing" string   NOT NULL,
    "Gill_size" string   NOT NULL,
    "Gill_color" string   NOT NULL,
    "Stalk_shape" string   NOT NULL,
    "Stalk_root" string   NOT NULL,
    "stalk_surface_above_ring" string   NOT NULL,
    "stalk_surface_below_ring" string   NOT NULL,
    "stalk_color_above_ring" string   NOT NULL,
    "stalk_color_below_ring" string   NOT NULL,
    "veil_type" string   NOT NULL,
    "veil_color" string   NOT NULL,
    "ring_number" string   NOT NULL,
    "ring_type" string   NOT NULL,
    "spore_print_color" string   NOT NULL,
    "population" string   NOT NULL,
    "habitat" string   NOT NULL
);

