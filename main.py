#used to download the videos
import yt_dlp
import ffmpeg
import soundfile as sf
import librosa as lr
import os

#https://youtu.be/dPNVJZP3i5g <- This is the test url i've been using, it's a song

def downloadmp3(url, save_path):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = os.path.join(save_path, f"{info['title']}.mp3") #chatgpt wrote this line
        return filename

def effectsMenu(filename):
    output_file = filename.replace(".mp3", "_processed.mp3")
    print("Please select one of the following options: "
          "1 - Tempo, 2 - Transpose, 3 - Quit: ")
    fxChoice = input("Enter choice here: ")
    #match case statement
    match fxChoice:
        case "1":
            tempomethod = input("Choose from the following options: "
                "\n\t1 - Change tempo by percentage"
                "\n\t2 - Enter tempo manually"
                "\nEnter choice here: ")
            changeTempo(filename, output_file, tempomethod)

        case "2":
            semitones = int(input("Enter number of semitones to transpose by: "))
            transpose(filename, output_file, semitones)
        case "3":
            exit()
        case default:
            print("Please enter a valid number")

def changeTempo(filename, output_file, tempomethod):
    y, sr = lr.load(filename)
    match tempomethod:
        case "1":
            newrate = float(input("Enter new playrate to change tempo (default 1.0): "))
            y_stretched = lr.effects.time_stretch(y, rate=newrate)
            sf.write(output_file, y_stretched, sr)
        case "2":
            tempo1 = float(input("Enter original tempo: "))
            tempo2 = float(input("Enter new tempo: "))
            newrate = tempo2 / tempo1
            print(newrate)
            y_stretched = lr.effects.time_stretch(y, rate=newrate)
            sf.write(output_file, y_stretched, sr)
        case default:
            print(f'Error: {tempomethod} is not a valid selection')
    filename = output_file

def transpose(filename, output_file, semitones):
    y, sr = lr.load(filename)
    #semitones is the number of stemps to raise or lower the pitch of the song by
    y_pitched = lr.effects.pitch_shift(y, sr=sr, n_steps=semitones)
    sf.write(output_file, y_pitched, samplerate=sr)
    filename = output_file

def main():
    save_path = "./downloads"
    os.makedirs(save_path, exist_ok=True)
    url = input("Please enter a valid YouTube video URL: ").strip()
    filename = downloadmp3(url, save_path)
    addEffects=input("Would you like to add any post-processing to the file? (y/n): ")
    if addEffects=="y":
        effectsMenu(filename)
        while addEffects=="y":
            # coded this way so I can process multiple effects
            output_file = filename.replace(".mp3", "_processed.mp3")
            addEffects = input("Would you like to add any more post-processing to the file? (y/n): ")
            if addEffects!="y":
                break
            else:
                effectsMenu(output_file)
        #This line is here to make sure the file doesn't have "_processed.mp3" added 4 times to the filename
        os.rename(output_file, filename.replace(".mp3", "_processed.mp3"))

main()