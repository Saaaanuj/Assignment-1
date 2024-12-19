# Google Image Downloader with Email Attachment

## Overview

This project allows users to download images from Google using a keyword, compress the images into a ZIP file, and email the file to a specified recipient. The script uses Python libraries such as `icrawler` for image crawling and `smtplib` for email functionality.

---

## Features

- **Search and Download Images**: Automatically downloads images based on user-provided keywords.
- **File Compression**: Compresses all downloaded images into a single ZIP file for convenience.
- **Email Delivery**: Sends the ZIP file as an email attachment.
- **User-Friendly Workflow**: Simple command-line interface for inputs.

---

## Prerequisites

1. **Python 3.x** installed on your system.
2. Install required Python packages using:
   ```bash
   pip install icrawler
   ```
3. Gmail account for sending emails. Ensure you:
   - Enable "Less secure app access" or create an App Password.

---

## Installation

1. Clone this repository:
   
2. Navigate to the project directory:
   
3. Install dependencies:
   

---

## Usage

Run the script by executing:
```bash
python main.py
```

### Input Prompts
1. **Keyword**: The search term for downloading images (e.g., `nature`).
2. **Number of Images**: Specify the number of images to download.
3. **Recipient Email**: Enter the email address to send the ZIP file.

### Example Execution
```bash
Enter the keyword to search for images: nature
Enter the number of images to download: 5
Enter your email address: example@gmail.com
```

---

## Code Explanation

### Main Functions

- **`download_and_send_images`**:
  - Downloads images using `GoogleImageCrawler`.
  - Compresses downloaded images into a ZIP file.
  - Sends the ZIP file via email.

- **`send_email_with_attachment`**:
  - Handles SMTP-based email sending.
  - Attaches the ZIP file to the email.

### Directory Structure
Downloaded images and the ZIP file are stored in the user's `Downloads` directory:
```
Downloads/
  downloaded_images/
    image1.jpg
    image2.jpg
  images.zip
```

---

## Error Handling

- **File Management**: Ensures necessary directories are created automatically.
- **Email Delivery**: Validates email sending and logs any errors.
- **General Exceptions**: Captures and logs unexpected errors for debugging.

---

## Future Enhancements

- **OAuth Integration**: Implement OAuth for secure email authentication.
- **Multi-Source Support**: Add functionality to download images from other sources like Bing or Flickr.
- **GUI Interface**: Create a graphical interface for easier user interaction.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as needed.

---
