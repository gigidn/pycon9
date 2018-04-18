# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 Teuron S.r.l.
#    (<http://www.teuron.it>).
#
################################################################################

from odoo import models,fields, api, _


class odoo_service(models.Model):
    _name = 'odoo_service.odoo_service'
    _description = "Contratto Intercettazioni"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = "sequence, name, id"

    name = fields.Char()
    active = fields.Boolean(default=True,
        help="If the active field is set to False, it will allow you to hide the service without removing it.")
    state = fields.Selection([
            ('draft','Draft'),
            ('open', 'Open'),
            ('suspended', 'Suspendend'),
            ('closed', 'Closed'),
        ], string='Status', index=True, readonly=True, default='draft',
        track_visibility='onchange', copy=False,
        help=" * The 'Draft' status is used when a user is encoding a new and unconfirmed Contract.\n"
             " * The 'Open' status is used for running contract.\n"
             " * The 'Suspended' status is set automatically when add suspension.\n"
             " * The 'Closed' status is used when user close a contract.")
    sequence = fields.Integer(default=10, help="Gives the sequence order when displaying a list of Services.")
    partner_id = fields.Many2one('res.partner',
        string='Customer',
    )
    domain_name = fields.Char()
    image_type = fields.Selection(
        [
            ('ce','Community')
            ('ent','Enterprise')
        ]
    )
    start_date = fields.Date()
    end_date = fields.Date()
    image = fields.Char()
    stage_image = fields.Char()
    persistent_disk_name = fields.Char()
    persistent_disk_size = fields.Integer()
    create_git_repo = fields.Boolean()
    create_mail_relay = fields.Boolean()
    create_stage_instance = fields.Boolean()
    #deployment specific value
    db_address = fields.Char()
    db_user = fields.Char()
    db_password = fields.Char()
    data_dir = fields.Char()
    db_lock = fields.Boolean()
    db_check = fields.Boolean()
    deployment = fields.Text()
    config = fields.Text()
    web_config = fields.Text()

