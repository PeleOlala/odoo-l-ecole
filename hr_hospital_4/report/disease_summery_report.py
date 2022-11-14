from odoo import api, models, _
from odoo.exceptions import UserError


class DiseaseReportSummery(models.AbstractModel):
    _name = 'hr_hospital_3.report.disease_summery'
    _description = 'Disease summery report'

    @api.model
    def _get_report_values(self, docids, data=None):

        if not data.get('form'):
            raise UserError(_("Form content is missing, this report "
                              "cannot be printed."))

        return {
            'doc_ids': self.ids,
        }
