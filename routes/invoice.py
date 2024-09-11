from app import app, render_template


@app.route('/admin/invoice')
def admin_invoice():
    return render_template("admin/invoice.html")