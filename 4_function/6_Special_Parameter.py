def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# standard_arg function calling
standard_arg("This is standard argument.")

# pos_only_arg function calling
pos_only_arg("This is pos_only_arg function")
# pos_only_arg(arg = "This is pos_only_arg function")   # this will produce an error

# kwd_only_arg function calling
kwd_only_arg(arg="This function is called via keyword arguments")
# kwd_only_arg("This function is called via keyword arguments")    # this will produce an error

# combined_example function calling
combined_example("Hello, I am position argument","Who are you ? ",kwd_only="I am keyword argument")

'''
Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.
'''