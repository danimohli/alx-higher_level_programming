#!/usr/bin/python3

if __name__ == "__main__":

    import importlib.util

    # Load the compiled module

    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all the names in the module

    names = dir(module)

    # Print names in alphabetical order excluding those starting with '__'

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
