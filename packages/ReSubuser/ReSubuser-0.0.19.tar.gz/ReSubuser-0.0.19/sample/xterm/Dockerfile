FROM debian
RUN apt-get update && apt -y upgrade
RUN apt install -y git xterm curl libgtk2.0 libxss1 gconf2 libnss3 libpulse0 libasound2
RUN apt install -y wget
RUN apt-get autoremove - && rm -rf /var/lib/apt/lists/*


