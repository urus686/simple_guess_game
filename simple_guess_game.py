import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Привет! Я загадал число от 1 до 100.")
    print(f"У тебя есть {max_attempts} попыток, чтобы его угадать.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}: Введите число: "))
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Слишком маленькое число.")
        elif guess > secret_number:
            print("Слишком большое число.")
        else:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
            break
    else:
        print(f"\nВы исчерпали попытки. Загаданное число было: {secret_number}")

if __name__ == "__main__":
    guess_the_number()
