import time
import random
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please drink water",
            message = "It boosts skin health and beauty", 
            app_icon = None,
            timeout = 10

        )
        time.sleep(60*60)