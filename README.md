fibonacci.py     gets N as input and outputs the Nth number in the Fibonacci sequence
fibonaci_test.py     tests the program by passing different values to it

# making the wheel (.whl) file and testing it:
1) create and organize directory 

2) build the wheel: 
python3 setup.py bdist_wheel

3) install the wheel:
pip install dist/fibonacci_project-0.1-py3-none-any.whl

4) run tests:
pytest --pyargs tests


This project was created as a means to learn CI/CD pipelines.
