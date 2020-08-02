import sys

print("Name is :", sys.argv[0])

print("Path has ", sys.path)


def dump(module):
    print(module, "=========>")
    if module in sys.builtin_module_names:
        print("内建模块", module)
    else:
        try:
            module = __import__(module)
            print(module.__file__)
        except:
            print("没有这个模块", module)


dump("os")
dump("sys")
dump("string")
dump("strop")
dump("zlib")
