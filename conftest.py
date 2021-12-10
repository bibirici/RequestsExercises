def pytest_addoption(parser):
    parser.addoption("--todos", action = "store",
                     default = "default name")
    parser.addoption("--posts", action="store",
                     default="default name")
    parser.addoption("--users", action="store",
                     default="default name")
    parser.addoption("--users_objects", action="store",
                     default="default name")

def pytest_generate_tests(metafunc):
    option_value1 = metafunc.config.option.todos
    option_value2 = metafunc.config.option.posts
    option_value3 = metafunc.config.option.users
    option_value4 = metafunc.config.option.users_objects
    if 'todos' in metafunc.fixturenames and option_value1 is not None:
        metafunc.parametrize("todos", [option_value1])
    if 'posts' in metafunc.fixturenames and option_value2 is not None:
        metafunc.parametrize("posts", [option_value2])
    if 'users' in metafunc.fixturenames and option_value3 is not None:
        metafunc.parametrize("users", [option_value3])
    if 'users_objects' in metafunc.fixturenames and option_value4 is not None:
        metafunc.parametrize("users_objects", [option_value4])