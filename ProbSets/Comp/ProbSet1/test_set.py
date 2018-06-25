from set import *
import pytest

def test_count_cards():

	with pytest.raises(ValueError) as excinfo:
		count_sets(["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110"])
	assert excinfo.value.args[0] == "there are not exactly 12 cards"
    
	with pytest.raises(ValueError) as excinfo:
		count_sets(["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "2110"])
	assert excinfo.value.args[0] == "the cards are not all unique"
    
	with pytest.raises(ValueError) as excinfo:
		count_sets(["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "102"])
	assert excinfo.value.args[0] == "one or more cards does not have exactly 4 digits"
    
	with pytest.raises(ValueError) as excinfo:
		count_sets(["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1023"])
	assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"
	
	hand = ["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]
	assert count_sets(hand) == 6


def test_is_set():
	assert is_set("1022", "1122", "1020") == False
	assert is_set("0000", "1111", "2222") == True