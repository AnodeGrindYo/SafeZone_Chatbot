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

