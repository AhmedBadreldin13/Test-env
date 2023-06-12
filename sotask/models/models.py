# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrders(models.Model):
    _inherit = 'sale.order'

    customer_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Datetime(string='Date')
    line_ids = fields.One2many('s.o', 'link_id', string='Order Line')


class SO(models.Model):
    _name = 's.o'

    product = fields.Many2one("product.template", string='product')
    price = fields.Float(string='Price', store=True, readonly=False, required=True)
    quantity = fields.Integer(string="Quantity", default=1.0, store=True, required=True)
    subtotal = fields.Float(string="SubTotal", compute='_compute_amount', store=True, precompute=True)
    tax = fields.Float(string='tax')
    link_id = fields.Many2one('sale.order', string='link')

    @api.depends('quantity', 'price')
    def _compute_amount(self):
        for rec in self:
            rec.subtotal = rec.price * rec.quantity
