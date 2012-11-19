#!/usr/bin/python

import os
import sys
import xbmc
import xbmcaddon

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__cwd__        = xbmc.translatePath( __addon__.getAddonInfo('path') ).decode("utf-8")
__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') ).decode("utf-8")
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources' ) ).decode("utf-8")

sys.path.append (__resource__)

class MyPlayer( xbmc.Player ):
  def __init__( self, *args, **kwargs ):
    xbmc.Player.__init__( self )
    print('MyPlayer - init')
    self.run = True
    
  def onPlayBackStopped( self ):
    self.run = True
  
  def onPlayBackEnded( self ):
    self.run = True         
  
  def onPlayBackStarted( self ):
    if self.run:
      movieFullPath       = xbmc.Player().getPlayingFile()
      if (not xbmc.getCondVisibility("VideoPlayer.HasSubtitles")) and (not movieFullPath.find("http") > -1 ) and (not movieFullPath.find("pvr") > -1 ):
        self.run = False
        xbmc.sleep(1000)
        print('AutoSearching for Subs')
        xbmc.executebuiltin('XBMC.RunScript(script.xbmc.subtitles)')
      else:
        self.run = False  
      

player_monitor = MyPlayer()
     
while not xbmc.abortRequested:
  xbmc.sleep(1000)
  
del player_monitor