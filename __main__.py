from runpy import run_path

'''
ATTENTION!

This lab is pretty messy if you type everything into main script all at once,
I've divided it into respective Python scripts to make the code (and output) tidier.

IGNORE THE DEF(BLAHBLAH): JUST FOCUS ON THE CODE INSIDE EACH OF THEM INSTEAD!!!

You are encouraged to experiment by debugging and editing the values to see the outputs when running the scripts.

You can either run here to display EVERYTHING
or run individual scripts by navigating to the desired script and click the run button from there.

Oh right, feel free to comment out the function calls below each scripts to
focus your studies on specific codes and it's outputs. 

Example: Add a hashtag before list_basic_usage(), becoming '#list_basic_usage()'
that Python will ignore since it's treated as a comment instead.

P.S: Some comments will refer "Values" as "Elements" or vice versa,
both are used interchangeably to describe the same thing.

Good reading and happy trails!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣤⣤⣴⣿⠟⠁⠀⠈⠛⠿⣿⣿⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣶⣇⠀⢀⣴⣿⠟⠉⠉⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⣿⣆⠀⠀⠀⠀⠀⠀
⢀⣿⡟⠙⢿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣄⠀⠀⠀⠀
⠸⣿⡇⠀⠀⠀⠀⠀⢀⡴⠶⢦⣄⣀⣤⠾⠛⠛⣧⡀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣄⠀⠀
⢠⣿⣇⠀⠀⠀⠀⣴⠋⠀⠀⠀⠈⠉⠁⠀⠀⠀⠈⠻⣦⣤⡤⠶⠻⢿⣦⠀⠀⢻⣿⣆⠀
⢸⣿⠉⢳⣶⢶⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⣿⣿⠀
⠘⣿⣄⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠄⠀⠀⠀⠀⢠⡼⠋⠀⠀⠀⣿⣿⠀
⠀⢹⡿⠁⠀⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠠⣝⢦⡀⠀⠀⣿⣿⠀
⢀⣿⠇⠀⠀⠘⣿⠇⠀⠀⢀⠎⠀⠀⠀⠘⠛⠛⠿⠆⠀⠀⠀⠀⠠⣝⢧⡳⡄⣸⣿⡟⠀
⢸⣿⠀⠀⠀⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣜⢷⣽⣷⣿⣿⠃⠀
⢸⡏⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠆⣹⣿⣿⠃⠀⠀
⢸⣇⠀⠀⠀⠀⠀⠀⠈⠛⠂⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⠀⠀⠀
⢸⣿⠀⠀⣾⣤⣀⣀⣀⢀⣀⣀⣀⡤⠔⠚⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⠀⠀
⠀⣿⣇⠀⠻⠳⢤⣈⣉⠉⠉⠀⣀⣀⣤⠖⠋⠟⠀⠀⠀⠀⠀⠀⢀⣀⣠⣾⣿⠃⠀⠀⠀
⠀⠘⣿⣆⠀⠀⠀⠈⠙⣛⣛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠛⠋⠀⠀⠀⠀⠀
⠀⠀⠘⢿⣧⡀⠀⠀⠈⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣶⣦⣤⣤⣤⣤⣶⣶⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

print('\n')

if __name__ == '__main__':
    py_scripts = ('List.py', 'Tuple.py', 'Set.py', 'Dictionary.py')

    for script in range(len(py_scripts)):
        run_path('./{}'.format(py_scripts[script]))
        script += 1