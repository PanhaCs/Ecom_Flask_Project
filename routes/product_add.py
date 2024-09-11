from app import app, render_template


@app.route('/admin/product_add')
def admin_product_add():
    return render_template("admin/product_add.html")