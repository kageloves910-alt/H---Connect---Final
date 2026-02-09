import flet as ft

def main(page: ft.Page):
    # App Settings
    page.title = "H-Connect"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"
    page.padding = 20

    # 1. Header Section
    header = ft.Column(
        [
            ft.Text("H-Connect", size=32, weight="bold", color="blue"),
            ft.Text("Helping hands for you", size=16, color="grey"),
        ],
        horizontal_alignment="center",
    )

    # 2. Daily Input Field
    win_input = ft.TextField(
        label="ယနေ့အတွက် အနိုင်ရလဒ်",
        hint_text="ဂဏန်းရိုက်ထည့်ပါ...",
        border_radius=10,
    )

    # 3. Call Button Logic
    def call_button_click(e):
        page.launch_url("tel:09123456789")

    # 4. Action Buttons
    action_buttons = ft.Row(
        [
            ft.ElevatedButton(
                "ဖုန်းခေါ်ဆိုရန်", 
                icon=ft.icons.PHONE, 
                on_click=call_button_click,
                style=ft.ButtonStyle(color="white", bgcolor="green")
            ),
            ft.ElevatedButton(
                "သိမ်းဆည်းရန်", 
                icon=ft.icons.SAVE,
                style=ft.ButtonStyle(color="white", bgcolor="blue")
            ),
        ],
        alignment="center",
    )

    # 5. Result Display Area
    result_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ANNOUNCEMENT),
                        title=ft.Text("နောက်ဆုံးရသတင်းများ"),
                        subtitle=ft.Text("ယနေ့အတွက် ကံထူးရှင်များကို ကြေညာပေးပါမည်။"),
                    ),
                ]
            ),
            padding=10,
        )
    )

    # Add components to page
    page.add(
        header,
        ft.Divider(height=20, color="transparent"),
        win_input,
        ft.Divider(height=10, color="transparent"),
        action_buttons,
        ft.Divider(height=20),
        result_card
    )

ft.app(target=main)
