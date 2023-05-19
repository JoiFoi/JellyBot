'''
JellyBot (github.com/JoiFoi/JellyBot)
Based On Bot API 6.7 - April 21, 2023
'''

import requests


class JellyBot:
  # Define and verify a robot by its API token
  def __init__(self, bot_token):
    if requests.get(
        f'https://api.telegram.org/bot{bot_token}/getMe').json()['ok'] == True:
      self.bot_token = bot_token
      print('@' + requests.get(f'https://api.telegram.org/bot{bot_token}/getMe'
                               ).json()['result']['username'] + ' is running!')
    else:
      raise ValueError(
        'Invalid bot token. Please ensure that you obtain your API token from @botfather.'
      )

  # This method allows us to generate HTTP request links by specifying the method name and bot token as parameters.
  def reqlink(self, method_name):
    return f'https://api.telegram.org/bot{self.bot_token}/{method_name}'

  # https://core.telegram.org/bots/api#available-methods

  # Use this method to send text messages. On success, the sent Message is returned.
  def sendMessage(self,
                  chat_id,
                  text,
                  parse_mode=None,
                  disable_web_page_preview=None,
                  reply_to_message_id=None,
                  disable_notification=None):
    requests.post(
      self.reqlink('sendMessage'), {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode,
        'disable_web_page_preview': disable_web_page_preview,
        'reply_to_message_id': reply_to_message_id,
        'disable_notification': disable_notification
      })

  # Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.
  def forwardMessage(self, chat_id, from_chat_id, message_id):
    requests.post(self.reqlink('forwardMessage'), {
      'chat_id': chat_id,
      'from_chat_id': from_chat_id,
      'message_id': message_id
    })

  # Use this method to send photos. On success, the sent Message is returned.
  def sendPhoto(self,
                chat_id,
                photo,
                caption=None,
                parse_mode=None,
                reply_to_message_id=None):
    requests.post(
      self.reqlink('sendPhoto'), {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption,
        'parse_mode': parse_mode,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send audio files, if you want Telegram clients to display them in the music player.
  # Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned.
  # Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
  def sendAudio(self,
                chat_id,
                audio,
                caption=None,
                parse_mode=None,
                title=None,
                reply_to_message_id=None):
    requests.post(
      self.reqlink('sendAudio'), {
        'chat_id': chat_id,
        'audio': audio,
        'caption': caption,
        'parse_mode': parse_mode,
        'title': title,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send general files. On success, the sent Message is returned.
  # Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
  def sendDocument(self,
                   chat_id,
                   document,
                   caption=None,
                   parse_mode=None,
                   reply_to_message_id=None):
    requests.post(
      self.reqlink('sendDocument'), {
        'chat_id': chat_id,
        'document': document,
        'caption': caption,
        'parse_mode': parse_mode,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document).
  # On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
  def sendVideo(self,
                chat_id,
                video,
                caption=None,
                parse_mode=None,
                supports_streaming=None,
                reply_to_message_id=None):
    requests.post(
      self.reqlink('sendVideo'), {
        'chat_id': chat_id,
        'video': video,
        'caption': caption,
        'parse_mode': parse_mode,
        'supports_streaming': supports_streaming,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound).
  # On success, the sent Message is returned.
  # Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.
  def sendAnimation(self,
                    chat_id,
                    animation,
                    caption=None,
                    parse_mode=None,
                    reply_to_message_id=None):
    requests.post(
      self.reqlink('sendAnimation'), {
        'chat_id': chat_id,
        'animation': animation,
        'caption': caption,
        'parse_mode': parse_mode,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send point on the map. On success, the sent Message is returned.
  def sendLocation(self,
                   chat_id,
                   latitude,
                   longitude,
                   reply_to_message_id=None):
    requests.post(
      self.reqlink('sendLocation'), {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method to send a native poll. On success, the sent Message is returned.
  def sendPoll(self,
               chat_id,
               question,
               options,
               is_anonymous=True,
               type='regular',
               allows_multiple_answers=False,
               correct_option_id=None,
               is_closed=None,
               reply_to_message_id=None):
    requests.post(
      self.reqlink('sendPoll'), {
        'chat_id': chat_id,
        'question': question,
        'options': options,
        'is_anonymous': is_anonymous,
        'type': type,
        'allows_multiple_answers': allows_multiple_answers,
        'correct_option_id': correct_option_id,
        'is_closed': is_closed,
        'reply_to_message_id': reply_to_message_id
      })

  # Use this method when you need to tell the user that something is happening on the bot's side.
  # The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).
  # Returns True on success.
  def sendChatAction(self, chat_id, action):
    requests.post(self.reqlink('sendChatAction'), {
      'chat_id': chat_id,
      'action': action
    })