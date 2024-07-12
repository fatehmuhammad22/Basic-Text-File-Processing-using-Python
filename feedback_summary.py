def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def count_feedback_entries(feedback_lines):
    return len(feedback_lines)

def extract_keywords(feedback_lines, keywords):
    keyword_counts = {keyword: 0 for keyword in keywords}
    for line in feedback_lines:
        for keyword in keywords:
            keyword_counts[keyword] += line.lower().count(keyword)
    return keyword_counts

def generate_summary_report(feedback_count, keyword_counts):
    report = []
    report.append(f"Total number of feedback entries: {feedback_count}")
    for keyword, count in keyword_counts.items():
        report.append(f"{keyword.capitalize()}: {count}")
    return "\n".join(report)

def save_report(report, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(report)

def main(input_file_path, output_file_path, keywords):
    feedback_lines = read_file(input_file_path)
    feedback_count = count_feedback_entries(feedback_lines)
    keyword_counts = extract_keywords(feedback_lines, keywords)
    summary_report = generate_summary_report(feedback_count, keyword_counts)
    save_report(summary_report, output_file_path)
    print("Summary report generated and saved successfully.")

if __name__ == "__main__":
    input_file_path = "customer_feedback.txt"
    output_file_path = "summary_report.txt"
    keywords = ["good", "bad", "excellent", "poor"]
    main(input_file_path, output_file_path, keywords)
