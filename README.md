# iPodScrobbler
> An attempt to automate iPod scrobbling to Last.FM using QTScrobbler


## Background
This Python based iPod Last.Fm Scrobbler is an attempt to automate iPod Scrobbling to Last.FM using the external program [QTScrobbler](http://qtscrob.sourceforge.net/).

After Last.FM's native scrobbler not working constsitently with scrobbling from the iPod, I looked into alternatives with no luck.

I had tried Rockbox, MusicBee and other standalone iPod scrobblers but none of them worked how I wanted them to - either they didn't upload the data to Last.FM and/or they didn't retain the logs for iTunes to update its own play count system.

After settling on QTScrobbler, I set out to find a way of uploading the logs to Last.FM while retaining the necessary files for iTunes to update its own play count counter.

As of the end of January 2018, I am currently undertaking the CS50 course and have begun to dip my toes into Python.
So what better way to learn the language by using it to slighty streamline the process of uploading my iPod scrobbling logs?
And thus my Python iPodScrobbler was born!

## Usage
**BEFORE USING THE SCRIPT**

Before using the script, make sure you have you have the following installed:
* [Python 3](https://www.python.org/downloads/)
* [iTunes](https://www.apple.com/itunes/download/)
* [QTScrobbler](http://qtscrob.sourceforge.net/)

Also, make sure you have your iPod set up and shown below - Untick "Open iTunes when this iPod is connected" and tick "Enable disk use"

![alt text](https://i.imgur.com/DH0vfVS.png "iTunes Setup")

**[constants.py](https://github.com/koaxu/iPodScrobbler/blob/master/constants.py)**

Please enter any values between the "quotes" ("")

What values you need are explained in the file.

**USING THE SCRIPT**

To use the script, open a command prompt/terminal window in the script's directory and enter:

```python
python ipodScrobbler.py
```

or double click the ipodScrobbler.py file and it should open in a command prompt/terminal window.

## TODO

In the future I plan to:

* Find a way to automatically close any music programs that are open.
* Open the 'Play Counts' file and submit it within QTScrobbler without the user needing to do so.
* Implement an iPod scrobbler within the script, making the use of QTScrobbler redundant.

If you have a Last.FM account and wish to see what I'm listening to you can do so [here](https://www.last.fm/user/tommo619).


