# 
# Example file for parsing and processing HTML
#

import os
from html.parser import HTMLParser


metacount = 0;

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data): # handle_comment is existing
    print("Encounted comment: ", data)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])

  def handle_starttag(self, tag, attrs):
    global metacount
    if tag == "meta":
        metacount += 1
    print("Encounted tag: ", tag)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])

    if attrs.__len__() > 0:
        print("\tAttributes: ")
        for a in attrs:
            print("/t", a[0], "=", a[1])

  def handle_endtag(self, tag):
    print("Encounted tag: ", tag)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])

  def handle_data(self, data):
    if data.isspace():
      return
    print("Encounted data: ", data)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])



def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("/home/linyiguo96/Desktop/exercise/Ch5/samplehtml.html")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)

  print("Meta tags found: "+ str(metacount))
   

if __name__ == "__main__":
  main();