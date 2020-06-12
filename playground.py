#!/usr/bin/env python

# Playground for implementing design patterns in Python


import singleton as s


def test_singleton():
    # create one and only instance of Singleton
    foo = s.Singleton()

    # get same instance
    bar = s.Singleton.get_instance()

    # get same instance again
    baz = s.Singleton.get_instance()

    # print memory addresses to confirm foo, bar, and baz are all stored at a single point in memory
    print('Showing memory addresses to confirm foo, bar, and baz are all stored at a single point in memory')
    print(f'foo: {foo}')
    print(f'bar: {bar}')
    print(f'baz: {baz}')
    print()

    # compare foo, bar, and baz using is operator
    print('Comparing foo, bar, and baz using the `is` operator')
    print(f'foo is bar: {foo is bar}')
    print(f'bar is baz: {bar is baz}')
    print(f'baz is foo: {baz is foo}')
    print()

    # attempt to create another instance of Singleton
    print('Attempting to create another instance of Singleton. . .')
    try: 
        second_foo = s.Singleton()
    except Exception as e:
        print(f'Exception: {e}')


# playground
def main():
    print('Testing Singleton class. . .')
    print()
    test_singleton()


if __name__ == '__main__':
    main()
