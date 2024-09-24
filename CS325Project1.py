import ollama

file_path = "C:\\Users\\sharkfin\\Downloads\\CS325\\Project1.txt"
file_path2 = "C:\\Users\\sharkfin\\Downloads\\CS325\\Project1Response.txt"
with open(file_path, 'r') as file:
   lines = file.read()

#Now, lines is a list where each element is a line from the file
print(lines)
        
response = ollama.generate(model="phi3", prompt=lines)
print("\nResponse: " + response['response'])

with open(file_path2, 'w') as file2:
    file2.write(response["response"])
