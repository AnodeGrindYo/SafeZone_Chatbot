# Project Title: Chatbot Assistance for Victims of Sexual Harassment in the Professional Environment

## Introduction
- Responsive web application dedicated to businesses, aimed at providing immediate and anonymous support to victims of sexual harassment via an intelligent chatbot.

## Strategic Choices
- **Web App**: Universal accessibility without the need for installation, accessible on any connected device, which encourages use and guarantees accessible help at all times.
- **LLM-based chatbot**: Provides natural, understandable and empathetic interactions, crucial for sensitive topics like sexual harassment.


## Key Technologies
- **Frontend**: Bootstrap for responsive design.
- **Backend**: FastAPI for a powerful and reliable API.
- **Chatbot Engine**: LLaMA-2-CPP (C++ port of LLaMA-2) for advanced user interaction.

## Architecture
- Modular design with a dedicated `Chat` class to encapsulate the interaction with LLaMA-2-CPP.
- Backend developed in FastAPI, guaranteeing performance and ease of development.
- Use of Bash scripts for automating server installation and configuration.

## Advantages of LLaMA-2-CPP
- **Optimization for Dialogue**: Models refined specifically for dialogue use cases.
- **Efficiency and Performance**: Faster and more efficient compared to larger models.
- **Open Source**: Flexibility and accessibility for research and commercial exploitation.

## Local Deployment
- Using WSL Debian to run the server locally.
- Exposure of the server to the Internet via ngrok for easy and secure access.
- Bash scripts for simplified installation, compilation and configuration of LLaMA-2-CPP.

## Documentation and Replicability
- Full instructions provided in the `README.md` file for installing and uploading to a Debian server via nginx.
- Bash scripts to automate the installation of dependencies, compilation and configuration of LLaMA-2-CPP, and server launch.

## Performance and scalability
- FastAPI offers high performance and scalability.
- LLaMA-2-CPP enables fast and precise interactions with users.
- Ability to extend the chatbot with additional features and integrate other technologies as needed.

## Security and Privacy
- Compliance with security and confidentiality standards in the processing of sensitive data.
- Careful design to ensure user safety and protection of their information.

## Social impact
- Provides crucial support to victims of sexual harassment in the workplace.
- Encourage a safe corporate culture and support harassment awareness and prevention.

## Benefits for Businesses
- **Immediate Response**: The chatbot offers an immediate response to employees, providing initial support in the event of harassment.
- **Anonymity**: Allows victims to speak freely, which can encourage reporting of incidents.
- **Education**: Provides valuable information on how to deal with sexual harassment, educating both employees and employers.
- **Cost Savings**: Reduces the burden on human resources by providing automated responses while maintaining human interaction thanks to the intelligence of the LLM.
- **Improving Corporate Culture**: Contribute to a safe and respectful corporate culture by providing support and education around sexual harassment.
- **Legal Compliance**: Helps companies comply with legal obligations regarding the prevention and treatment of sexual harassment.


## Conclusion
- Innovative project that combines modern technologies and positive social impact.
- Robust and reliable solution that addresses a critical societal problem with an advanced technological approach.