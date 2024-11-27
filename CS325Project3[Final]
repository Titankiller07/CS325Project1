import ollama
import os

# Output file path pattern for saving results
output_file_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Reviews_{}.txt"
output_response_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Responses_{}.txt"

class OllamaModel:
    def __init__(self, model_name):
        self.model_name = model_name
        print(f"Model '{self.model_name}' is set.")

    def ask_question(self, question):
        # Ask the model to classify sentiment as positive, negative, or neutral.
        try:
            # Modify the question to ensure clarity and a one-word response
            question = f"Is the following statement positive, negative, or neutral? Respond with only one word: {question.strip()}"
            response = ollama.generate(model=self.model_name, prompt=question)
            response_text = response.get('response', "").strip().lower()

            # Return one of the three acceptable responses. Default to 'neutral' if not recognized.
            if response_text in ['positive', 'negative', 'neutral']:
                return response_text
            else:
                return "neutral"  # Default to "neutral" if an unexpected response is given
        except Exception as e:
            print(f"Error while asking the question: {e}")
            return "Error"

class FileReader:
    def __init__(self, file_path_pattern, num_files=5, file_extension='.txt'):
        #Initialize the FileReader with the base file path and number of files.
        
        #param file_path_pattern: Path pattern for the file names.
        #param num_files: Number of files to read (default is 5).
        #param file_extension: File extension (default is '.txt').
        self.file_path_pattern = file_path_pattern
        self.num_files = num_files
        self.file_extension = file_extension
        self.files_content = {}

    def read_files(self):
        #Read content from multiple files.
        for i in range(1, self.num_files + 1):
            file_name = self.file_path_pattern.format(i)
            if os.path.exists(file_name):
                try:
                    # Open file with 'utf-8' encoding to avoid decoding issues
                    with open(file_name, 'r', encoding='utf-8') as file:
                        self.files_content[file_name] = file.readlines()
                except UnicodeDecodeError as e:
                    print(f"Error decoding file {file_name}: {e}")
                    self.files_content[file_name] = []
            else:
                print(f"File {file_name} not found.")
                self.files_content[file_name] = []

    def get_lines(self, file_name):
        #Get lines from a specific file.
        return self.files_content.get(file_name, [])

class SentimentAnalyzer:
    def __init__(self, ollama_model, file_reader, output_path_pattern):
        #Initialize the SentimentAnalyzer with a model and file reader.
        self.ollama_model = ollama_model
        self.file_reader = file_reader
        self.output_path_pattern = output_path_pattern

    def analyze_lines(self):
        #Analyze each line in the files and classify the sentiment.
        for i in range(1, self.file_reader.num_files + 1):
            file_name = self.file_reader.file_path_pattern.format(i)
            lines = self.file_reader.get_lines(file_name)

            print(f"\nAnalyzing file: {file_name}")
            
            # Prepare output file for this file's responses
            response_file_name = self.output_path_pattern.format(i)
            with open(response_file_name, 'w') as response_file:
                # Write header or file-specific information if needed
                response_file.write(f"Sentiment Analysis Results for {file_name}\n")
                response_file.write("=" * 60 + "\n")

                # Process each line
                for line_number, line in enumerate(lines, start=1):
                    #print(f"Line {line_number}: {line.strip()}")
                    question = f"Using one term is this statement positive, negative, or neutral?: {line.strip()}"

                    response = self.ollama_model.ask_question(question)

                    if response:
                            # Write the Ollama response (only the sentiment)
                            response_file.write(f"{response}\n")
                            print(f"Response: {response}")
                    else:
                            response_file.write("No response\n")
                            print("No response from the model.")
                    print("-" * 40)

                # End of response file
                response_file.write("=" * 60 + "\n")
                response_file.write("\n")

# Example Usage
if __name__ == "__main__":
    # Initialize the Ollama model
    model_name = "phi3"  # You can change this to any available model like "llama2"
    ollama_model = OllamaModel(model_name)

    # Initialize the FileReader with the base file path and number of files.
    file_reader = FileReader(output_file_path, 5)  # File path pattern is Reviews_1.txt, Reviews_2.txt, etc.
    file_reader.read_files()  # Read content from the files

    # Initialize the SentimentAnalyzer to process and classify sentiment
    sentiment_analyzer = SentimentAnalyzer(ollama_model, file_reader, output_response_path)
    sentiment_analyzer.analyze_lines()  # Analyze each line and get a sentiment response
