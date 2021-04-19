# -*- coding: utf-8 -*-

import pytz
import json
from odoo import _, api, fields, models


class EventEvent(models.Model):
    _inherit = 'event.event'

    date_tz = fields.Selection('_tz_get', string='Timezone', required=True, default='Egypt')
    organizer_ids = fields.Many2many('crm.team', 'event_team_rel', 'event_id', 'team_id', string='Organizer')
    attendee_ids = fields.Many2many('res.users', 'event_attendee_rel', 'event_id', 'user_id', string='Attendees')
    attendee_domain = fields.Char(compute="_compute_attendee_domain", readonly=True, store=False)

    @api.multi
    @api.depends('organizer_ids')
    def _compute_attendee_domain(self):
        for rec in self:
            domain = []
            if rec.organizer_ids:
                domain = json.dumps([('id', 'in', rec.organizer_ids.mapped('member_ids').ids)])
            rec.attendee_domain = domain

    @api.model
    def _tz_get(self):
        return [(x, x) for x in pytz.all_timezones]
