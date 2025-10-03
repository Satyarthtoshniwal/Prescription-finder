from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
import os

KV = '''
MDBoxLayout:
    orientation: "vertical"
    padding: dp(16)
    spacing: dp(16)

    MDCard:
        orientation: "vertical"
        padding: dp(16)
        size_hint_y: None
        height: self.minimum_height
        elevation: 8
        radius: [16,]

        MDLabel:
            text: "Prescription Finder"
            font_style: "H5"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1] + dp(12)

        MDSeparator:
            height: dp(1)

        MDTextField:
            id: age_field
            hint_text: "Age"
            helper_text_mode: "on_focus"
            input_filter: "int"
            required: True

        MDTextField:
            id: weight_field
            hint_text: "Weight (kg)"
            helper_text_mode: "on_focus"
            input_filter: "float"
            required: True

        MDTextField:
            id: symptom_field
            hint_text: "Symptoms (e.g., fever, headache)"
            helper_text_mode: "on_focus"
            required: True

        MDRaisedButton:
            text: "Get Prescription"
            pos_hint: {"center_x": 0.5}
            on_release: app.get_prescription()

    MDCard:
        orientation: "vertical"
        padding: dp(16)
        elevation: 6
        radius: [12,]
        size_hint_y: None
        height: dp(180)

        MDLabel:
            id: result_label
            text: "Enter details above and press Get Prescription"
            halign: "center"
            valign: "middle"
            theme_text_color: "Primary"
            markup: True
            font_style: "Body1"
'''

class MedicineMDApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        data_dir = self.user_data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        store_path = os.path.join(data_dir, "prescriptions.json")
        self.store = JsonStore(store_path)

        if not self.store.exists("prescriptions"):
            prescriptions = [
                {'age_min': 2, 'age_max': 10, 'weight_min': 10, 'weight_max': 25, 'symptom': 'fever', 'medicine': 'Paracetamol', 'dosage': '5ml twice a day'},
                {'age_min': 11, 'age_max': 18, 'weight_min': 25, 'weight_max': 55, 'symptom': 'fever', 'medicine': 'Paracetamol', 'dosage': '10ml twice a day'},
                {'age_min': 19, 'age_max': 65, 'weight_min': 55, 'weight_max': 100, 'symptom': 'headache', 'medicine': 'Ibuprofen', 'dosage': '400mg once daily'},
            ]
            self.store.put("prescriptions", data=prescriptions)

    def get_prescription(self):
        age_text = self.root.ids.age_field.text.strip()
        weight_text = self.root.ids.weight_field.text.strip()
        symptom = self.root.ids.symptom_field.text.strip().lower()

        if not age_text or not weight_text or not symptom:
            self.root.ids.result_label.text = "[color=#d32f2f]⚠ Please fill all fields[/color]"
            return

        try:
            age = int(age_text)
            weight = float(weight_text)
        except ValueError:
            self.root.ids.result_label.text = "[color=#d32f2f]⚠ Invalid input[/color]"
            return

        prescriptions = []
        if self.store.exists("prescriptions"):
            prescriptions = self.store.get("prescriptions")["data"]

        result = None
        for p in prescriptions:
            if (p['age_min'] <= age <= p['age_max'] and
                p['weight_min'] <= weight <= p['weight_max'] and
                symptom == p['symptom']):
                result = (f"[b][color=#2e7d32]Medicine:[/color][/b] {p['medicine']}\n"
                          f"[b][color=#1565c0]Dosage:[/color][/b] {p['dosage']}")
                break

        if not result:
            result = "[color=#d32f2f]No matching prescription found.[/color]"

        self.root.ids.result_label.text = result


if __name__ == '__main__':
    MedicineMDApp().run()
