NB : this has been made in a few hours, for a workshop at school. Don't implement this as is !

# SafeBot: Your Companion in Combating Workplace Sexual Harassment

SafeBot embodies the pinnacle of artificial intelligence meeting empathy, manifest in a web application aimed at providing solace and actionable help to individuals navigating the murky waters of workplace sexual harassment. With a rich repository of resources and a compassionate chatbot powered by a Large Language Model (LLM) - LLAMA-2-CPP, SafeBot is not just an app, but a companion in your journey towards justice and healing.

## Highlights

- **Intuitive Interface**: Easy to navigate, user-friendly, and accessible to everyone, ensuring a seamless user experience.
- **Informative Resources**: A comprehensive database providing essential information on legal recourse, supportive communities, and much more.
- **Empathetic Chatbot**: A conversational agent ready to lend a listening ear and provide assistance, powered by the robust LLAMA-2-CPP.
- **Privacy-Centric**: Your interactions are held with the utmost confidentiality, ensuring a safe space for you to express and seek help.

## Setting Sail with SafeBot: Installation Guide

### For Debian-based Systems:

#### 1. Clone the Repository:
```bash
git clone https://github.com/AnodeGrindYo/SafeZone_Chatbot.git
cd SafeZone_Chatbot/projet/
```

#### 2. Package Installation:
```bash
pip3 install -r requirements.txt
```

#### 3. Language Model Deployment:
Download and compile the LLAMA-2-CPP language model using the provided script (all the tools are provided in this script):
```bash
chmod +x model/install_llama_2.sh && ./model/install_llama_2.sh
```

**Note:** In certain configurations, it might be necessary to modify the permissions of downloaded files using chmod.

#### 4. Server Initialization:
```bash
chmod +x start_server.sh && ./start_server.sh
```

To halt the server, simply use:
```bash
Ctrl + C
```

#### 5. Going Live with Nginx:
- Install Nginx:
```bash
sudo apt install -y python3-pip nginx
```

- Create Configuration File:
```bash
sudo vim /etc/nginx/sites-enabled/fastapi_nginx
```

- Configure Nginx:
```bash
server {
        listen 80;
        server_name XX.XX.XX.XXX; # Your EC2 Instance's Public IPV4
        location / {
                proxy_pass http://127.0.0.1:8000;
        }
}
```

- Restart Nginx:
```bash
sudo service nginx restart
```

With SafeBot now deployed, you're not alone in confronting workplace harassment. We're here with you, every step of the way.

![](https://cdn.discordapp.com/attachments/1160907035311886339/1162223545393360946/demo.gif?ex=653b2806&is=6528b306&hm=8a1c95889300b3e3f012c38e3d6831633fbfb18b3eb4de80e974a00c06fe89c2&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162081297175420989/image.png?ex=653aa38b&is=65282e8b&hm=f022709b75e34834e69edb799fa95d1c970d99174fc11ba4727487324ae88ffa&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162082969729630360/image.png?ex=653aa51a&is=6528301a&hm=b8398a48de7620cbb20fe2a299147e463ecfc83070966c802b981c52d97002a7&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162081602109722705/image.png?ex=653aa3d4&is=65282ed4&hm=713b3870cb93c17af0dfde82d2b472cf36b9eeb4bbe928daa2f9a3758fb02578&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162081723153141801/image.png?ex=653aa3f1&is=65282ef1&hm=65c189f61e783f007eaea64266e907faca3b3e6fc76278891558fdfe910ff9b2&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162081834457387169/image.png?ex=653aa40b&is=65282f0b&hm=05078574acc78dc6bc3b70a3cc3b90567b8959359c034a7fc9a1d312fd2336a5&)

![](https://cdn.discordapp.com/attachments/932672918859702355/1162081980142342256/image.png?ex=653aa42e&is=65282f2e&hm=44433602d6ff62fdb6e7fafedfd487a844f0a60e05528224410dde921e992aa4&)
