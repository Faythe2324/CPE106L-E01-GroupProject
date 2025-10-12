import flet as ft

def main(page: ft.Page):
    page.title = "Eco-Action Tracker"
    page.theme_mode = "LIGHT"
    page.window_width = 800
    page.window_height = 600

    # Input fields
    action_type = ft.TextField(label="Action Type (e.g., biking, recycling)")
    description = ft.TextField(label="Description", multiline=True)
    date = ft.TextField(label="Date (YYYY-MM-DD)")

    # Submit handler
    def log_action(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Logged: {action_type.value}, {description.value}, {date.value}"))
        page.snack_bar.open = True
        page.update()

    # Layout
    page.add(
        ft.Text("Log Your Eco-Action", size=24, weight="bold"),
        action_type,
        description,
        date,
        ft.ElevatedButton("Submit", on_click=log_action)
    )

ft.app(target=main)
