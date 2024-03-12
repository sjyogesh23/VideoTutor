**Team: Teen Wolves**

# Video Tutor

## Problem Statement

Students often find it challenging to locate answers to questions from video lectures and access supplementary materials efficiently. Content creators also face difficulties in organizing notes, summaries, and quizzes. A solution is needed to automate responses to student queries based on video content and provide easily accessible supplementary materials, enhancing the learning experience for both students and content creators.

## Proposed Solution

Utilizing advanced transformer models, we aim to convert video content into text and store it in a centralized database. Our system will employ transformer-based algorithms to analyze these transcripts, automatically generating structured notes and concise summaries. Leveraging transformer-based natural language processing (NLP) techniques, we will develop a robust Q&A system to provide relevant answers extracted from the transcript content. Integrating transformer-powered interactive elements such as quizzes and annotations into our video platform, we seek to ensure an engaging and effective learning experience. With a focus on designing a streamlined and intuitive interface, our goal is to revolutionize video learning by seamlessly capturing, transcribing, and incorporating interactive features to enhance educational engagement.

## Target Users

**Creator:**

- Content creators can upload video lectures and easily organize supplementary materials such as notes, summaries, and quizzes.
- They can efficiently generate structured notes and concise summaries through automated transcript analysis.
- The platform provides tools for creating interactive elements like quizzes and annotations, enhancing the engagement of their educational content.

**Student:**

- Students can access video lectures along with supplementary materials, making it easier to study and review course content.
- The Q&A system allows students to quickly find answers to their queries based on the video transcript.
- Interactive elements like quizzes provide an engaging learning experience, helping students reinforce their understanding of the material.

## Tech Stack

### Front-End:

- React JS
- Tailwind CSS
- React Bootstrap

### Machine Learning:

- NLTK
- easyOCR
- Whisper
- Googletransulator

## How to Run the Program

### Creator:

#### Server End:

```
cd Creator/server
python server.py
```

#### Front End:

```
cd Creator/client
npm start
```

### Student:

#### Server End:

```
cd student/server
python chatbot.py
```

#### Front End:

```
cd student/client
npm start
```

## Contributors

- [Your Name]
- [Teammate 1 Name]
- [Teammate 2 Name]

---

Feel free to add any additional information or instructions as needed. Good luck with your project!
