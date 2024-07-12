# Basic-Text-File-Processing-using-Python
The Feedback Summary Generator is designed to process customer feedback efficiently. The system includes features for reading a text file containing feedback entries, counting the total number of feedback entries, extracting specific keywords, counting the occurrences of each keyword, and generating a summary report.

## Description
This Python script processes a text file containing customer feedback, extracts specific keywords, and generates a summary report. The summary report includes the total number of feedback entries and the occurrences of each specified keyword.

## Requirements
- Python 3.x

## Usage

1. **Prepare the Input File:**
   Ensure you have a text file named `customer_feedback.txt` in the same directory as the script. This file should contain customer feedback entries, with each entry on a new line.

2. **Script Execution:**
   Run the script using the following command:
   ```sh
   python feedback_summary.py

3. **Output:**
The script will generate a summary report and save it to summary_report.txt in the same directory.

## Script Details
**Functions:**
1. **read_file(file_path):** Reads the content of the specified text file and returns it as a list of lines.
2. **count_feedback_entries(feedback_lines):** Counts the total number of feedback entries.
3. **extract_keywords(feedback_lines, keywords):** Extracts specified keywords from the feedback lines and counts their occurrences.
4. **generate_summary_report(feedback_count, keyword_counts):** Generates a summary report based on the feedback count and keyword counts.
5. **save_report(report, output_file_path):** Saves the generated report to the specified output file.

## Customization
You can customize the keywords by modifying the keywords list in the main function.

## Contact
For any questions or issues, please contact Fateh Muhammad at fateh.m0101@gmail.com.
