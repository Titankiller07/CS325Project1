import ollama

file_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325\\Project1.txt"
file_path2 = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325\\Project1Response.txt"
with open(file_path, 'r') as file:
    lines = file.read()

#Now, lines is a list where each element is a line from the file
print(lines)
response = ollama.generate(model="phi3",prompt = lines)
print("\nResponse: " + response['response'])
print("\nDone")

with open(file_path2, 'w') as file2:
     file2.write(response["response"])