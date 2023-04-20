import os
import datetime
from flask import Flask, jsonify, request
import openpyxl

app = Flask(__name__)

@app.route('/submit-segmentation', methods=['POST'])
def submit_segmentation():
    # Get the selected segmentation types from the form data
    selected_segmentations = request.get_json()

    # Generate a unique filename based on the current date
    filename = 'segmentation_responses.xlsx'

    # Check if the file already exists
    file_exists = os.path.isfile(filename)

    # Load the existing workbook or create a new workbook
    if file_exists:
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Timestamp', 'Segmentation Type'])

    # Write the selected segmentation types and timestamp to the Excel worksheet
    timestamp = datetime.datetime.now()
    for segmentation_type in selected_segmentations:
        ws.append([timestamp, segmentation_type])

    # Save the workbook to the Excel file
    wb.save(filename)

    return jsonify({'message': f'Segmentation data saved to file {filename}.'})

if __name__ == '__main__':
    app.run(debug=True)
