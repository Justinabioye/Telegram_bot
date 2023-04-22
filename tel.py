import telegram.ext 

def start(update, context):
    update.message.reply_text("Hello! Welcome to RoomsForLiving Type help")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /Room -> Check Room Availability
    /Price  -> Room Price
    /Location -> Google Map Location
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)
    
def Room(update, context):
    update.message.reply_text("We have Rooms")

def Price(update, context):
    update.message.reply_text("Room is 4,500 ")

def Location(update, context):
    update.message.reply_text("Click for Location : https://maps.app.goo.gl/BErMXJ4X43VK1EAi8 ")
    
def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/i6AZdFxTK9I")
    
def Images(update, context):
    update.message.reply_text("tutorial link :")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mailgitgiid")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")

Token = ("6217926804:AAEdahmsm9_gCE6p7dtbmEeXZRzBwMjOYaU")
#print(bot.get_me())
updater = telegram.ext.Updater("6217926804:AAEdahmsm9_gCE6p7dtbmEeXZRzBwMjOYaU", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('Room',Room))
disp.add_handler(telegram.ext.CommandHandler('Price',Price))
disp.add_handler(telegram.ext.CommandHandler('Location',Location))
disp.add_handler(telegram.ext.CommandHandler('Java',Java))
disp.add_handler(telegram.ext.CommandHandler('Images',Images))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
