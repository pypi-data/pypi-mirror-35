# symphony-api-client-python
The Python client is built in an event handler architecture. If you are building a bot that listens to conversations, you will only have to implement an interface of a listener with the functions to handle all events that will come through the Data Feed.

### Install: pip install sym-api-client-python
### Note this repo is in constant development


## Configuration
Create a config.json file in your project which includes the following properties

        {
          "sessionAuthHost": "COMPANYNAME-api.symphony.com",
          "sessionAuthPort": 8444,
          "keyAuthHost": "COMPANYNAME-api.symphony.com",
          "keyAuthPort": 8444,
          "podHost": "COMPANYNAME.symphony.com",
          "podPort": 443,
          "agentHost": "COMAPNYNAME.symphony.com",
          "agentPort": 443,
          "botCertPath": "PATH",
          "botCertName": "BOT-CERT-NAME",
          "botCertPassword": "BOT-PASSWORD",
          "botEmailAddress": "BOT-EMAIL-ADDRESS",
          "appCertPath": "",
          "appCertName": "",
          "appCertPassword": "",
          "proxyURL": "",
          "proxyUsername": "",
          "proxyPassword": "",
          "authTokenRefreshPeriod": "30",
          "authType": "RSA"
        }

## Example main class

    from sym_api_client_python.configure.configure import Config
    from sym_api_client_python.auth.auth import Auth
    from sym_api_client_python.clients.SymBotClient import SymBotClient
    from sym_api_client_python.listeners.imListenerTestImp import IMListenerTestImp
    from sym_api_client_python.listeners.roomListenerTestImp import RoomListenerTestImp

    #debug logging --> set to debug --> check logs/example.log
    import logging
    logging.basicConfig(filename='example.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w', level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    #main() acts as executable script --> run python3 hello.py to start Bot...
    def main():
        print('hi')
        #pass in path to config.json file to Config class
        configure = Config('config.json')
        #parse through config.json and extract decrypt certificates
        configure.connect()
        #if you wish to authenticate using RSA replace following line with: auth = rsa_Auth(configure) --> get rid of auth.authenticate
        auth = Auth(configure)
        #retrieve session and keymanager tokens:
        auth.authenticate()
        #initialize SymBotClient with auth and configure objects
        botClient = SymBotClient(auth, configure)
        #initialize datafeed service
        DataFeedEventService = botClient.getDataFeedEventService()
        #initialize listener classes and append them to DataFeedEventService class
        #these listener classes sit in DataFeedEventService class as a way to easily handle events
        #coming back from the DataFeed
        imListenerTest = IMListenerTestImp(botClient)
        DataFeedEventService.addIMListener(imListenerTest)
        roomListenerTest = RoomListenerTestImp(botClient)
        DataFeedEventService.addRoomListener(roomListenerTest)
        #create data feed and read datafeed recursively
        DataFeedEventService.startDataFeed()

    if __name__ == "__main__":
    main()



## Example RoomListener implementation

    class RoomListenerTestImp(RoomListener):

        def __init__(self, SymBotClient):
            self.botClient = SymBotClient

        def onRoomMessage(self, message):
            print('room message recieved', message)
            #sample code for developer to implement --> use MessageClient and
            #data recieved from message event to reply with a #reed
            streamId = message['payload']['messageSent']['message']['stream']['streamId']
            messageId = message['payload']['messageSent']['message']['messageId']
            message = dict(message = '<messageML><hash tag="reed"/></messageML>')
            self.botClient.messageClient.createMessage(streamId, message)

        def onRoomCreated(self, roomCreated):
            print('room created', roomCreated)

        def onRoomDeactivated(self, roomDeactivated):
            print('room Deactivated', roomDeactivated)

        def onRoomMemberDemotedFromOwner(self, roomMemberDemotedFromOwner):
            print('room member demoted from owner', roomMemberDemotedFromOwner)

        def onRoomMemberPromotedToOwner(self, roomMemberPromotedToOwner):
            print('room member promoted to owner', roomMemberPromotedToOwner)

        def onRoomReactivated(self, roomReactivated):
            print('room reactivated', roomReactivated)

        def onRoomUpdated(self, roomUpdated):
            print('room updated', roomUpdated)

        def onUserJoinedRoom(self, userJoinedRoom):
            print('USER JOINED ROOM', userJoinedRoom)

        def onUserLeftRoom(self, userLeftRoom):
            print('USER LEFT ROOM', userLeftRoom)
