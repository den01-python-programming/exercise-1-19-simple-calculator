import pytest
import src.exercise

def test_exercise():
    input_values = ["12","24"]
    input_values_stored = ["12","24"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Give the first number:",\
                                       "Give the second number:",\
                                       input_values_stored[0] + " + " + input_values_stored[1] + " = "\
                                       + str(int(input_values_stored[0])+int(input_values_stored[1])),\
                                       input_values_stored[0] + " - " + input_values_stored[1] + " = "\
                                       + str(int(input_values_stored[0])-int(input_values_stored[1])),\
                                       input_values_stored[0] + " * " + input_values_stored[1] + " = "\
                                       + str(int(input_values_stored[0])*int(input_values_stored[1])),\
                                       input_values_stored[0] + " / " + input_values_stored[1] + " = "\
                                       + str(int(input_values_stored[0])/int(input_values_stored[1]))]
