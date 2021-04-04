#!/usr/bin/python3
import youtube_dl
import pafy


link1 = input("Enter Your link: ")
setup1 = pafy.new(link1)

getLatest = setup1.getbest()
getLatest.download()