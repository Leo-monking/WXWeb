# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
from django.shortcuts import render
from django.http import HttpResponse
import receive
import reply
import hashlib

def index(request):
	requestMethod = request.method
	try:
		if requestMethod == 'GET':
			signature = request.GET.get('signature')
			timestamp = request.GET.get('timestamp')
			nonce = request.GET.get('nonce')
			echostr = request.GET.get('echostr')
			token = "monking" 
			list = [token, timestamp, nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update, list)
			hashcode = sha1.hexdigest()
			if hashcode == signature:
				return HttpResponse(echostr, content_type="text/plain")
			else:
				return HttpResponse("")
			
		if requestMethod == 'POST':
     		recMsg = receive.parse_xml(str(request.body))
     		toUser = recMsg.FromUserName
     		fromUser = recMsg.ToUserName
     		msgType = recMsg.MsgType
     		if msgType == 'text':
     			content = "Welcome to monking`s house!"
     			replyMsg = reply.TextMsg(toUser, fromUser, content)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
     		if msgType == 'image':
     			mediaId = recMsg.MediaId
     			replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
     		if msgType == "voice":
     			content = "Welcome to monking`s house!But,What are you nong sha le , ting budong !"
     			print content
     			replyMsg = reply.VoiceMsg(toUser, fromUser, recMsg.Format)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
     		if msgType == "location":
     			content = "Welcome to monking`s house!But,What are you nong sha le!\nshushu,shushu,buyue buyue !"
     			print content
     			replyMsg = reply.LocationMsg(toUser, fromUser, recMsg.Location_X,recMsg.Location_Y,recMsg.Scale,recMsg.Label)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
          	else:
          		return HttpResponse(reply.Msg().send())
	except Exception, Argment:
		print Argment 
		return HttpResponse(Argment)
