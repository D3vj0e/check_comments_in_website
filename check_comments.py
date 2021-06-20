import requests
from bs4 import BeautifulSoup
import time
from bs4 import Comment



print("welcome to Check it out!")
print("Please input full link(http://....)")
target_web = input("Your target: ")
target_check = requests.get(test_tar)
print("\nstatus target is :",target_check.status_code)
time.sleep(2)

#1 check comments in html
#2 check json files

make_it_good = BeautifulSoup(target_check.text,"html.parser")
print(make_it_good.prettify())

print("\n\n this is all contents in your target website\n")

comments = make_it_good.find_all(string=lambda text: isinstance(text, Comment))
print("\n\nAll comment in this website here \n\n ")
for fill_comments in comments:
    print(fill_comments)
    