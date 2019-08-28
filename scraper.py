import subprocess
import urllib.request
import os
site = urllib.request.urlopen("http://whatthecommit.com/").read()
content = str(site)
start = content.find("<div id=\"content\">") + 23
end = content.find("\\n</p>\\n<p class=\"permalink\">")
message = content[start:end]
print("Message:", message, "\n")

os.system(R"cd C:\Users\zacha\Documents\MEGAsync\Zachary\Self\Programs\Python\CommitMessages")
print("1")
os.system("git add scraper.py")
print("2")
os.system("git commit -m \"" + str(message) +  "\"")
print("3")
os.system("git push")
print("4")
