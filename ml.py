import pandas as pd 

def runML(data):
    df = pd.DataFrame(data)
    # do machine learning stuff
    print(df, flush=True)
    return 1


if __name__ == "__main__":
    JSONdata = [{ "poisonous_or_edible": "p", "cap_shape": "x", "cap_surface": "s", "cap_color": "p", "bruises": "f", "odor": "c", "gill_attachment": "f", "gill_spacing": "w", "gill_size": "n", "gill_color": "g", "stalk_shape": "e", "stalk_root": "b", "stalk_surface_above_ring": "s", "stalk_surface_below_ring": "s", "stalk_color_above_ring": "w", "stalk_color_below_ring": "w", "veil_type": "p", "veil_color": "w", "ring_number": "o", "ring_type": "p", "spore_print_color": "n", "population": "s", "habitat": "d" }]
    print(runML(JSONdata), flush=True)
