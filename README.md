# chatgpt-speaker-openai-whisper
A Voice assistant chatbot made with whisper speech to text and openai to generate responses to user queries. Features include speech recognition, text-to-speech conversion, and a customizable personality


[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project is a customizable voice assistant that uses machine learning to generate responses to user queries. It integrates two powerful APIs: `Pyttsx3` and `OpenAi`. Pyttsx3 is used for text-to-speech conversion, while OpenAI's text-based language model is used to generate responses to the user's questions. The voice assistant can be customized to suit different use cases and personalities. For example, it can be used to provide customer support, answer trivia questions, or even act as a personal companion.




<!-- GETTING STARTED -->
## Getting Started

To get started with the voice assistant, follow these steps:
Clone the repository to your local machine.

1) Install the required dependencies. See the next section for instructions.

2) Set up an OpenAI API key. You can get one by signing up for the OpenAI GPT-3 API at https://openai.com/api/.

3) Update the api_key variable in the code with your OpenAI API key.

4) Customize the personality of the voice assistant by modifying the prompt variable in the chat() function.

5) Run the main.py script to start the voice assistant.

### Prerequisites

Installing Dependencies
The voice assistant relies on the following dependencies:
Python 3.7 or later
Pyttsx3
OpenAI
pydub
numpy
whisper
torch

### Installation

You can install these dependencies using pip, the Python package manager. Here are the steps:
   ```sh
   git clone https://github.com/Gustavoandresai/chatgpt-speaker-openai-whisper.git
   ```
Run the following command to install dependencies:
`WHISPER` `OpenAi` `pyttsx3` `SpeechRecognition` `pydub` `torch` `numpy`
   ```sh
   pip install git+https://github.com/openai/whisper.git 
   ```
 
   ```sh
   pip install openai
   ```
   
   ```sh
   pip install pyttsx3
   ```
   
   ```sh
   pip install SpeechRecognition
   ```
   
   ```sh
   pip install pydub
   ```
   
   ```sh
   pip install torch

   ```
   
   ```sh
   pip install numpy

   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once you have installed the dependencies, you are ready to run the voice assistant.
Once you have installed these dependencies, you can use the record_audio() function in the mic.py file to record audio and the transcribe_forever() function to transcribe the audio into text.

Note that the transcribe_forever() function requires a trained model, which you can load using the whisper.load_model() function. The mic.py file provides an example of how to load and use a pre-trained model for English. You can modify this code to use a different language or a different model, as needed.

_Please refer to the [Documentation](https://openai.com/blog/whisper/)_



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->
## Contact

Gustavo Andres Barreto- - Barretoandres461@gmail.com

Project Link: [https://github.com/Gustavoandresai/chatgpt-speaker-openai-whisper](https://github.com/Gustavoandresai/chatgpt-speaker-openai-whisper)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-url]: https://github.com/Gustavoandresai/chatgpt-speaker-openai-whisper/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gustavoandresbarreto
[product-screenshot]: portfolio-9.jpg
