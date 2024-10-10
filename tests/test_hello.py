import pytest
from helloworld import main
from io import StringIO
import sys

def test_main(capsys):
    # Capture output from the main function
    main()
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the output is as expected
    assert captured.out == "Hello, World!\n"
