"""
Script de tests TP2 autonome sans framework externe.
Exécute les 4 scénarios TP2 en utilisant directement Selenium et le POM.
"""
import time
from driver_factory import create_chrome_driver
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.notification_page import NotificationPage
from pages.infinite_scroll_page import InfiniteScrollPage


def run_step(name, func):
    """Lancer un test et afficher le résultat"""
    print(f"EXÉCUTION: {name}")
    func()
    print(f"✓ SUCCÈS: {name}\n")


def main():
    """Lancer tous les tests"""
    driver = create_chrome_driver(headless=False)
    try:
        # Test 1 : Contrôles dynamiques
        dynamic_controls = DynamicControlsPage(driver)
        dynamic_controls.open()
        assert dynamic_controls.is_loaded()
        assert dynamic_controls.is_checkbox_present()
        dynamic_controls.click_remove_or_add()
        dynamic_controls.wait_checkbox_disappears()
        assert "It's gone!" in dynamic_controls.get_message()
        dynamic_controls.click_remove_or_add()
        dynamic_controls.wait_checkbox_appears()
        assert "It's back!" in dynamic_controls.get_message()
        assert dynamic_controls.is_input_disabled()
        dynamic_controls.click_enable()
        dynamic_controls.wait_input_enabled()
        assert not dynamic_controls.is_input_disabled()
        dynamic_controls.enter_text("Selenium TP2")

        # Test 2 : Chargement dynamique
        dynamic_loading = DynamicLoadingPage(driver)
        dynamic_loading.open()
        dynamic_loading.click_example_2()
        assert dynamic_loading.is_start_present()
        dynamic_loading.click_start()
        dynamic_loading.wait_for_hello()
        assert dynamic_loading.get_hello_text() == "Hello World!"

        # Test 3 : Notifications
        notification = NotificationPage(driver)
        notification.open()
        assert notification.wait_for_message()
        for _ in range(3):
            notification.click_refresh()
            message = notification.wait_for_message()
            assert notification.is_message_expected(message)

        # Test 4 : Défilement infini
        infinite_scroll = InfiniteScrollPage(driver)
        infinite_scroll.open()
        before = infinite_scroll.get_block_count()
        infinite_scroll.scroll_down()
        infinite_scroll.wait_for_additional_blocks(before)
        after = infinite_scroll.get_block_count()
        assert after > before

        print("\n✓ TOUS LES TESTS TP2 RÉUSSIS")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
