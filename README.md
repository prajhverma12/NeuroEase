# NeuroEase - Enhancing Digital Accessibility for Neurodivergent Individuals

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![GitHub Issues](https://img.shields.io/github/issues/prajhverma12/NeuroEase)](https://github.com/prajhverma12/NeuroEase/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/prajhverma12/NeuroEase)](https://github.com/prajhverma12/NeuroEase/pulls)

## Project Description

NeuroEase is a comprehensive web application and Chrome extension designed to improve digital accessibility for neurodivergent individuals, including those with autism, dyslexia, and Tourette’s syndrome. It addresses challenges in reading comprehension, information processing, and communication by integrating key assistive technologies:

* **Text Summarization:** Condenses long-form content into concise, easy-to-read summaries, reducing cognitive overload.
* **Text-to-Speech (TTS):** Converts written text into spoken words, aiding individuals with reading impairments like dyslexia.
* **Speech-to-Text (STT):** Transcribes spoken words into written text, facilitating communication for those with verbal difficulties.
* **Sentiment Analysis:** Interprets the emotional tone of text, assisting in understanding social and professional interactions.

This project aims to create a more inclusive digital environment, empowering neurodivergent users to interact with online content effectively and confidently.

## Features

* **User Authentication:** Secure registration and login.
* **Mental Health Assessments:** Integrated tests to identify and manage mental health concerns.
* **Text Summarization (Chrome Extension/Web):** Summarize web pages and text.
* **Text-to-Speech (TTS):** Listen to text read aloud.
* **Speech-to-Text (STT):** Convert speech to text.
* **Sentiment Analysis:** Analyze the emotional tone of text.
* **Database Storage:** Stores user data and test results securely.
* **Responsive Design:** Accessible across various devices.

## Technologies Used

* **Frontend:** React.js
* **Backend:** Node.js, Express.js
* **Database:** MongoDB
* **Authentication:** JWT (JSON Web Tokens)
* **Chrome Extension:** JavaScript, HTML, CSS
* **Natural Language Processing (NLP):** For Summarization and Sentiment analysis.

## Getting Started

### Prerequisites

* Node.js and npm installed
* MongoDB installed and running
* Chrome browser (for extension)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/prajhverma12/NeuroEase.git](https://github.com/prajhverma12/NeuroEase.git)
    cd NeuroEase
    ```

2.  **Install backend dependencies:**

    ```bash
    cd server
    npm install
    ```

3.  **Install frontend dependencies:**

    ```bash
    cd ../client
    npm install
    ```

4.  **Configure environment variables:**

    * Create a `.env` file in the `server` directory.
    * Add your MongoDB connection string and JWT secret. Example:

        ```
        MONGODB_URI=your_mongodb_connection_string
        JWT_SECRET=your_jwt_secret
        ```

5.  **Run the application:**

    * Start the backend server:

        ```bash
        cd ../server
        npm start
        ```

    * Start the frontend development server:

        ```bash
        cd ../client
        npm start
        ```

6. **Chrome Extension**
    * Load unpacked extension in chrome from the chrome-extension directory.

## Future Enhancements

* Integration with desktop and mobile platforms.
* Enhanced NLP algorithms for improved accuracy.
* Expanded mental health resources and support.
* Improved UI/UX for better accessibility.
* Comprehensive testing and security audits.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues to report bugs or suggest new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or inquiries, please contact:

* [Your Email Address]
* [Your GitHub Profile]
