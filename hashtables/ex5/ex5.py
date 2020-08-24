# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    directories = {}

    for file in files:
        f = file.split("/")[-1]

        if f not in directories:
            directories[f] = [] 

        directories[f].append(file)

    for q in queries:
        if q in directories:
            result.extend(directories[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
        '/bin/foo/bar/foo',
        '/bin/bar/bar/bar/baz',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
