def read_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def match_keywords(resume_text, keywords):
    matches = {keyword.strip().lower(): keyword.strip().lower() in resume_text.lower() for keyword in keywords}
    return matches

def main():
    resume_file_path = input("Enter the path to the resume file: ")
    keywords_input = input("Enter the keywords (comma-separated): ")
    
    resume_text = read_resume(resume_file_path)
    keywords = keywords_input.split(',')
    
    matches = match_keywords(resume_text, keywords)
    
    print("\nKeyword Matches:")
    for keyword, found in matches.items():
        status = "Found" if found else "Not Found"
        print(f"{keyword}: {status}")

if __name__ == '__main__':
    main()
