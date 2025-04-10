import random

class TaiXiuAI:
    def __init__(self):
        self.history = []
        self.prediction = None

    def update_result(self, result):
        self.history.append(result)
        if len(self.history) > 100:
            self.history.pop(0)

    def predict(self):
        if not self.history:
            return random.choice(['tai', 'xiu'])
        tai_count = self.history.count('tai')
        xiu_count = self.history.count('xiu')
        if tai_count > xiu_count:
            self.prediction = 'xiu'
        elif xiu_count > tai_count:
            self.prediction = 'tai'
        else:
            self.prediction = random.choice(['tai', 'xiu'])
        return self.prediction

if __name__ == "__main__":
    ai = TaiXiuAI()
    while True:
        user_input = input("Nhập kết quả (tai/xiu, hoặc q để thoát): ").strip().lower()
        if user_input == 'q':
            break
        if user_input not in ['tai', 'xiu']:
            print("Kết quả không hợp lệ. Vui lòng nhập 'tai' hoặc 'xiu'.")
            continue
        ai.update_result(user_input)
        prediction = ai.predict()
        print(f"Dự đoán tiếp theo: {prediction}")
