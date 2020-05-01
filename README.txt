README

OVERVIEW

REQUIREMENTS

System: Windows 10(for demo) or server with Apache(for production)
Python 3.8.2+
Python Dependencies:
    appdirs 1.4.3
    asgiref 3.2.7
    bleach 3.1.5
    click 7.1.2
    distlib 0.3.0
    Django 3.0.5
    filelock 3.0.12
    joblib 0.14.1
    markdown2 2.3.8
    nltk 3.5
        nltk libraries: stopwords and punkt
    numpy 1.18.3
    packaging 20.3
    pbr 5.4.5
    pyparsing 2.4.7
    pytz 2020.1
    regex 2020.4.4
    scikit-learn==0.22.2.post1
    scipy 1.4.1
    six 1.14.0
    sqlparse 0.3.1
    stevedore 1.32.0
    tqdm 4.45.0
    virtualenv-clone 0.5.4
    webencodings 0.5.1h



INSTALLATION

Windows installation guide:
    Download and install version python 3.8.2+

Ensure that Windows Command Prompt has access to Python commands:
    1. Go to Control Panel
    2. Go to System
    3. On left side of System window select Advanced system settings.
    4. At the bottom of the System Properties window, select Environment Variables
    5. Under "System Variables" select and double click  "Path", A new window will appear
    6. Click New then Browser on the right side of the new window
    7. In the "Browse For Folder", Navigate to you Python installation and select "Python38-xx" file
        Example Python Install location(Try this path, but may differ depending on system):
        This PC -> Windows(C:) -> Users -> [Name of User] -> AppData -> Local -> Programs -> Python -> Python 3.8-32
    8. Click OK in Edit environment variable window
    9. Click OK in Environment Variables window
    10. Click OK in System Properties window
    11. Test configuration by opening a Command Prompt window and typing "python -V" and you should see Python 3.8.x


Install program and python dependencies:
    1. Extract Cyber-Security-Knowledge-Base file to desired location
    2. Start command prompt and navigate, utilizing cd command, to the /Cyber-Security-Knowledge-Base program location
        in command prompt
    3. To install dependencies type "python -m pip install -r requirements.txt"
    4. Wait for installation to complete

Install nltk required libraries:
    1. Open Command prompt
    2. Type "python -m nltk.downloader stopwords"
    3. Type "python -m nltk.downloader punkt"
    4. Allow both files to finish download.

STARTING PROGRAM
    1. Open Command Prompt
    2  Navigate to the Cyber-Security-Knowledge-Base/Cyber_Security_KBMS project location utilizing command prompt

RESOURCES



