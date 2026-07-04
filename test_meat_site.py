import pytest
from playwright.sync_api import Page, expect

# URL твоего живого сайта на Render
BASE_URL = "https://dep-projekt.onrender.com"

def test_site_title(page: Page):
    """Проверяем корректность тайтла страницы."""
    page.goto(BASE_URL)
    # expect в Playwright умеет ждать элемент/состояние автоматически
    expect(page).to_have_title("М Я С О — Культ Продукта")

def test_logo_is_visible(page: Page):
    """Проверяем, что логотип отображается и текст верный."""
    page.goto(BASE_URL)
    logo = page.locator(".logo")
    expect(logo).to_be_visible()
    expect(logo).to_have_text("Мясо.")

def test_menu_cards_count(page: Page):
    """Проверяем, что на странице ровно 3 карточки стейков."""
    page.goto(BASE_URL)
    cards = page.locator(".grid .card")
    
    # Проверяем количество элементов в сетке
    expect(cards).to_have_count(3)
    
    # Проверяем заголовок конкретно первой карточки (Рибай)
    expect(cards.nth(0).locator("h3")).to_have_text("Рибай")