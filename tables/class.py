class mine() :
    name = "BASAVA"
    college = "M S RAMAIAH INSTITUTE OF TECHNOLOGY"
    fee = 122000
    village = "GOUDANBHAVI"
    taluk = "MASKI"
    @staticmethod
    def home(self) :
        print(f"NAME IS {self.name} and he is stuiding in {self.college} with fee {self.fee} and his village is {self.village} and taluk is {self.taluk}")


sweety = mine()
sweety.home()