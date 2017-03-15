#coding=utf-8
'''
Created on 2017��3��13��

@author: zhao
'''
class Message(object):
    def __init__(self,messageStr,recipient):
        self.messageStr=messageStr
        self.recipient=recipient

class User(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.room=[]
    def createRoom(self,chatArea):
        self.room.append(Room(self,chatArea))
    def deleteRoom(self,aRoomNo):
        self.room.remove(aRoomNo)

class Room(object):
    def __init__(self,hostP,chatArea):
        self.hostP=hostP
        self.chatArea=chatArea