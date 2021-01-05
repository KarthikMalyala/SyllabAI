import docx2txt
import re

# Install docx2txt using the commands on the blog page Karem sent us
# Can be done for PDF as well but that's a different library

class resume:
    # Extracts whole text from resume
    def extract_text_from_doc(doc_path):
        temp = docx2txt.process(doc_path)
        text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
        return ' '.join(text)

    # Tries and finds email based on key symbols stated below
    def extract_email(txt):
        email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", txt)
        if email:
            try:
                return email[0].split()[0].strip(';')
            except IndexError:
                return None

# Put your own file path here
txt = resume.extract_text_from_doc("C:\Career Documents\Test.docx")
outputEmail = resume.extract_email(txt)
print(outputEmail)

