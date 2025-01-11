# CHAT_BOT
Building  Chatbot with Google Gemini API and Streamlit 

Overview 
This  guide  provides  instructions  on  how  to  set  up  and  run  a  chatbot  using  Google’s 
Gemini API and Streamlit within Visual Studio Code (VS Code). 

Prerequisites 
●  Python (3.7 or later) 
●  Google API key  Get API key 
●  Streamlit library 
●  Vs Code 

Create a Project Folder 
1.  Create a New Folder: 
○  In your file system, create a new folder for your project, e.g.,  chatbot . 
2.  Open the Folder in VS Code: 
○  Open VS Code. 
○  Go to  File  >  Open Folder...  and select the folder you created. 

Install dependencies 
pip install streamlit google-generativeai python-dotenv 

Configure Environment Variables 
1.  Create a  .env  File: 
○  In your project directory, create a file named  .env . 
Add the following line to the file, replacing  YOUR_API_KEY  with your actual API key: 
GOOGLE_API_KEY = YOUR_API_KEY 


Set Environment Variable: 
Ensure the  GOOGLE_API_KEY  is loaded into your environment using  python-dotenv . 
The following Python code will automatically load this key from the  .env  file. 
Create a python file – > main.py 


Run the App: 
Execute the following command to start the Streamlit server: 
streamlit run mainpy 
Open your web browser and navigate to  http://localhost:8501  to interact with your 
chatbot.
