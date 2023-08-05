import os


def get_root_path():
    root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    return root_path


if __name__ == '__main__':
    print(get_root_path())
