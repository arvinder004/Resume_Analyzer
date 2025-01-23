from pdfminer.high_level import extract_text
import re

def parse_resume(resume_path):
    try:
        text = extract_text(resume_path)
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
    
    extracted_data = {
        'name': '',
        'phone': '',
        'email': '',
        'skills': [],
        'experience': [],
        'education': [],
    }

    #name
    name_pattern = r"([A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+)"
    name_match = re.search(name_pattern, text)
    if name_match:
        extracted_data['name'] = name_match.group(0)

    #phone
    phone_pattern = r"(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        extracted_data['phone'] = phone_match.group(0)    
    
    #email
    email_pattern = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
    email_match = re.search(email_pattern, text)
    if email_match:
        extracted_data['email'] = email_match.group(0)
    
    #skills
    skills_pattern = r"\b(Python|Java|C\+\+|JavaScript|SQL|Machine Learning|Deep Learning|Data Science|AWS|Azure|Cloud|AI|HTML|CSS|React|Angular|Node.js|MongoDB|Docker|Kubernetes|DevOps|Agile|Scrum|Git|GitHub|AI|IoT|Cybersecurity|Networking|Operating Systems|C#|Go|Ruby|PHP|Swift|Kotlin|R|Scala|Rust|Perl|Objective-C|Data Mining|Natural Language Processing|Computer Vision|Data Analysis|Data Visualization|Statistics|Probability|Big Data|Data Engineering|Data Warehousing|Data Wrangling|Predictive Modeling|Reinforcement Learning|TensorFlow|PyTorch|Scikit-learn|Pandas|NumPy|Matplotlib|Seaborn|Tableau|Power BI|AWS EC2|AWS S3|AWS Lambda|Azure Functions|GCP Compute Engine|Cloud Computing|Cloud Security|DevOps|CI/CD|Jenkins|Git|GitHub|GitLab|Bitbucket|Docker|Kubernetes|Ansible|Terraform|CloudFormation|Azure DevOps|iOS|Swift|Objective-C|Android|Java|Kotlin|React Native|Flutter|Xamarin|Project Management|Communication|Teamwork|Leadership|Problem-solving|Critical Thinking|Business Analysis|Product Management|Marketing|Software Engineering|Algorithms|Data Structures|Design Patterns|Object-Oriented Programming|Testing|Debugging|Version Control|Blockchain)\b"
    skills_matches = re.findall(skills_pattern, text)
    extracted_data['skills'] = list(set(skills_matches))  # Remove duplicates

    #experience
    experience_pattern = r"([A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+)\s+\-+\s+([A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+)" 
    experience_matches = re.findall(experience_pattern, text)
    for company, role in experience_matches:
        extracted_data['experience'].append({'company': company, 'role': role})

    #education
    education_pattern = r"([A-Z\s]+)\n\n([A-Z,\s]+)\n\n([A-Z\s]+)\n\nCGPA\s*:\s*([\d.]+)\n\n([A-Z]{3}\.\s+\d{2})\s+–\s+([A-Z]{3}\.\s+\d{4})\s*\(expected\)" 
    education_matches = re.findall(education_pattern, text)
    for degree, institution in education_matches:
        extracted_data['education'].append({'degree': degree, 'institution': institution})

    return extracted_data;

resume_file = "/Users/arvinder004/Developer/ResumeAnalyzer/ResumeParser/ArvinderSinghDhoul_Resume.pdf"
extracted_info = parse_resume(resume_file)

if(extracted_info):
    print("Extracted Information:")
    print("Name: ", extracted_info['name'])
    print("Email: ", extracted_info['email'])
    print("Phone: ", extracted_info['phone'])
    print("Skills: ", extracted_info['skills'])
    print("Experience: ", extracted_info['experience'])
    print("Education: ", extracted_info['education'])