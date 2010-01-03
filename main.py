# -*- coding: utf-8 -*-

import profanity
import logging

from waveapi import events
from waveapi import model
from waveapi import robot
from waveapi import document

ROBOT_URL = 'http://language-timothy.appspot.com'

def OnRobotAdded(event, context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hi Everyone,\n\nI'm the \"Language, Timothy!\" swearbot. Watch your language!")

def OnBlipSubmitted(event, context):
  blip = context.GetBlipById(event.properties['blipId'])
  doc = blip.GetDocument()
  contents = doc.GetText()
  for m in profanity.replaceProfanity( contents ): 
    r = document.Range(m.start(), m.end())
    t = m.group(0)[0] + '*'*(len(m.group(0))-2) + m.group(0)[len(m.group(0))-1] 
    doc.SetTextInRange(r, t)
    doc.SetAnnotation(r, 'style/backgroundColor', 'rgb(255,240,240)')

if __name__ == '__main__':
  myRobot = robot.Robot('Language, Timothy!', 
    image_url = ROBOT_URL + 'assets/icon.png',
    version = '1',
    profile_url = ROBOT_URL)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
