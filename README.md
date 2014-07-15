Name: Trivia Challenge 3000!

Description: Welcome to the Sci-Fi part of our game. In this challenge, you
will have to match captains with their vessels from the show Star Trek. Oh
wait! It appears as though we've lost one of the pictures of the captains!
Maybe you can help us out?

How to Solve: Participants are presented with a website which displays a 
series of Star Trek captains (with some distractors) and the names of vessels
on the right. Each of the pictures is labeled with a number (and there is a 
dropdown next to each vessel name).

It should be obvious based on the black image and the corruption in the image
of Sisko that there is something going on here. Once the participant downloads
all of the images, it is possible to find fragments of a phrase embedded in
the images of the four captains (via strings). When put together (in order
of the shows' airing), a passphrase is formed. Appended to the end of the
black image is an archive which can be opened with this passphrase.

Inside that archive are an image and another archive. If one adds up all of 
the RGB values of the `addition' image, in decimal, a new string is found. By
inputting that decimal number as the password of the archive, a number of
images, along with a text file. In the text file is the flag.

What to distribute:
Only give the link to the web server hosting the challenge.

How to Stand Up locally: 
    Install [vagrant](http://vagrantup.com/) and then run vagrant up from the root of this directory. After the script finished, navigate to [localhost:8080](http://localhost:8080) in your browser.

Flag: MCA-ED0C7012
