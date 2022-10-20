# -*- coding: utf-8 -*-
# from odoo import http


# class HrHospital2(http.Controller):
#     @http.route('/hr_hospital_2/hr_hospital_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_hospital_2/hr_hospital_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_hospital_2.listing', {
#             'root': '/hr_hospital_2/hr_hospital_2',
#             'objects': http.request.env['hr_hospital_2.hr_hospital_2'].search([]),
#         })

#     @http.route('/hr_hospital_2/hr_hospital_2/objects/<model("hr_hospital_2.hr_hospital_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_hospital_2.object', {
#             'object': obj
#         })
