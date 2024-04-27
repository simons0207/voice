import os

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)


filename = "output_test.wav"


def text2speech(text):
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        SPEAK_OPTIONS = {"text": text}
        deepgram = DeepgramClient("79c26e7a4629dd68ee5d7771cbe1c6fab368a21a")

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    text2speech("This is a test")