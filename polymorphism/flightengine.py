class Flight:
    def __iniit__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start();

class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")

class BoingEngine:
    def start(self):
        print("Starting BoingingEnginr engine")

ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()