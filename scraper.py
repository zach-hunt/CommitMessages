import urllib.request
import os
from profanity_check import predict_prob


def main():
    site = urllib.request.urlopen("http://whatthecommit.com/").read()
    content = str(site)
    start = content.find("<div id=\"content\">") + 23
    end = content.find("\\n</p>\\n<p class=\"permalink\">")
    message = content[start:end]
    print("Message:", message, "\n")

    message = clean(message)
    if len(message) == 0:
        main()

    os.system(R"cd C:\Users\zacha\Documents\MEGAsync\Zachary\Self\Programs\Python\CommitMessages")
    os.system("git add scraper.py")
    os.system("git commit --allow-empty -m \"" + str(message) + "\"")
    os.system("git push")


def clean(phrase: str) -> str:
    cleanphrase = []
    for word in phrase.split(" "):
        if predict_prob([word])[0] < 0.5:
            cleanphrase.append(word)
    return " ".join(cleanphrase)


if __name__ == "__main__":
    main()
