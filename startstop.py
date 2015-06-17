#play.py
import pygst
#pygst.require("0.10")
import gst

player = gst.element_factory_make("playbin", "player")
def play(uri):
	#our stream to play 'http://173.224.125.98:7788'
	#print 
	music_stream_uri = uri
	#creates a playbin (plays media form an uri) 
	

	#set the uri
	player.set_property('uri', music_stream_uri)
	#start playing
	player.set_state(gst.STATE_PLAYING)
	#wait and let the music play
#	raw_input('Press enter to stop playing...')
	#print playing

def stop():
	#wait and let the music play
	#raw_input('Press enter to stop playing...')
	player.set_state(gst.STATE_NULL)
	#print playing
