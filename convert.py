import cc_dat_utils
import cc_json_utils


json_data = cc_json_utils.make_cc_data_from_json("data/sglickma_testData.json")
cc_dat_utils.write_cc_data_to_dat(json_data, "data/sglickma_testData.dat")
dat_data = cc_dat_utils.make_cc_data_from_dat("data/sglickma_testData.dat")
print(dat_data)

