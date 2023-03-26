"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
# import openai
import time
import asyncio

from samantha_nn import handel_image
# openai.api_key = "YOUR_API_KEY"

color = "rgb(107,99,246)"


# def handel_image(image_path):
#     """Функція обробки зображеня нейромережею"""
#     # await asyncio.sleep(5)
#     time.sleep(5)
#     return f"This is {image_path}"


class State(pc.State):
    """The app state."""
    answer = "?"
    prompt = ""
    image_url = ""
    image_processing = False
    image_made = False
    img: str

    def process_image(self):
        """Set the image processing flag to true and indicate that the image has not been made yet."""
        self.image_made = False
        self.image_processing = True

    # def get_image(self):
    #     """Get the image from the prompt."""
    #     try:
    #         response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
    #         self.image_url = response["data"][0]["url"]
    #         # Set the image processing flag to false and indicate that the image has been made.
    #         self.image_processing = False
    #         self.image_made = True
    #     except:
    #         self.image_processing = False
    #         return pc.window_alert("Error with OpenAI Execution.")

    # def get_answer(self, image_path):
    #     """Оброблює зображення та повертає текст"""
    #     print(f'Run get answer {image_path}')
    #     try:
    #         result = handel_image(image_path)
    #         print(result)
    #         self.answer = result
    #         self.image_processing = False
    #         self.image_made = True
    #     except Exception:
    #         self.image_processing = False
    #         return pc.window_alert("Error with Samantha Execution.")
    #
    # def run_handler(self):
    #     self.handle_upload(pc.upload_files())
    #     print('upload files', pc.upload_files())

    async def handle_upload(self, file: pc.UploadFile):
        """Handle the upload of a file.

        Args:
            file: The uploaded file.
        """
        print(f'Run handel upload')
        # self.process_image()
        self.image_made = False
        self.image_processing = True

        upload_data = await file.read()
        outfile = f".web/public/{file.filename}"
        if file.filename:
            ext = file.filename.split('.')[-1]
            if ext not in ['png', 'gif', 'jpeg', 'jpg', 'svg']:
                return pc.window_alert("This is not a picture!\nTry again!")
        # print(self.image_made, self.image_processing)
        # Save the file.
        with open(outfile, "wb") as f:
            f.write(upload_data)

        # Update the img var.
        self.img = file.filename
        print(self.img)
        # self.get_answer(outfile)
        print(f'Run get answer {outfile}')
        # print(self.image_made, self.image_processing)
        try:
            result = handel_image(outfile)
            print(result)
            self.answer = result
            self.image_processing = False
            self.image_made = True
            # print(self.image_made, self.image_processing)
        except Exception:
            self.image_processing = False
            return pc.window_alert("Error with Samantha Execution.")


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Samantha", font_size="1.5em"),
            pc.divider(),
            pc.upload(pc.button("Select File", color=color, bg="white", border=f"1px solid {color}",
                                width="80%", padding="2em", margin="2em", ),
                      pc.text("Drag and drop files here or click to select files", ), padding="2em", ),
            pc.divider(),
            pc.button(
                "Generate Answer",
                # on_click=[State.process_image, State.run_handler],
                on_click=lambda: State.handle_upload(pc.upload_files(), ),
                width="60%", bg="green", color="white", size="md", space="1em", margin="2em", ),
            pc.divider(),
            # pc.image(src=State.img, height="18em", width="18em", ),
            # pc.divider(),
            pc.cond(State.image_made,
                    pc.image(src=State.img, height="18em", width="18em", ), ),
            pc.divider(),
            pc.cond(State.image_made,
                    pc.badge("Samantha recognized the image as:", variant="subtle", color_scheme="yellow"),
                    # pc.circular_progress(is_indeterminate=True),
                    ),
            pc.cond(
                State.image_made,
                pc.text(State.answer, padding="2em", ),
            ), ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Samantha")
app.compile()
