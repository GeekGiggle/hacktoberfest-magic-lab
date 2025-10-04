from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image
import io, os, tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        files = request.files.getlist('images')
        if not files:
            return redirect(request.url)
        frames = []
        for f in files:
            try:
                img = Image.open(f.stream).convert('RGBA').resize((480,320))
                frames.append(img)
            except Exception:
                continue
        if not frames:
            return "No valid images uploaded.", 400
        out = io.BytesIO()
        frames[0].save(out, format='GIF', save_all=True, append_images=frames[1:], loop=0, duration=int(request.form.get('duration',200)))
        out.seek(0)
        return send_file(out, mimetype='image/gif', as_attachment=True, download_name='dreamframe.gif')
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)
