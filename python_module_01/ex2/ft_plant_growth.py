class Plant:
    def __init__(self, name_pam: str, height_pam: float, age_pam: int) -> None:
        self.name_pam = name_pam
        self.height_pam = height_pam
        self.age_pam = age_pam

    def grow(self) -> None:
        self.height_pam += 0.8

    def age(self) -> None:
        self.age_pam += 1

    def show(self) -> None:
        for i in range(8):
            if i > 1:
                print("=== Day", i, "===")
            print(f"{self.name_pam}: {round(self.height_pam, 2)}cm,"
                  f" {self.age_pam} days old")
            if i < 1:
                print("=== Day 1 ===")
            self.grow()
            self.age()
            if i >= 7:
                print(f"Growth this week: {round(0.8*i, 2)}cm")


p1 = Plant("Rose", 25.0, 30)

print("=== Garden Plant Growth ===")
p1.show()
