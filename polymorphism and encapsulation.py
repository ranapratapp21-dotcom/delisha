# Sports Scoreboard (complete activity, DSCM2L6). Python 3 standard library only.
# Run: python sports_scoreboard.py  (or paste into one Google Colab cell and press Run)


class Sport:                             # A: the parent class
    def __init__(self, player, score):
        self.player = player             # public: anyone may read it
        self.__score = 0                 # private: Python stores it as _Sport__score
        self.set_score(score)            # even the starting score goes through the setter

    def get_score(self):                 # B: the getter, the safe way to read
        return self.__score

    def set_score(self, new_score):      # the setter, the only way to change the score
        # Step 4: Validate the new score
        valid = type(new_score) is int and new_score >= 0
        if valid:                        # C: only a valid value reaches the private score
            self.__score = new_score
        else:
            print(f"Rejected {new_score!r}: a score is a whole number, 0 or more.")
        return valid

    def info(self):                      # D: the parent versions of info() and play()
        print(f"{self.player}: {self.get_score()} points")

    def play(self):
        print(f"{self.player} plays.")


class Baseball(Sport):
    def info(self):                      # E: Baseball overrides info()
        # Step 1: Override info() for baseball
        print(f"Baseball - {self.player}: {self.get_score()} runs")

    def play(self):
        print(f"{self.player} hits a home run!")


class Football(Sport):
    def info(self):
        print(f"Football - {self.player}: {self.get_score()} goals")

    def play(self):                      # F: Football overrides play()
        # Step 2: Override play() for football
        print(f"{self.player} scores a goal!")


class Basketball(Sport):
    def play(self):                      # G: a new sport, added without touching the loop
        # Step 3: Add a sport, keep the loop
        print(f"{self.player} shoots and scores a three-pointer!")


player = input("Baseball player name? ")
runs = int(input("Baseball runs? "))
scoreboard = [Baseball(player, runs), Football("Marco", 2), Basketball("Nina", 12)]   # H
for sport in scoreboard:                 # I: one loop, many behaviours
    sport.info()
    sport.play()
baseball, football = scoreboard[0], scoreboard[1]             # J: encapsulation tests
baseball.__score = 999
print("After baseball.__score = 999, get_score() gives", baseball.get_score())
print("Attributes really stored:", sorted(vars(baseball)))
for value in [100, -5, "abc"]:
    baseball.set_score(value)
print("Final:", baseball.get_score(), "runs and", football.get_score(), "goals")
Sport("Nobody", -3).info()                                   # K: a bad starting score
