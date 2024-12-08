
# Advanced Speech Recognition System using Whisper AI  

![Project Banner](https://github.com/user-attachments/assets/f1395105-bff6-4263-a8b7-40b3056b37c8)


## 🚀 Abstract  
This project showcases an **Advanced Speech Recognition (ASR) System** that transcribes audio to text in real time using OpenAI's **Whisper AI** model. With support for multilingual transcription, noise robustness, and a user-friendly web interface, this tool offers efficient voice-to-text applications for transcription, dictation, and voice-based user interfaces.

---

## 🔍 Motivation  
Voice-driven technologies are revolutionizing industries like **healthcare**, **customer service**, and **accessibility**. Existing systems often face challenges in noisy environments, handling accents, or processing multiple languages. This project addresses these gaps by leveraging the Whisper model's versatility and accuracy to build a **scalable, real-time ASR system**.

---

## 🎯 Problem Definition  
Traditional speech recognition systems are hindered by:  
- 🚫 High latency  
- ❌ Limited accuracy in noisy environments  
- 🌐 Poor multilingual support  
- 🔒 Privacy concerns due to reliance on cloud services  

This project tackles these issues, aiming for **real-time**, **accurate**, and **multilingual transcription**, all while maintaining robust privacy measures.

---

## 🌟 Features  
### 📝 **Key Capabilities**:  
- **Real-time Transcription**: Accurate audio-to-text conversion.  
- **Multilingual Support**: Dynamic recognition of multiple languages.  
- **Noise Robustness**: Enhanced transcription in noisy environments.  
- **User-Friendly GUI**: Intuitive web interface for seamless interaction.  

### 🎯 **Future Scope**:  
- Enhanced real-time conversion for time-sensitive applications.  
- Support for additional use cases like subtitles and live translations.

---

## 🛠️ System Architecture  

### **Workflow**  
1. **Input and Preprocessing**:  
   - Context-aware transcription using past tokens.  
   - Starts transcription pipeline upon receiving audio data.  

2. **Language and Speech Detection**:  
   - Automatic language identification for multilingual support.  
   - Voice activity detection to filter non-speech audio.  

3. **Transcription and Translation**:  
   - **Time-aligned Transcription**: With timestamps for precise indexing.  
   - **Text-only Transcription**: Continuous text output.  
   - Optional **translation** from non-English to English.

4. **Output Generation**:  
   - Generates time-stamped or continuous text.  
   - Marks transcription completion per audio segment.  

![Architecture Diagram](https://github.com/user-attachments/assets/32a43cd9-e30e-4305-8e82-11a6669be80c)


---

## 💻 Technology Stack  
### **Software**  
- **Streamlit**: Web-based user interface.  
- **Whisper AI**: Speech-to-text engine.  


**Deployment:**  
- **Platform**: Streamlit Cloud  
- **Deployment Link**: [Hertz ASR App](https://hertz-asr.streamlit.app/)

### **Networking and Infrastructure**  
- High-speed internet for real-time services.  
- Scalable cloud-based infrastructure.  

---

## 🚀 Getting Started  

### Clone the Repository  
```bash  
git clone https://github.com/AE-Hertz/speech-to-text/  
cd advanced-speech-recognition  
```  

### Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Run Locally  
```bash  
streamlit run app.py  
```  

---

## 🤝 Contributions  
We welcome contributions to improve this project! Please:  
1. Fork the repository.  
2. Create a feature branch.  
3. Submit a pull request.  

---

## 📄 License  
This project is licensed under the [MIT License](LICENSE).  

---

## 🛡️ Acknowledgments  
- **OpenAI** for the Whisper model.  
- **Streamlit** for the web development framework.  

---

![Banner(2)](https://github.com/user-attachments/assets/dd2b557c-0683-41a6-8a87-254d524df093)


Happy coding! 😊  

 
