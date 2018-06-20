import smallest_factor as sf

def test_smallest_factor():
	assert sf.smallest_factor(1) == 1
	assert sf.smallest_factor(5) == 5
	assert sf.smallest_factor(9) == 3
	