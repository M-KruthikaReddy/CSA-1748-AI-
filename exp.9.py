import string
input_string = input("Enter a string: ")
no_punctuations = input_string.translate(str.maketrans("", "", string.punctuation))

print("String with no punctuations:", no_punctuations)
