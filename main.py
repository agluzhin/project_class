class Car:
    car_inf = {}
    car_type = ['Хэтчбек', 'Седан', 'Универсал', 'Купе', 'Внедорожник', 'Кабриолет', 'Электромобиль', 'Родстер']

    def show_type(self):
        self.car_type = Car.car_type
        for i in self.car_type:
            print(i)
        print("Выберите тип автомобиля:")

    def show_info(self):
        z = input()
        if z == "Хэтчбэк":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: A-Класс")
            print("Мощность двигателя у данной модели:", AMG.car_inf["A-Класс"], "кВт")
        elif z == "Седан":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__, car_d.__class__.__name__)
            print("Модель: E-Класс, S-Класс")
            print("Мощность двигателя:", AMG.car_inf["E-Класс"], MayBach.car_inf["S-Класс"], "кВт")
        elif z == "Универсал":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: E-Класс")
            print("Мощность двигателя:", AMG.car_inf["E-Класс"], "кВт")
        elif z == "Купе":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: E-Класс, CLA, GT, CLS, GLC")
            print("Мощность двигателя:", AMG.car_inf["E-Класс"], AMG.car_inf["CLA"], AMG.car_inf["GT"],
                  AMG.car_inf["CLS"], AMG.car_inf["GLC"], "кВт")
        elif z == "Внедорожник":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: GLA, G-Класс, GLC")
            print("Мощность двигателя:", AMG.car_inf["GLS"], AMG.car_inf["G-Класс"], AMG.car_inf["GLC"], "кВт")
        elif z == "Кабриолет":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: E-Класс")
            print("Мощность двигателя:", AMG.car_inf["E-Класс"], "кВт")
        elif z == "Электромобиль":
            print("Вам подойдет автомобиль класса:", car_b.__class__.__name__)
            print("Модель: EQE, EQS")
            print("Мощность двигателя:", car_b.car_inf["EQE"], car_b.car_inf["EQs"], "кВт")
        elif z == "Родстер":
            print("Вам подойдет автомобиль класса:", car_c.__class__.__name__)
            print("Модель: SL")
            print("Мощность двигателя:", AMG.car_inf["SL"], "кВт")
        else:
            print("Ошибка. Попробуйте ещё раз...")


class MersedesEQ(Car):
    car_inf = {
        # model: engine_power
        'EQE': 215,
        'EQS': 385
    }


class AMG(Car):
    car_inf = {
        'A-Класс': 110,
        'E-Класс': 320,
        'GLA': 224,
        'GLC': 375,
        'G-Класс': 430,
        'CLA': 310,
        'CLS': 320,
        'GT': 320,
        'SL': 320
    }


class MayBach(Car):
    car_inf = {
        'S-Класс': 270
    }


car_a = Car()
car_b = MersedesEQ()
car_c = AMG()
car_d = MayBach()

car_a.show_type()
car_a.show_info()
