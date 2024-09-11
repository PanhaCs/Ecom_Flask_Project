from app import app, render_template


@app.route('/admin/product_edit')
def admin_product_edit():
    return render_template("admin/product_edit.html")