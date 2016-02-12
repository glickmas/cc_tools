import json
import sys
import cc_dat_utils
import cc_data

default_input_json_file = "data/sglickma_cc1.json"
default_output_dat_file = "data/sglickma_cc1.dat"

json_reader = open(default_input_json_file, "r")
json_data = json.load(json_reader)
json_reader.close() #Close the file now that we're done using it

#def make_datafile_from_json(json_data):
cc_datafile = cc_data.CCDataFile()

for field in json_data:
    cc_level = cc_data.CCLevel()

    level_number = field["level_number"]
    cc_level.level_number = level_number
    time = field["time"]
    cc_level.time = time
    num_chips = field["num_chips"]
    cc_level.num_chips = num_chips

    upper_layer = field["upper_layer"]
    cc_level.upper_layer = upper_layer
    lower_layer = field["lower_layer"]
    cc_level.lower_layer = lower_layer

    optional_fields = field["optional_fields"]

    for opt_field in optional_fields:
        if opt_field["type_val"] == 3:
            cc_field = opt_field["title"]
            cc_title = cc_data.CCMapTitleField(cc_field)
            cc_level.add_field(cc_title)
        elif opt_field["type_val"] == 6:
            cc_field = opt_field["password"]
            cc_password = cc_data.CCEncodedPasswordField(cc_field)
            cc_level.add_field(cc_password)
        elif opt_field["type_val"] == 7:
            cc_field = opt_field["hint"]
            cc_hint = cc_data.CCMapHintField(cc_field)
            cc_level.add_field(cc_hint)
        elif opt_field["type_val"] == 10:
            cc_field = opt_field["monsters"]
            cc_monsters = cc_data.CCMonsterMovementField(cc_field)
            cc_level.add_field(cc_monsters)

    cc_datafile.add_level(cc_level)

print (cc_datafile)



# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename> <output dat filename>


# Reading the JSON data in from the input file
#json_reader = open(default_input_json_file, "r")
#json_data = json.load(json_reader)
#json_reader.close() #Close the file now that we're done using it

# Build the Python data structure from the JSON data
#  Note: Your code will be making a CCDataFile instead of a Game Library
#        You will want a function similar to this, but called something like
#             make_cc_data_from_json(json_data)

#game_library = make_game_library_from_json(json_data)
#game_levels = make_cc_data_from_json(json_data)

# This is where you would write the data to the DAT file
#  Note: You will use the cc_data_utils.write_cc_data_to_dat(cc_data, output_dat_file) function to do this
#        This function takes a CCDataFile object and the filename of the output file
#        It converts the CCDataFile object to binary and writes it to the output file
#print("I would write the data to this file", output_dat_file)

#cc_dat_utils.write_cc_data_to_dat(game_levels, default_output_dat_file)

#cc_returned = make_datafile_from_json(json_data)
#print("cc_returned= ", cc_returned)


#cc_dat_utils.write_cc_data_to_dat(cc_datafile,default_output_dat_file)