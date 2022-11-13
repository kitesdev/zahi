odoo.define('pos_payment_different_access.ClosePosPopup', function (require) {
    'use strict';

    const ClosePosPopup = require('point_of_sale.ClosePosPopup');
    const Registries = require('point_of_sale.Registries');

    const PosPaymentDiffAccessClosePopup = (ClosePosPopup) =>
        class extends ClosePosPopup {
        hasUserAuthority() {
            const absDifferences = Object.entries(this.state.payments).map(pm => Math.abs(pm[1].difference));
            return this.isManager && this.amountAuthorizedDiff == null || Math.max(...absDifferences) <= this.amountAuthorizedDiff;
        }
        };

    Registries.Component.extend(ClosePosPopup, PosPaymentDiffAccessClosePopup);

    return ClosePosPopup;
});
