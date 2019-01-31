from bashify import bashify

lines = ["test=$(service mongod status)", "echo 'test'", "echo $test"]
name = "test"

b = bashify(name, lines)
b.runExecutable()

b2 = bashify()

b2.printBashFile(name, lines)
b2.makeExecutable(name)
b2.runExecutable(name)