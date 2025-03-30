import PyPDF2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup


def create_password_protected_pdf(input_pdf, output_pdf, password):
    """
    Creates a password-protected PDF by reading an existing PDF and encrypting it with a given password.

    :param input_pdf: The path to the input PDF file.
    :param output_pdf: The path where the password-protected PDF will be saved.
    :param password: The password to encrypt the PDF with.
    """
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            pdf_writer.encrypt(password)

            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

            show_popup("Success", f"Password-protected PDF saved as {output_pdf}")
    except FileNotFoundError:
        show_popup("Error", f"The file {input_pdf} was not found.")
    except Exception as e:
        show_popup("Error", f"Error: {e}")


def show_popup(title, message):
    popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.5))
    popup.open()


class PDFShieldApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_label = Label(text="Select Input PDF", font_size=38)
        self.layout.add_widget(self.input_label)

        self.input_chooser = FileChooserIconView()
        self.layout.add_widget(self.input_chooser)

        self.output_label = Label(text="Select Output Location", font_size=38)
        self.layout.add_widget(self.output_label)

        self.output_chooser = FileChooserIconView()
        self.layout.add_widget(self.output_chooser)

        self.password_label = Label(text="Enter Password (Min 8 characters)", font_size=38)
        self.layout.add_widget(self.password_label)

        password_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        self.password_input = TextInput(password=True, multiline=False, font_size=32, size_hint=(0.8, 1))
        self.toggle_password_button = Button(text="Show", size_hint=(0.2, 1))
        self.toggle_password_button.bind(on_press=self.toggle_password_visibility)
        password_box.add_widget(self.password_input)
        password_box.add_widget(self.toggle_password_button)
        self.layout.add_widget(password_box)

        self.encrypt_button = Button(text="Encrypt PDF", font_size=36, background_color=(0.2, 0.6, 1, 1))
        self.encrypt_button.bind(on_press=self.process_pdf)
        self.layout.add_widget(self.encrypt_button)

        return self.layout

    def toggle_password_visibility(self, instance):
        """Toggles password visibility on button press."""
        self.password_input.password = not self.password_input.password
        self.toggle_password_button.text = "Hide" if not self.password_input.password else "Show"

    def process_pdf(self, instance):
        input_pdf = self.input_chooser.selection[0] if self.input_chooser.selection else ""
        output_pdf = self.output_chooser.path + "/encrypted.pdf" if self.output_chooser.path else ""
        password = self.password_input.text

        if not input_pdf or not output_pdf or not password:
            show_popup("Error", "Please fill in all the required details.")
            return

        if len(password) < 8:
            show_popup("Error", "Password must be at least 8 characters long.")
            return

        create_password_protected_pdf(input_pdf, output_pdf, password)


if __name__ == '__main__':
    PDFShieldApp().run()
