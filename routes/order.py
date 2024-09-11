from app import app, render_template


@app.route('/admin/order')
def admin_order():
    return render_template("admin/order.html")