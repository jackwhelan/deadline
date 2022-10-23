from time import sleep


class Alert:
    def __init__(self, hours, minutes, seconds, message):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.message = message

    def is_timer_done(self):
        hours_done = self.hours == 0
        minutes_done = self.minutes == 0
        seconds_done = self.seconds == 0
        return hours_done and minutes_done and seconds_done

    def start(self):
        while True:
            # timeformat = f'{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}'
            if self.seconds == 0:
                if self.minutes == 0:
                    if self.hours == 0:
                        break
                    self.hours -= 1
                    self.minutes = 60
                self.minutes -= 1
                self.seconds = 60
            sleep(1)
            self.seconds -= 1
            # print(timeformat)
        print(self.message)

if __name__ == '__main__':
    my_alert = Alert(0, 0, 5, 'Hello')
    my_alert.start()
