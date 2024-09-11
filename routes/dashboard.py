from app import app, render_template


@app.route('/admin')
@app.route('/admin/dashboard')
def admin():
    return render_template("admin/dashboard.html")