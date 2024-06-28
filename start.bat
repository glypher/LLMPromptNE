
C:\Users\suppo\MLENV\Scripts\activate

cd C:\Users\suppo\Desktop\LLMpromptNE

jupyter notebook


sudo docker build -t conf_llm_img .

sudo docker run -d --name conf_llm -p 8040:80 conf_llm_img
