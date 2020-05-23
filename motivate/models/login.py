class Observable():
    
    def __init__(self):
        self._user = 'Alan@b.com'
        self._pass = 'pass'
        self._observers = []
        
    def attach(self, observer) -> None:
        print("attached observer " + str(observer))
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def _notify(self, earnings, count) -> None:
        print("notifying observers..")
        for observer in self._observers:
            observer.update(earnings, count)

    @property
    def username(self):
        return self._user

    @username.setter
    def username(self, usernam):
        self._user = username
        self._notify(self._user)

    @property
    def password(self):
        return self._pass

    @password.setter
    def password(self, pass_):
        self._pass = pass_
        
class Calculator():
    def __init__(self):
        self.obs = Observable()

    def check(self, details):
        if self.obs.username == details.username and self.obs.password == details.password:
            return True
     
