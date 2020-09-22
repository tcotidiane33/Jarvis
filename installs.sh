# looks for brew installation and installs only if brew is not found in /usr/local/bin
check=$(which brew)
condition="/usr/local/bin/brew"
if [[ "$check" != "$condition" ]]; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi
#python3 -m venv venv
brew install portaudio
pip install --upgrade pip
python3 -m pip install SpeechRecognition
python3 -m pip install PyAudio
python3 -m pip install numpy
python3 -m pip install pyttsx3
python3 -m pip install pytemperature
python3 -m pip install psutil
python3 -m pip install wikipedia
python3 -m pip install newsapi-python
python3 -m pip install pyrh
python3 -m pip install pytz
python3 -m pip install selenium
python3 -m pip install ChatterBot==1.0.0
python3 -m pip install chatterbot-corpus==1.2.0
# looks for google chrome version and installs the right chromedriver version
echo "*** Checking your chrome version to install chromedriver ***"
chrome_v=$(/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version)
echo $chrome_v
raw_v=$(echo $chrome_v | grep -Eo '[0-9]+([.][0-9]+)' | tr '\n' ' '; echo "")
big_v=${raw_v%.*}
v=$(echo $big_v | tr ' ' '.';)
python3 -m pip install chromedriver-py==$v.*