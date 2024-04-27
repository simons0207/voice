import tempfile
from text2speech import text2speech
from speech2text import speech2text
from groq import Groq
from flask import Flask ,request, send_file,render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-audio",methods=["POST"])
def process_audio_data():
    audio_data=request.files["audio"].read()

    with tempfile.NamedTemporaryFile(delete=False,suffix='.wav') as temp_audio:
        temp_audio.write(audio_data)
        temp_audio.flush()

    text=speech2text(temp_audio.name)
    client = Groq(
    api_key="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"
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        model="mixtral-8x7b-32768",
    )
    generated_answer=(chat_completion.choices[0].message.content)
    generated_speech=text2speech(generated_answer)

    return send_file(generated_speech,mimetype='audio/mpeg')

  
if __name__ =='__main__':
    app.run(debug=True,port=8080)