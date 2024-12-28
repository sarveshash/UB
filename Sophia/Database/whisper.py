from Sophia import DATABASE
import asyncio
import random
import logging

db = DATABASE["whisper"]

class whisper:
  async def get(self, id):
    try:
      info = await db.find_one({"_id": id})
      if info and info['msg'] and info['id']:
        data = {
          'message': info['msg'],
          'id': info['id']
        }
        return data or {}
      return {}
    except Exception as e:
      logging.error(e)
      return {}
  async def add(self, message, id):
    try:
      wid = await db.find_one({"_id": 1})
      if wid: wid = len(wid['ids')+1 or 1
      else: wid = 1
      await db.update_one({"_id": 1}, {"$addToSet": {"ids": int(wid)}}, upsert=True)
      await db.update_one({"_id": int(wid)}, {"$set": {"message": message, "user_id": id}}, upsert=True)
      return wid
    except Exception as e: logging.error(e)
