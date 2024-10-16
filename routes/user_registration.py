from app import app, render_template


@app.route('/admin/user_registration')
def admin_user_registration():
    return render_template("admin/user_registration.html")