from __future__ import print_function

import io
import json
import os
import sys

from six.moves import zip

from stix2elevator import elevate_file
from stix2elevator.options import (get_option_value, initialize_options,
                                   set_option_value)
from stix2elevator.utils import find_dir, iterpath

TESTED_XML_FILES = []
XML_FILENAMES = []
MASTER_JSON_FILES = []

IGNORE = (u"id", u"idref", u"created_by_ref", u"object_refs", u"marking_ref",
          u"object_marking_refs", u"target_ref", u"source_ref", u"valid_until",
          u"sighting_of_ref", u"observed_data_refs", u"where_sighted_refs",
          u"created", u"modified", u"first_seen", u"valid_from", u"last_seen",
          u"first_observed", u"last_observed", u"published",
          u"external_references")


def idiom_mappings(xml_file_path, stored_json):
    """Test fresh conversion from XML to JSON matches stored JSON samples."""
    print("Checking - " + xml_file_path)
    print("With Master - " + stored_json["id"])

    initialize_options()
    set_option_value("log_level", "CRITICAL")
    set_option_value("validator_args", "--no-cache")
    if not get_option_value("policy") == "no_policy":
        print("'no_policy' is not allowed for testing")
    set_option_value("policy", "no_policy")
    sys.setrecursionlimit(3000)
    converted_json = elevate_file(xml_file_path)
    converted_json = json.loads(converted_json)

    for good, to_check in zip(iterpath(stored_json), iterpath(converted_json)):
        good_path, good_value = good
        last_good_field = good_path[-1]

        if isinstance(good_value, (dict, list)):
            # Rule #1: No need to verify iterable types. Since we will deal
            # with individual values in the future.
            continue

        if (any(s in (u"object_marking_refs", u"granular_markings")
                for s in good_path)):
            # Exception to Rule #1: object_marking_refs and granular_markings
            # are not verifiable because they contain identifiers per rule #2.
            continue

        if last_good_field in IGNORE:
            # Rule #2: Since fresh conversion may create dynamic values.
            # Some fields are omitted for verification. Currently
            # fields with: identifier and timestamp values.
            continue

        yield good, to_check


def setup_tests():
    directory = os.path.dirname(__file__)

    xml_idioms_dir = find_dir(directory, "idioms-xml")
    json_idioms_dir = find_dir(directory, "idioms-json")

    print("Setting up tests from following directories...")
    print(xml_idioms_dir)
    print(json_idioms_dir)

    for json_filename in sorted(os.listdir(json_idioms_dir)):
        if json_filename.endswith(".json"):
            path = os.path.join(json_idioms_dir, json_filename)

            with io.open(path, "r", encoding="utf-8") as f:
                loaded_json = json.load(f)

            MASTER_JSON_FILES.append(loaded_json)

    for xml_filename in sorted(os.listdir(xml_idioms_dir)):
        if xml_filename.endswith(".xml"):
            path = os.path.join(xml_idioms_dir, xml_filename)
            XML_FILENAMES.append(xml_filename.split(".")[0])
            TESTED_XML_FILES.append(path)


def test_idiom_mapping(test_file, stored_master):
    for good_path, check_path in idiom_mappings(test_file, stored_master):
        if good_path != check_path:
            find_index_of_difference(good_path, check_path)
            assert good_path == check_path


def pytest_generate_tests(metafunc):
    setup_tests()
    argnames = ["test_file", "stored_master"]
    argvalues = [(x, y) for x, y in zip(TESTED_XML_FILES, MASTER_JSON_FILES)]

    metafunc.parametrize(argnames=argnames, argvalues=argvalues, ids=XML_FILENAMES, scope="function")


def find_index_of_difference(str1, str2):
    str1_len = len(str1[1])
    str2_len = len(str2[1])
    i = j = 0

    while True:
        if i < str1_len and j < str1_len:
            if str1[1][i] != str2[1][j]:
                print("difference at " + str(i))
                break
        elif i == str1_len and j == str2_len:
            print("no difference")
            break
        elif i == str1_len:
            print("str1 ended at " + str(i))
            break
        elif j == str2_len:
            print("str2 ended at " + str(j))
            break
        i = i + 1
        j = j + 1
