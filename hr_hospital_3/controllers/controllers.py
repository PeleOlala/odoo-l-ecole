# -*- coding: utf-8 -*-
# from odoo import http


# class HrHospital3(http.Controller):
#     @http.route('/hr_hospital_3/hr_hospital_3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_hospital_3/hr_hospital_3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_hospital_3.listing', {
#             'root': '/hr_hospital_3/hr_hospital_3',
#             'objects': http.request.env['hr_hospital_3.hr_hospital_3'].search([]),
#         })

#     @http.route('/hr_hospital_3/hr_hospital_3/objects/<model("hr_hospital_3.hr_hospital_3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_hospital_3.object', {
#             'object': obj
#         })
