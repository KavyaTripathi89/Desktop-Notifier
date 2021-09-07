import time
import random
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please drink water",
            message = random.choice(["It boosts skin, health and beauty", "Makes your mind stronger", "Increases intelligence"]), 
            app_icon = None,
            timeout = 10

        )
        time.sleep(60*60)
