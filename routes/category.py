from app import app, render_template


@app.route('/admin/category')
def admin_category():
    return render_template("admin/category.html")