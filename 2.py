import time
class MyTimer:
    def __init__(self, units):
        if units in ("s", "m", "h"):
            self.units = units
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.spent_time = self.end - self.start

    def elapsed_time(self):
        if self.units == "s":
            return self.spent_time
        if self.units == "m":
            return self.spent_time/60
        if self.units == "h":
            return self.spent_time/3600

if __name__ == "__main__":
    with MyTimer(units="s") as t:
        print("Hello world")
    print(t.elapsed_time())
