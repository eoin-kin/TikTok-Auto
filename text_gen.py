from openai import OpenAI
import os
from moviepy.editor import *
from moviepy.video import *
from dotenv import load_dotenv
import random
from gtts import gTTS
'''
load_dotenv()
adding a change
### Code works when I give them their blood money
client = OpenAI(os.getenv("API_Key"))

def get_completion(prompt, client_instance, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = client_instance.chat.completions.create(
  model=model,
  messages=messages,
  max_tokens=50,
  temperature=0,
  )
  return response.choices[0].message["content"]

prompt = "please say hi"
get_completion(prompt, client)
'''
### Using generated script from here on
files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)

files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)
        
files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)

footage = VideoFileClip("Minecraft Parkour Gameplay No Copyright.mp4",audio=False)
duration = int(footage.duration - 0.28)

start = random.randint(0,duration-60)
clip = footage.subclip(start,start+60)

clip = clip.resize((500,600))

### Only used until I pay openAI ###
file = open("Script.txt")
script = file.readlines()
file.close()
final_script =[]
for line in script:
  final_script.append(line.replace("\n",""))

clear = False
while not clear:
  try:
    final_script.remove("")
  except:
    clear = True
    break

### End of filler code ###

lines = len(final_script)

lines_min = 60//lines
start = 0
end = lines_min
for i in range(0,lines):
  sub_clip = clip.subclip(start,end)
  start += lines_min
  end += lines_min
  txt = TextClip(final_script[i],bg_color="white",method="caption",size=(400,300))
  txt = txt.set_position("center").set_duration(lines_min)
  speech = gTTS(text=final_script[i],lang="en")
  speech.save(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios\\audio number {i}.wav")
  f = CompositeVideoClip([sub_clip,txt])
  f.write_videofile(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips\\clip number {i}.mp4")
  audio = AudioFileClip(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios\\audio number {i}.wav")
  f = VideoFileClip(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips\\clip number {i}.mp4").without_audio()
  voiced = f.set_audio(audio)
  voiced.write_videofile(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced\\clip number {i}.mp4")
  print("Just finished line: ",i+1," of ",lines)
  audio.close()
  f.close()

clips = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced")
file_paths = []
for clip in clips:
    file_paths.append("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced\\"+clip)

def finish(*args):
  files = args[0]
  film_list =[]
  for file in files:
      foo = VideoFileClip(file)
      film_list.append(foo)
  
  video = concatenate_videoclips(film_list)
  return video
  
    

final = finish(file_paths)
final.preview()
        

from openai import OpenAI
import os
from moviepy.editor import *
from moviepy.video import *
from dotenv import load_dotenv
import random
from gtts import gTTS
'''
load_dotenv()
adding a change
### Code works when I give them their blood money
client = OpenAI(os.getenv("API_Key"))

def get_completion(prompt, client_instance, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = client_instance.chat.completions.create(
  model=model,
  messages=messages,
  max_tokens=50,
  temperature=0,
  )
  return response.choices[0].message["content"]

prompt = "please say hi"
get_completion(prompt, client)
'''
### Using generated script from here on
files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)

files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)
        
files = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced")
for file in files:
    file_path = os.path.join("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced", file)
    if os.path.isfile(file_path):
      try:
        os.remove(file_path)
      except:
        print("Unable to delete file ",file)

footage = VideoFileClip("Minecraft Parkour Gameplay No Copyright.mp4",audio=False)
duration = int(footage.duration - 0.28)

start = random.randint(0,duration-60)
clip = footage.subclip(start,start+60)

clip = clip.resize((500,600))

### Only used until I pay openAI ###
file = open("Script.txt")
script = file.readlines()
file.close()
final_script =[]
for line in script:
  final_script.append(line.replace("\n",""))

clear = False
while not clear:
  try:
    final_script.remove("")
  except:
    clear = True
    break

### End of filler code ###

lines = len(final_script)

lines_min = 60//lines
start = 0
end = lines_min
for i in range(0,lines):
  sub_clip = clip.subclip(start,end)
  start += lines_min
  end += lines_min
  txt = TextClip(final_script[i],bg_color="white",method="caption",size=(400,300))
  txt = txt.set_position("center").set_duration(lines_min)
  speech = gTTS(text=final_script[i],lang="en")
  speech.save(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios\\audio number {i}.wav")
  f = CompositeVideoClip([sub_clip,txt])
  f.write_videofile(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips\\clip number {i}.mp4")
  audio = AudioFileClip(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\audios\\audio number {i}.wav")
  f = VideoFileClip(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\clips\\clip number {i}.mp4").without_audio()
  voiced = f.set_audio(audio)
  voiced.write_videofile(f"C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced\\clip number {i}.mp4")
  print("Just finished line: ",i+1," of ",lines)
  audio.close()
  f.close()

clips = os.listdir("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced")
file_paths = []
for clip in clips:
    file_paths.append("C:\\Users\\Owner\\Desktop\\TikTok Gen\\voiced\\"+clip)

def finish(*args):
  files = args[0]
  film_list =[]
  for file in files:
      foo = VideoFileClip(file)
      film_list.append(foo)
  
  video = concatenate_videoclips(film_list)
  return video
  
    

final = finish(file_paths)
final.preview()
        
