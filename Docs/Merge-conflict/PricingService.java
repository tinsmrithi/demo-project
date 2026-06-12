package com.shopwave.orders.service;

import com.shopwave.orders.model.Customer;
import com.shopwave.orders.model.PricingRule;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;

/**
 * Applies pricing rules and discounts to order totals.
 */
@Service
public class PricingService {

    private final PricingRuleEngine ruleEngine;

    public PricingService(PricingRuleEngine ruleEngine) {
        this.ruleEngine = ruleEngine;
    }

    /**
     * Applies the appropriate discount for the given customer.
     * Returns the discounted total, or the original total if no discount applies.
     */
    public BigDecimal applyDiscount(Customer customer, BigDecimal orderTotal) {
        PricingRule rule = ruleEngine.getRuleForCustomer(customer);
        return rule.apply(orderTotal);
    }

    /**
     * Calculates the base price for a B2B customer based on volume tier.
     * Tiers: 0–99 units = list price, 100–499 = 5% off, 500+ = 12% off.
     */
    public BigDecimal applyB2BVolumeTier(int quantity, BigDecimal unitPrice) {
        BigDecimal total = unitPrice.multiply(BigDecimal.valueOf(quantity));
        if (quantity >= 500) {
            return total.multiply(BigDecimal.valueOf(0.88));
        } else if (quantity >= 100) {
            return total.multiply(BigDecimal.valueOf(0.95));
        }
        return total;
    }
}