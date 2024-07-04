from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)


@app.route('/add', methods=['POST'])
def add_note():
    post = request.form['post']
    posts.append(post)
    return redirect(url_for('blog'))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_post(index):
    if request.method == 'POST':
        new_post = request.form['post']
        posts[index - 1] = new_post
        return redirect(url_for('blog'))
    else:
        post_to_edit = posts[index - 1]
        return render_template('edit.html', index=index, note=post_to_edit)


@app.route('/delete/<int:index>')
def delete_note(index):
    del posts[index - 1]
    return redirect(url_for('blog'))


if __name__ == '__main__':
    app.run(debug=True)
