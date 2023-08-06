from pyatc import PyATC
import os
import filecmp

version_delimiter = "================================================"
print_prefix = "===== "
path = "data/"

test_data = [("V2","in_v2.atc", 30, 9000, None, "v2_edf_target.edf"), ("V3", "in_v3.atc", 30, 9000, None, "v3_edf_target.edf")]
for (version, atcIn, atcInDuration, lead1len, lead2, targetEdf) in test_data:
    print(version_delimiter)
    print("TESTING "+str(version))
    print(version_delimiter)
    print(print_prefix+"TESTING READING ATC FILE")
    print("Reading ATC file")
    atc = PyATC.read_file(path+atcIn)
    print("Checking that the recording duration is correct")
    assert(atc.get_recording_duration() == atcInDuration)

    print("Testing that ecg 1 and 2 samples are set correctly")
    assert(len(atc.get_lead1_samples()) == lead1len)
    assert(atc.get_lead2_samples() == lead2)

    #Test json
    print(print_prefix+"TESTING TO/FROM JSON")
    print("Writing to json")
    atc.write_json_to_file(path+"out.json")
    print("Reading from json")
    atc_from_json = PyATC.read_json_file(path+"out.json")
    print("Removing json file")
    os.remove(path+"out.json")
    assert(atc == atc_from_json)

    print(print_prefix+"TESTING TO/FROM ATC")
    print("Writing to ATC")
    atc.write_to_file(path+"out.atc")

    #Does in.atc === out.atc?
    print("Validating that the newly created file equals the input file")
    assert(filecmp.cmp(path+atcIn, path+"out.atc", shallow = False))

    print("Reading the newly written ATC")
    atc2 = PyATC.read_file(path+"out.atc")

    print("Removing newly created atc")
    os.remove(path+"out.atc")
    assert(atc == atc2)

    print(print_prefix+"TESTING TO EDF")
    print("Writing EDF file")
    atc.write_edf_to_file(path+"out.edf")

    print("Validating contents of the written EDF")
    assert(filecmp.cmp(path+"out.edf", path+targetEdf, shallow = False))
    print("Removing written EDF")
    os.remove(path+"out.edf")

print(version_delimiter)
print("OTHER TESTS")

#Try loading a v4 file that should fail
print("Trying to read ATC v4 file (should raise exception)")
failed = False
try:
    PyATC.read_file(path+"in_v4.atc")
except:
    failed = True
assert(failed)
