import operate as op
import pytest

def test_operate():
	with pytest.raises(TypeError) as excinfo:
		op.operate(1, 2, 5) 
	assert excinfo.value.args[0] == "oper must be a string"
	assert op.operate(1, 2, '+') == 3
	assert op.operate(1, 2, '-') == -1
	assert op.operate(1, 2, '*') == 2
	assert op.operate(1, 2, '/') == 0.5
	assert op.operate(2, 1, '/') == 2
	with pytest.raises(ZeroDivisionError) as excinfo:
		op.operate(2, 0, '/')
	assert excinfo.value.args[0] == "division by zero is undefined"
	with pytest.raises(ValueError) as excinfo:
		op.operate(1, 2, "p") 
	assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"