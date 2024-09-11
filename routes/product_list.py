from app import app, render_template


@app.route('/admin/product')
def admin_product():
    return render_template("admin/product_list.html")