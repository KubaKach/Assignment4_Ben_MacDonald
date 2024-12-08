This program is used to download audio from youtube videos to your computer, but with the ability to change pitch and tempo.
It will ask you for a youtube URL. Paste your desired URL and it will download it, then prompt you with options for
post-processing.
This is the link to the GitHub repo: https://github.com/KubaKach/Assignment4_Ben_MacDonald.git

Here's the link to the dockerhub repository: https://hub.docker.com/repository/docker/dockingchampion/audio-manipulator/general

Here is the docker pull command: docker pull dockingchampion/audio-manipulator

If you are using windows, open powershell and write "docker run -it --rm -v ${PWD}/downloads:/app/downloads audio-manipulator" 

If you are using Linux, use the same command in the terminal.

note for Saad:
This was my 3rd attempt at making a Git repository for this assignment, it didn't go well the first two times. As a result, my 
first failed attempt was named "fail" and my second one was named "Assignment4". Those repos are still up. 

I also struggled a lot with making the docker container, after multiple failures I asked ChatGPT to guide me so I could better
understand. The link to that conversation is right here: https://chatgpt.com/share/6754d71c-dfa4-800d-b590-1af2b900b853

I screwed up a lot, but I learned a lot from it. Even if ChatGPT carried me throughout this assignment, I made sure to go 
over every step in its response to better understand how to dockerize my applications. I'm not really expecting any other 
grade than a 0 because of how late I gave this assignment in, and because of my usage of chatGPT. Regardless, it was a good 
learning experience for me because of two things:
  1. I really got to learn how docker worked because I tried troubleshooting on my own, and then tried following multiple
     youtube tutorials before finally giving up and asking chatGPT.
  2. I learned that I need to start giving myself a troubleshooting time limit, because 2 hours of trying on my own
     and failing is acceptable because I do learn a lot from those experiences. However, this went on for 4 days, which
     is really bad because I'm giving it in way later than I should, and I ended up costing myself 4% of my total grade.

Anyways, hopefully I can do well enough on the final exam so I can prove that I spent time afterwards trying to understand
chatgpt's answers and not just "thanks for giving me the answers! I can forget about this now".

I don't plan on stopping here though, I plan on expanding this to where you can upload your own audio files for 
post-processing, and with many more options for effects to add to the files themselves.
