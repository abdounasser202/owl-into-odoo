from odoo import http


class Hello(http.Controller):
    @http.route('/hello', auth='public')
    def index(self, **kwargs):
        return http.request.render('hello_owl.index')
