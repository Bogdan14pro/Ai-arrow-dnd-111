import flet as ft
import random
import openai

# Вставьте ваш API ключ OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"  # Замените на ваш API ключ

def generate_story(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response['choices'][0]['message']['content']

def roll_dice(sides):
    return random.randint(1, sides)

def main(page: ft.Page):
    page.title = "DnD Game with AI"

    # Элементы интерфейса
    prompt_input = ft.TextField(label="Введите ваш запрос", multiline=True, expand=True)
    story_output = ft.TextField(label="История", multiline=True, expand=True, read_only=True)
    roll_button = ft.ElevatedButton(text="Бросить кубик", on_click=lambda e: roll_dice_action())
    dice_result = ft.Text("Результат броска: ")
    roll_input = ft.TextField(label="Количество сторон кубика", value="20")

    def roll_dice_action():
        try:
            sides = int(roll_input.value)
            result = roll_dice(sides)
            dice_result.value = f"Результат броска: {result}"
        except ValueError:
            dice_result.value = "Пожалуйста, введите корректное число сторон кубика."
        page.update()

    def submit_prompt(e):
        story = generate_story(prompt_input.value)
        story_output.value = story
        page.update()

    prompt_input.on_submit = submit_prompt

    # Добавление элементов на страницу
    page.add(
        prompt_input,
        ft.ElevatedButton(text="Сгенерировать историю", on_click=submit_prompt),
        story_output,
        roll_input,
        roll_button,
        dice_result
    )

ft.app(target=main)
