# -*- coding: utf-8 -*-
from odoo import fields, models, api

class User(models.Model):
    _inherit = 'res.users'
    course_count = fields.Integer(compute='compute_course_count', string="Number of Course")
    course_ids = fields.One2many('openacademy.course', 'responsible_id' , string="Courses")

    facture_count = fields.Integer(compute='compute_facture_count', string="Number of Invoice")
    facture_ids = fields.One2many('account.move', 'partner_id' , string="Factures")

    def course_list(self):
        action = self.env.ref('openacademy.course_list_action').read()[0]
        action['domain']=[('id','in',self.course_ids.ids)]
        action['views'] = [(self.env.ref('openacademy.course_tree_view').id, 'tree'),
                           (self.env.ref('openacademy.course_form_view').id, 'form')]
        action['context']={'default_responsible_id':self.id}
        return action

    def facture_list(self):
        action = self.env.ref('account.action_move_in_invoice_type').read()[0]
        action['domain']=[('partner_id','=',self.partner_id.id)]
        action['views'] = [(self.env.ref('account.view_invoice_tree').id, 'tree'),
                           (self.env.ref('account.view_account_move_kanban').id, 'kanban')]
        action['context']={}
        return action

    @api.depends('course_ids')
    def compute_course_count(self):
        for r in self:
            r.course_count = len(self.course_ids)

    @api.depends('facture_ids')
    def compute_facture_count(self):
        for r in self:
            r.facture_count = len(self.facture_ids)