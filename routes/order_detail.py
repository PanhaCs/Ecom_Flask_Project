from app import app, render_template


@app.route('/admin/order_detail')
def admin_order_detail():
    return render_template("admin/order_detail.html")