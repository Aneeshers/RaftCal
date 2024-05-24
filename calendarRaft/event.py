HEADER_LENGTH = 10

class Event:
    def __init__(self,username,title, date, start_time, end_time):
        self.username = username
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def overlapping(self, start, end):
        return (self.start_time >= start and self.start_time <= end) or (self.end_time >= start and self.end_time <= end)

    @staticmethod
    def createEventFromBuffer(data):
        dataSplit = data.split(":",4)
        
        print(data)
        print(dataSplit)
        print("EARLIER.",dataSplit)
        username = dataSplit[1]
        title = dataSplit[2]
        date = dataSplit[3]
        time = dataSplit[4]
        start_time, end_time = time.split("-")

        print("EVENT. ")
        print(username) 
        print(title) 
        print(date)
        print(start_time)
        print(end_time)
        return Event(username, title, date, start_time, end_time)