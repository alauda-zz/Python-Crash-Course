""" FileNotFound exception """
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt', 'tomas.txt']

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass or
        msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        return("\n" + msg)
    else:
        # count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        # print("The file " + filename + " has about " + str(num_words) + " words.")
        return("\nThe file " + filename + " has about " + str(num_words) + " words.")

with open('results.txt', 'w') as output:
    for filename in filenames:
        output.write(count_words(filename))

for filename in filenames:
    count_words(filename)
