# Required Libraries Import
import requests
from bs4 import BeautifulSoup

# Get Problem Tag and editorial url to request html page
problem_tag = input("Enter Problem Code: ").upper()
url = "https://discuss.codechef.com/problems/"+problem_tag
page = requests.get(url)

# If Response code is 200 then process page for Editorial Solution and print all given solutions
if page.status_code == 200:
  soup = BeautifulSoup(page.content,'html5lib')
  codes = soup.select('body')[0].find_all("div")[0].select("div")[4].select("div")[3].select("code")
  codes = [code.get_text() for code in codes]
  if len(codes) == 0:
    print("Sorry, Editorial for this problem either doesn't exist or not in supported format")
  else:
    for code in codes:
      if(len(code) > 20):
        print("\n\n\n->Given Solution:\n")
        print(code)
else:
  print("Please Enter a Valid Problem Code")
