# web-app-builder--LLM

https://github.com/george-mountain/web-app-builder--LLM/assets/19597087/4541e5f5-844d-4862-8745-bac3436de6ec


# Web Builder App

Web Builder App is a Streamlit-based application that allows users to upload an image, generate code based on the contents of the image, and view the code implementation.

## Table of Contents
- [Data Flow Diagram](#data-flow-diagram)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Generating Executable](#generating-executable)
- [License](#license)


## Data Flow Diagram
![dataFlow](https://github.com/george-mountain/web-app-builder--LLM/assets/19597087/827cfd54-ef13-4040-8184-8a93f097b5af)



## Getting Started

### Prerequisites

Make sure you have the following software installed on your machine:

- Python 3.8 or later
- Pytorch Cuda: CUDA Version >=11.8. Install from here - [Pytorch CUDA Installation](https://pytorch.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/web-builder-app.git
   cd web-builder-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   - For Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - For Linux/Mac:

     ```bash
     source env/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create .env file:
    Create .env file and place your API keys in the file. A sample of how to do this is seen on the .env file


## Usage

### Running the Application

To run the application locally:

```bash
streamlit run main.py
```

Visit the provided URL in your web browser to interact with the application.

### Generating Executable

To create an executable file for your application:

```bash
pyinstaller --onefile --name "Web Builder App" --exclude-module google.api main.py
```

The executable will be located in the `dist` folder.


## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/) file for details.
```
