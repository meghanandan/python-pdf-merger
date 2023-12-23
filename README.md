# PDF Merger with Bootstrap and Python

A simple web application that enables users to upload multiple PDF documents, merge them using a Python script, and generate a download link for the merged PDF file.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The PDF Merger with Bootstrap project provides a user-friendly interface for merging multiple PDF documents. Users can easily upload their PDF files through the web interface, and the server-side Python script will merge them into a single PDF file. A download link is then generated for the user to obtain the merged PDF.

## Features

- Upload multiple PDF documents.
- Merge PDFs into a single file.
- Responsive and intuitive user interface using Bootstrap.
- Secure file handling on the server.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- Flask
- PyPDF2 (Python library for PDF manipulation)
- Bootstrap (included in the project)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/meghanandan/python-pdf-merger.git
    cd python-pdf-merger
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

3. Use the web interface to upload multiple PDF documents.

4. Click the "Merge" button to combine the uploaded PDFs.

5. Once the merge is complete, a download link will be provided for the merged PDF file.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
