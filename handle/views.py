# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
from django.shortcuts import render
from django.http import HttpResponse
import receive
import reply
import hashlib
#import sys

#reload(sys)
#sys.setdefaultencoding("utf-8")
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
			webData = str(request.body)
			print webData
     		recMsg = receive.parse_xml(webData)
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
     			#content = u"Welcome to monking`s house!But,What are you ≈™…∂‡œ , Ã˝≤ª∂Æ !"
     			content = u"Welcome to monking`s house!But,What are you nong sha le ! ting bu dong !"
     			print content
     			replyMsg = reply.VoiceMsg(toUser, fromUser, recMsg.MediaId,recMsg.Format)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
     		if msgType == "location":
     			content = u"Welcome to monking`s house!But,What are you ≈™…∂‡œ!\n Â Â£¨ Â Â£¨Œ“≤ª‘º !"
     			content = (content.decoding("asscii")).encoding("utf-8")
     			print content
     			#replyMsg = reply.LocationMsg(toUser, fromUser, recMsg.Location_X,recMsg.Location_Y,recMsg.Scale,recMsg.Label)
     			#retMsg = replyMsg.send()
     			#print retMsg
     			#return HttpResponse(retMsg)
     			replyMsg = reply.TextMsg(toUser, fromUser, content)
     			retMsg = replyMsg.send()
     			print retMsg
     			return HttpResponse(retMsg)
          	else:
          		return HttpResponse(reply.Msg().send())
	except Exception, Argment:
		print Argment 
		return HttpResponse(Argment)
